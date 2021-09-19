from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, DateField, TimeField, HiddenField
from wtforms.validators import InputRequired, Email, Length, DataRequired


class LoginForm(FlaskForm):
    email = StringField('Email', [DataRequired(), Email("Must Be a Valid Email")])
    password = PasswordField('Password', [DataRequired()])
    submit = SubmitField('Submit')

class ContactForm(FlaskForm):
    email = StringField("Email", [DataRequired(), Email("Must Be a Valid Email")])
    subject = StringField("Subject", validators=[DataRequired()])
    content = TextAreaField("How can we Help", validators=[DataRequired(), Length(min=25)])
    submit = SubmitField('Submit')

class CreateMeetingForm(FlaskForm):
    host = StringField("Host Name", [DataRequired()])
    date = DateField("Date", [DataRequired()])
    time = TimeField("Time", [DataRequired()])
    link = StringField("Zoom Link")
    submit = SubmitField('Submit')

class EditMeetingForm(FlaskForm):
    host = StringField("Host Name", [DataRequired()])
    date = DateField("Date", [DataRequired()])
    time = TimeField("Time", [DataRequired()])
    link = StringField("Zoom Link")
    submit = SubmitField('Submit')

class MailingListJoinForm(FlaskForm):
    email = StringField("Email", [DataRequired(), Email()])
    submit = SubmitField('Submit')

class CreateEventForm(FlaskForm):
    date = DateField("Date", [DataRequired()])
    title = StringField("Title", [DataRequired()])
    time = TimeField("Time", [DataRequired()])
    location = StringField("Zoom Link")
    submit = SubmitField('Submit')

class EditEventForm(FlaskForm):
    date = DateField("Date", [DataRequired()])
    title = StringField("Title", [DataRequired()])
    time = TimeField("Time", [DataRequired()])
    location = StringField("Zoom Link")
    submit = SubmitField('Submit')

class CreateEmailForm(FlaskForm):
    subject = StringField("Subject", [DataRequired()])
    content = TextAreaField("Content", [DataRequired()])
    submit = SubmitField("Send")