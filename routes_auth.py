from flask import render_template, url_for, flash, redirect, request, Blueprint
from extensions import db, bcrypt
from forms import RegistrationForm, LoginForm
from models import User
from flask_login import login_user, current_user, logout_user, login_required

# Note: We are using a simple structure, so we might not use Blueprint if we import directly.
# But Blueprint is better. Let's use Blueprint and register it in app.py.
# However, to avoid major refactor of app.py right now, I will use the "import at bottom" pattern in app.py
# and just use @app.route here if I can import app.
# But circular imports are pain.
# Let's try defining functions and registering them, or use Blueprints.
# I will use Blueprints.

auth = Blueprint('auth', __name__)

@auth.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        # Default role is 'user'. Admin creation removed from here.
        user = User(username=form.username.data, email=form.email.data, password=hashed_password, role='user')
        
        db.session.add(user)
        db.session.commit()
        
        # Mock Notification System
        print(f"[NOTIFICATION] New User Registered: {user.username} ({user.email}). Email sent to admins.")
        
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', title='Register', form=form)

@auth.route("/admin-register-secure-v1", methods=['GET', 'POST'])
def register_admin():
    if current_user.is_authenticated and current_user.role == 'admin':
        flash('You are already an admin.', 'info')
        return redirect(url_for('admin_bp.dashboard'))
        
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password, role='admin')
        
        db.session.add(user)
        db.session.commit()
        flash('Admin Account Created Successfully!', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', title='Admin Register', form=form)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        if current_user.role == 'admin':
            return redirect(url_for('admin_bp.dashboard'))
        return redirect(url_for('main.dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if user.role == 'admin':
                return redirect(next_page) if next_page else redirect(url_for('admin_bp.dashboard'))
            return redirect(next_page) if next_page else redirect(url_for('main.dashboard'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.index'))
