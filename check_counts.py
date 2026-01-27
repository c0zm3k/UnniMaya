from app import app
from extensions import db
from models import College, Course, Job, Internship

with app.app_context():
    print(f"Colleges: {College.query.count()}")
    print(f"Courses: {Course.query.count()}")
    print(f"Jobs: {Job.query.count()}")
    print(f"Internships: {Internship.query.count()}")
