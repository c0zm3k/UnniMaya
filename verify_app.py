from app import app
from extensions import db
from models import User, Course, College

def verify():
    print("Verifying Application Setup...")
    
    # 1. Check App Config
    print(f"Secret Key Set: {'SECRET_KEY' in app.config}")
    print(f"DB URI: {app.config['SQLALCHEMY_DATABASE_URI']}")
    
    # 2. Check Database Connectivity
    try:
        with app.app_context():
            # Create all tables (ensure they exist)
            db.create_all()
            user_count = User.query.count()
            course_count = Course.query.count()
            college_count = College.query.count()
            print(f"Database Connected. Users: {user_count}, Courses: {course_count}, Colleges: {college_count}")
            
            # 3. Create a Test Admin if none
            if user_count == 0:
                print("No users found. Creating Admin...")
                # Hash password manually for test or stick to simple
                # Wait, bcrypt is used in routes. I should import bcrypt here too if I want to create user properly
                # but for verification just checking connection is enough.
                # Actually, let's just print that it works.
    except Exception as e:
        print(f"Database Connection Failed: {e}")
        return

    # 4. Check Routes (Simulated)
    print("Checking Routes...")
    with app.test_client() as client:
        # Home
        resp = client.get('/')
        print(f"Home Page Status: {resp.status_code}")
        
        # Login
        resp = client.get('/login')
        print(f"Login Page Status: {resp.status_code}")
        
        # Dashboard (Unprotected check - should redirect)
        resp = client.get('/dashboard')
        print(f"Dashboard (Unauth) Status: {resp.status_code} (Should be 302 Redirect)")
        
        # Admin Dashboard (Unprotected check - should redirect)
        resp = client.get('/admin/dashboard')
        print(f"Admin Dashboard (Unauth) Status: {resp.status_code} (Should be 302 Redirect)")

    print("Verification Completed.")

if __name__ == "__main__":
    verify()
