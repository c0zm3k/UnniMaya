from flask import render_template, url_for, flash, redirect, request, Blueprint
from .extensions import db
from .models import User, Course, College, Feedback, Job, Internship
from .forms import RecommendationForm
from flask_login import login_required, current_user
from .ml_model import recommendation_engine

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def index():
    return render_template('index.html')

@main.route("/dashboard")
@login_required
def dashboard():
    if current_user.role == 'admin':
        return redirect(url_for('admin_bp.dashboard'))
    return render_template('dashboard_user.html', title='Dashboard')

@main.route("/recommend", methods=['GET', 'POST'])
@login_required
def recommend():
    form = RecommendationForm()
    if form.validate_on_submit():
        # Get Enhanced AI Prediction
        rec_data = recommendation_engine.get_recommendations(
            current_user.qualification, 
            form.interests.data, 
            form.skills.data
        )
        predicted_course = rec_data['suggested_course']
        
        # Save user preferences
        current_user.skills = form.skills.data
        current_user.interests = form.interests.data
        current_user.experience = form.experience.data
        db.session.commit()
        
        # 1. Academic Path (Colleges & Courses)
        recommended_colleges = []
        suggested_courses = []
        
        target_lvls = rec_data.get('target_levels', [])
        if target_lvls:
            # Recommend colleges offering this path
            recommended_colleges = College.query.filter(College.affiliates.contains(predicted_course)).all()
            if not recommended_colleges:
                recommended_colleges = College.query.limit(3).all()
            
            # Recommend courses for those levels
            suggested_courses = Course.query.filter(Course.level.in_(target_lvls)).limit(6).all()

        # 2. Career Path (Jobs & Internships)
        jobs = []
        internships = []
        
        # Logic: If UG or PG, show jobs and internships requiring that or lower qualification
        if current_user.qualification in ['UG', 'PG']:
            jobs = Job.query.filter_by(qualification_required=current_user.qualification).all()
            internships = Internship.query.filter_by(qualification_required=current_user.qualification).all()
            
            # Fallback for demo
            if not jobs: jobs = Job.query.limit(2).all()
            if not internships: internships = Internship.query.limit(2).all()

        job_roles = recommendation_engine.get_job_roles(predicted_course)

        return render_template('results.html', title='Recommendations', 
                               course=predicted_course, 
                               colleges=recommended_colleges, 
                               job_roles=job_roles,
                               jobs=jobs,
                               internships=internships,
                               suggested_courses=suggested_courses,
                               qualification=current_user.qualification)
    return render_template('recommendation_form.html', title='Get Recommendations', form=form)
