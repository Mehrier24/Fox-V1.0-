from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, TelField
from wtforms.validators import DataRequired, Length, Email, EqualTo


# Registration Form
class RegistrationForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[
            DataRequired(),
            Length(min=4, max=25, message="Username must be between 4 and 25 characters")
        ]
    )
    email = EmailField(
        "Email",
        validators=[
            DataRequired(),
            Email(message="Enter a valid email address")
        ]
    )
    phone = TelField(
        "Phone",
        validators=[
            DataRequired(),
            Length(min=10, max=15, message="Phone number must be between 10 and 15 digits")
        ]
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=6, message="Password must be at least 6 characters")
        ]
    )
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(),
            EqualTo("password", message="Passwords must match")
        ]
    )
    submit = SubmitField("Register")


# Login Form
class LoginForm(FlaskForm):
    email = EmailField(
        "Email",
        validators=[
            DataRequired(),
            Email(message="Enter a valid email address")
        ]
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired()]
    )
    submit = SubmitField("Login")


# OTP Verification Form
class OTPForm(FlaskForm):
    otp = StringField(
        "Enter OTP",
        validators=[
            DataRequired(),
            Length(min=6, max=6, message="OTP must be 6 digits")
        ]
    )
    submit = SubmitField("Verify")


# Book Entry Form
class BookEntryForm(FlaskForm):
    title = StringField(
        "Book Title",
        validators=[
            DataRequired(),
            Length(max=200, message="Title cannot be longer than 200 characters")
        ]
    )
    author = StringField(
        "Author",
        validators=[
            DataRequired(),
            Length(max=100, message="Author name cannot be longer than 100 characters")
        ]
    )
    submit = SubmitField("Add Book")
