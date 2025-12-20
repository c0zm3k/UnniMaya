from flask import render_template, url_for, flash, redirect, request, Blueprint
from extensions import db
from models import User, Course, College, Feedback
from forms import RecommendationForm
from flask_login import login_required, current_user
from ml_model import recommendation_engine

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
        # Get AI Prediction
        predicted_course = recommendation_engine.predict(form.interests.data, form.skills.data)
        
        # Save user preferences
        current_user.skills = form.skills.data
        current_user.interests = form.interests.data
        current_user.experience = form.experience.data
        db.session.commit()
        
        # Filter Colleges
        # Simple Logic: Recommend all colleges offering the predicted course (or related)
        # In this demo model, we match string in 'affiliates'
        recommended_colleges = College.query.filter(College.affiliates.contains(predicted_course)).all()
        # If no strict match, return all for demo
        if not recommended_colleges:
             recommended_colleges = College.query.all()
             
        job_roles = recommendation_engine.get_job_roles(predicted_course)

        return render_template('results.html', title='Recommendations', 
                               course=predicted_course, colleges=recommended_colleges, job_roles=job_roles)
    return render_template('recommendation_form.html', title='Get Recommendations', form=form)
