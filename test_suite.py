import unittest
from app import app
from extensions import db, bcrypt
from models import User, Course, College

class SystemTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False # Disable CSRF for testing convenience
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:' # Use in-memory DB
        self.app = app.test_client()
        self.ctx = app.app_context()
        self.ctx.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.ctx.pop()

    def register(self, username, email, password):
        return self.app.post('/register', data=dict(
            username=username,
            email=email,
            password=password,
            confirm_password=password
        ), follow_redirects=True)

    def login(self, email, password):
        return self.app.post('/login', data=dict(
            email=email,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def test_registration_and_login(self):
        # Good Registration
        resp = self.register('testuser', 'test@example.com', 'password123')
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b'Log In', resp.data) # Should redirect to login page (or login immediately? Route says redirect to login)
        
        # Duplicate Registration
        resp = self.register('testuser', 'test@example.com', 'password123')
        self.assertIn(b'That username is taken', resp.data)

        # Login
        resp = self.login('test@example.com', 'password123')
        self.assertIn(b'Dashboard', resp.data)

    def test_admin_access(self):
        # Create Admin (First user)
        self.register('admin', 'admin@example.com', 'adminpass')
        self.login('admin@example.com', 'adminpass')
        
        # Check Admin Dashboard
        resp = self.app.get('/admin/dashboard', follow_redirects=True)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b'Admin Dashboard', resp.data)
        self.logout()

        # Create Normal User
        self.register('user', 'user@example.com', 'userpass')
        self.login('user@example.com', 'userpass')
        
        # Check Admin Access Denied
        resp = self.app.get('/admin/dashboard')
        self.assertEqual(resp.status_code, 403)

    def test_recommendation_flow(self):
        self.register('user2', 'user2@example.com', 'pass')
        self.login('user2@example.com', 'pass')
        
        resp = self.app.post('/recommend', data=dict(
            skills='python, ai',
            interests='data science',
            experience='Beginner'
        ), follow_redirects=True)
        
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b'Recommended Career Path', resp.data)

if __name__ == '__main__':
    unittest.main()
