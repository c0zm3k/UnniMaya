from flask import render_template, url_for, flash, redirect, request, Blueprint, abort
from extensions import db
from models import User, Course, College
from forms import CourseForm, CollegeForm
from flask_login import login_required, current_user

admin_bp = Blueprint('admin_bp', __name__)

@admin_bp.route("/admin/dashboard")
@login_required
def dashboard():
    if current_user.role != 'admin':
        abort(403)
    users_count = User.query.count()
    courses_count = Course.query.count()
    colleges_count = College.query.count()
    return render_template('dashboard_admin.html', title='Admin Dashboard', 
                           users_count=users_count, courses_count=courses_count, colleges_count=colleges_count)

@admin_bp.route("/admin/course/new", methods=['GET', 'POST'])
@login_required
def new_course():
    if current_user.role != 'admin':
        abort(403)
    form = CourseForm()
    if form.validate_on_submit():
        course = Course(title=form.title.data, description=form.description.data, skills_required=form.skills_required.data)
        db.session.add(course)
        db.session.commit()
        flash('Course has been created!', 'success')
        return redirect(url_for('admin_bp.dashboard'))
    return render_template('create_course.html', title='New Course', form=form, legend='New Course')

@admin_bp.route("/admin/college/new", methods=['GET', 'POST'])
@login_required
def new_college():
    if current_user.role != 'admin':
        abort(403)
    form = CollegeForm()
    if form.validate_on_submit():
        college = College(name=form.name.data, location=form.location.data, 
                          affiliates=form.affiliates.data, cutoff_score=form.cutoff_score.data, fees=form.fees.data)
        db.session.add(college)
        db.session.commit()
        flash('College has been created!', 'success')
        return redirect(url_for('admin_bp.dashboard'))
    return render_template('create_college.html', title='New College', form=form, legend='New College')

@admin_bp.route("/admin/users")
@login_required
def view_users():
    if current_user.role != 'admin':
        abort(403)
    users = User.query.all()
    return render_template('admin_users.html', users=users, title='Manage Users')

@admin_bp.route("/admin/courses")
@login_required
def view_courses():
    if current_user.role != 'admin':
        abort(403)
    courses = Course.query.all()
    return render_template('admin_courses.html', courses=courses, title='Manage Courses')

@admin_bp.route("/admin/colleges")
@login_required
def view_colleges():
    if current_user.role != 'admin':
        abort(403)
    colleges = College.query.all()
    return render_template('admin_colleges.html', colleges=colleges, title='Manage Colleges')
