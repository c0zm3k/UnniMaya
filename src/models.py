from .extensions import db, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(10), nullable=False, default='user') # 'user' or 'admin'
    
    # Profile Data for Recommendations
    qualification = db.Column(db.String(20), nullable=False, default='12th') # '12th', 'UG', 'PG'
    skills = db.Column(db.String(200)) # stored as comma-separated string
    interests = db.Column(db.String(200))
    experience = db.Column(db.String(50))
    
    feedbacks = db.relationship('Feedback', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.qualification}')"

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    skills_required = db.Column(db.String(200), nullable=False)
    level = db.Column(db.String(20), nullable=False, default='UG') # 'Diploma', 'UG', 'PG'
    stream = db.Column(db.String(50)) # 'Engineering', 'Medical', 'Arts', etc.
    duration = db.Column(db.String(50)) # '3 Years', '4 Years', etc.
    mode = db.Column(db.String(50), default='Full-time') # 'Full-time', 'Online', 'Part-time'
    
    def __repr__(self):
        return f"Course('{self.title}', '{self.level}')"

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    skills_required = db.Column(db.String(200), nullable=False)
    qualification_required = db.Column(db.String(20), nullable=False) # 'Diploma', 'UG', 'PG'
    work_mode = db.Column(db.String(20), nullable=False, default='Onsite') # 'Onsite', 'Hybrid', 'WFH'
    role_type = db.Column(db.String(50), default='Full-Time')
    experience_level = db.Column(db.String(50), default='Fresher')
    salary_range = db.Column(db.String(50))

    def __repr__(self):
        return f"Job('{self.title}', '{self.company}', '{self.work_mode}')"

class Internship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    skills_required = db.Column(db.String(200), nullable=False)
    duration = db.Column(db.String(50))
    qualification_required = db.Column(db.String(20), nullable=False) # 'Diploma', 'UG', 'PG'
    work_mode = db.Column(db.String(20), nullable=False, default='Onsite') # 'Onsite', 'Hybrid', 'WFH'
    experience_level = db.Column(db.String(50), default='Fresher')
    stipend = db.Column(db.String(50))

    def __repr__(self):
        return f"Internship('{self.title}', '{self.company}', '{self.work_mode}')"

class College(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    affiliates = db.Column(db.String(200)) # Courses offered
    cutoff_score = db.Column(db.Integer)
    fees = db.Column(db.Integer)
    institute_type = db.Column(db.String(50)) # 'Government', 'Private', 'Deemed'
    ranking = db.Column(db.Integer) # NIRF Ranking
    facilities = db.Column(db.String(200)) # comma separated: 'Hostel,WiFi,etc'
    
    def __repr__(self):
        return f"College('{self.name}', '{self.location}')"

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Feedback('{self.content[:20]}...')"
