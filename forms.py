from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
        DataRequired(),
        # Strong Password Policy:
        # At least 8 chars, 1 uppercase, 1 lowercase, 1 number, 1 special char
        # Note: wtforms Regexp requires import
    ])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_password(self, password):
        import re
        # Regex: 
        # (?=.*[a-z]) : At least 1 lowercase
        # (?=.*[A-Z]) : At least 1 uppercase
        # (?=.*\d)    : At least 1 digit
        # (?=.*[@$!%*?&]) : At least 1 special char (customize list as needed)
        # [A-Za-z\d@$!%*?&]{8,} : At least 8 chars allowed
        
        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        
        if not re.match(pattern, password.data):
             raise ValidationError('Password must be at least 8 characters long and include an uppercase letter, a lowercase letter, a number, and a special character (@$!%*?&).')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class RecommendationForm(FlaskForm):
    skills = StringField('Skills (comma separated)', validators=[DataRequired()])
    interests = StringField('Interests (comma separated)', validators=[DataRequired()])
    experience = SelectField('Experience Level', choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')])
    submit = SubmitField('Get Recommendations')

class CourseForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    skills_required = StringField('Skills Required', validators=[DataRequired()])
    submit = SubmitField('Add Course')

class CollegeForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    affiliates = StringField('Courses (comma separated)', validators=[DataRequired()])
    cutoff_score = IntegerField('Cutoff Score')
    fees = IntegerField('Fees')
    submit = SubmitField('Add College')
