import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from app import app
    from src.extensions import db
    from src.models import Course, College, Job, Internship
    from src.routes_api import API_KEY
    import os

    with app.app_context():
        print(f"Courses count: {Course.query.count()}")
        print(f"Colleges count: {College.query.count()}")
        print(f"Jobs count: {Job.query.count()}")
        print(f"Internships count: {Internship.query.count()}")
        print(f"API_KEY from src.routes_api: '{API_KEY}'")
        print(f"API_KEY from os.environ: '{os.environ.get('API_KEY')}'")
        
except Exception as e:
    print(f"Error: {e}")
