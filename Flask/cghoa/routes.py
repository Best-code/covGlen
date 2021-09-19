from cghoa.models import User, Event, Meeting, MailingList
from flask import render_template, redirect, url_for, flash, request
from cghoa.forms import LoginForm, ContactForm, CreateMeetingForm, MailingListJoinForm, EditMeetingForm, CreateEventForm, CreateEmailForm, EditEventForm
from cghoa import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
from mailer import Mailer

contactPageEmail = "cpmraygun@gmail.com"
contactPagePassword ="Cpmbingo"

recievingEmailAddress = "cpmraygun@gmail.com"

def flash_error(form):
    """Flashes form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))

@app.route("/", methods=['GET','POST'])
@app.route("/home", methods=['GET','POST'])
def homePage():
    form = MailingListJoinForm()
    if form.is_submitted():
        if form.validate_on_submit():
            email = form.email.data
            db.session.add(MailingList(email=email))
            db.session.commit()
            flash("You have successfully joined the mailing list", 'success')
            return redirect(url_for("homePage"))
        flash_error(form)
    props = {'title':'Home', 'user':current_user}
    return render_template('cgHome.html', props=props, form=form)


@app.route("/board")
def teamPage():
    props = {'title':'Board', 'user':current_user}
    return render_template('cgTeam.html', props=props)

@app.route('/login', methods=["GET","POST"])
def loginPage():
    form = LoginForm()
    if form.is_submitted():
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and (user.password == form.password.data):
                login_user(user)
                flash('You are now logged in ' + current_user.username, 'success')
                return redirect(url_for("homePage"))
            else:
                flash("Login Unsuccessful. Please Check Email and Password",'error')
        flash_error(form)
    props = {'title':'Login', 'user':current_user}
    return render_template('cgLogin.html', props=props, form=form)

@app.route("/logout")
@login_required
def logout():
    flash("You are now logged out", "success")
    logout_user()
    return redirect(url_for("homePage"))

@app.route('/meetings', methods=['GET',"POST"])
def meetingsPage():
    props = {'title':'Meetings', 'user':current_user, 'meetings':Meeting.query.all()}
    return render_template('cgMeetings.html', props=props)

@app.route("/edit-meeting/<int:meetingID>", methods=['GET','POST'])
@login_required
def editMeeting(meetingID):
    form = EditMeetingForm()
    meeting = Meeting.query.get_or_404(meetingID)
    if form.validate_on_submit():
        meeting.host = form.host.data
        meeting.time = form.time.data
        meeting.date = form.date.data
        meeting.dateText = form.date.data.strftime("%B %d")
        meeting.timeText = form.time.data.strftime("%I:%M %p") 
        meeting.link = form.link.data
        db.session.commit()
        flash("You have successfully updated the meeting", "success")
        return redirect(url_for("meetingsPage"))
    elif request.method == 'GET':
        form.host.data = meeting.host
        form.date.data = meeting.date
        form.time.data = meeting.time
        form.link.data = meeting.link
    props = {'title':'Update Meeting', 'user':current_user}
    return render_template("cgEditMeeting.html", props=props, form=form, meetingID_in=meetingID)

@app.route("/create-meeting", methods=['GET','POST'])
@login_required    
def newMeeting():
    if not current_user.is_authenticated:
        flash("You must be Logged in to access that page.", "danger")
        return redirect(url_for("homePage"))
    form = CreateMeetingForm()
    props = {'title':'Create Meeting', 'user':current_user}
    if form.validate_on_submit():
        host = form.host.data
        time = form.time.data
        date = form.date.data
        dateText = form.date.data.strftime("%B %d")
        timeText = form.time.data.strftime("%I:%M %p")
        link = form.link.data
        db.session.add(Meeting(host=host,date=date,time=time,link=link, dateText=dateText,timeText=timeText))
        db.session.commit()
        flash("You successfully created a meeting.", "success")
        return redirect(url_for("meetingsPage"))
    return render_template("cgCreateMeeting.html", props=props, form=form)
    
@app.route("/delete-meeting/<int:meetingID>", methods=['GET','POST'])
@login_required
def deleteMeeting(meetingID):
    db.session.delete(Meeting.query.get_or_404(meetingID))
    db.session.commit()
    flash("Meeting successfully deleted", "success")
    return redirect(url_for("meetingsPage"))

@app.route('/contact', methods=['GET','POST'])
def contactPage():
    form = ContactForm()
    if form.is_submitted():
        if form.validate_on_submit():
            mail = Mailer(email=contactPageEmail, password=contactPagePassword)
            sender = form.email.data
            subject = form.subject.data
            content = form.content.data
            message=f"""We have received a message today from: '{sender}'

Subject: 
    '{subject}''

    
Content: 
    '{content}'"""
            mail.send(receiver=recievingEmailAddress, subject=f"Incoming Message from {sender}", message=message)
            flash("Thanks for reaching out!", 'success')
            return redirect(url_for("homePage"))
        flash_error(form)
    props = {'title':'Contact Us', 'user':current_user}
    return render_template('cgContact.html', props=props, form=form)

@app.route('/events')
def eventsPage():
    props = {'title':'Events', 'user':current_user, 'events':Event.query.all()}
    return render_template('cgEvents.html', props=props)

@app.route("/create-event", methods=['GET','POST'])
@login_required    
def newEvent():
    if not current_user.is_authenticated:
        flash("You must be Logged in to access that page.", "danger")
        return redirect(url_for("homePage"))
    form = CreateEventForm()
    props = {'title':'Create Event', 'user':current_user}
    if form.validate_on_submit():
        time = form.time.data
        title = form.title.data
        date = form.date.data
        location = form.location.data
        dateText = form.date.data.strftime("%B %d")
        timeText = form.time.data.strftime("%I:%M %p")
        db.session.add(Event(location=location, date=date, time=time, title=title, dateText=dateText, timeText=timeText))
        db.session.commit()
        flash("You successfully created a meeting.", "success")
        return redirect(url_for("eventsPage"))
    return render_template("cgCreateEvent.html", props=props, form=form)

@app.route("/edit-event/<int:eventID>", methods=['GET','POST'])
@login_required
def editEvent(eventID):
    form = EditEventForm()
    event = Event.query.get_or_404(eventID)
    if form.validate_on_submit():
        event.title = form.title.data
        event.time = form.time.data
        event.date = form.date.data
        event.dateText = form.date.data.strftime("%B %d")
        event.timeText = form.time.data.strftime("%I:%M %p") 
        event.location = form.location.data
        db.session.commit()
        flash("You have successfully updated the event", "success")
        return redirect(url_for("eventsPage"))
    elif request.method == 'GET':
        form.title.data = event.title
        form.date.data = event.date
        form.time.data = event.time
        form.location.data = event.location
    props = {'title':'Update Event', 'user':current_user}
    return render_template("cgEditEvent.html", props=props, form=form, eventID_in=eventID)


@app.route("/delete-event/<int:eventID>", methods=['GET','POST'])
@login_required
def deleteEvent(eventID):
    db.session.delete(Event.query.get_or_404(eventID))
    db.session.commit()
    flash("Event successfully deleted", "success")
    return redirect(url_for("eventsPage"))


@app.route("/create-email", methods=['GET','POST'])
@login_required
def createEmail():
    form = CreateEmailForm()
    if form.validate_on_submit():
        recipients = [str(x) for x in db.session.query(MailingList).all()]
        mail = Mailer(email="cpmraygun@gmail.com", password="Cpmbingo")
        if(recipients):
            mail.send(receiver=recipients, subject=form.subject.data, message=form.content.data)
            flash("Email sent succesfully", "success")
            return redirect(url_for("homePage"))
        else:
            flash("We currently have no recipients", "danger")
            return redirect(url_for("createEmail"))
    props = {'title':'Create Email', 'user':current_user}
    return render_template("cgCreateEmail.html", props=props, form=form)
