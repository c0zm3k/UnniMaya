from flask import Blueprint, jsonify, request, abort
from .models import Course, College, Job, Internship
import os

api_bp = Blueprint('api_bp', __name__)

API_KEY = os.environ.get('API_KEY', 'futurefit-dev-key-789')

def require_api_key(func):
    def wrapper(*args, **kwargs):
        if request.headers.get('x-api-key') != API_KEY:
            return jsonify({'error': 'Unauthorized: Invalid API Key'}), 401
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper

@api_bp.route('/api/courses', methods=['GET'])
@require_api_key
def get_courses():
    query = Course.query
    search = request.args.get('search')
    level = request.args.get('level')
    stream = request.args.get('stream')
    mode = request.args.get('mode')
    
    if search:
        query = query.filter(Course.title.contains(search) | Course.description.contains(search))
    if level and level != 'all':
        query = query.filter_by(level=level)
    if stream and stream != 'all':
        query = query.filter_by(stream=stream)
    if mode and mode != 'all':
        query = query.filter_by(mode=mode)
        
    limit = 20 if (search or (level and level != 'all') or (stream and stream != 'all')) else 5
    courses = query.limit(limit).all()
    courses_list = [{'id': c.id, 'title': c.title, 'description': c.description, 'skills_required': c.skills_required, 'level': c.level, 'stream': c.stream, 'mode': c.mode} for c in courses]
    return jsonify(courses_list)

@api_bp.route('/api/colleges', methods=['GET'])
@require_api_key
def get_colleges():
    query = College.query
    search = request.args.get('search')
    location = request.args.get('location')
    inst_type = request.args.get('type')
    fees_max = request.args.get('fees_max')
    
    if search:
        query = query.filter(College.name.contains(search) | College.location.contains(search))
    if location and location != 'all':
        query = query.filter_by(location=location)
    if inst_type and inst_type != 'all':
        query = query.filter_by(institute_type=inst_type)
    if fees_max:
        try: query = query.filter(College.fees <= int(fees_max))
        except: pass
        
    limit = 20 if (search or (location and location != 'all') or inst_type) else 5
    colleges = query.limit(limit).all()
    colleges_list = [{'id': c.id, 'name': c.name, 'location': c.location, 'type': c.institute_type, 'fees': c.fees, 'cutoff': c.cutoff_score} for c in colleges]
    return jsonify(colleges_list)

@api_bp.route('/api/jobs', methods=['GET'])
@require_api_key
def get_jobs():
    query = Job.query
    search = request.args.get('search')
    mode = request.args.get('mode')
    exp = request.args.get('experience')
    role = request.args.get('role')
    
    if search:
        query = query.filter(Job.title.contains(search) | Job.company.contains(search) | Job.description.contains(search))
    if mode and mode != 'all':
        query = query.filter_by(work_mode=mode)
    if exp and exp != 'all':
        query = query.filter_by(experience_level=exp)
    if role and role != 'all':
        query = query.filter_by(role_type=role)
        
    limit = 20 if (search or (mode and mode != 'all') or exp) else 5
    jobs = query.limit(limit).all()
    jobs_data = [{'id': j.id, 'title': j.title, 'company': j.company, 'mode': j.work_mode, 'exp': j.experience_level, 'salary': j.salary_range} for j in jobs]
    return jsonify(jobs_data)

@api_bp.route('/api/internships', methods=['GET'])
@require_api_key
def get_internships():
    query = Internship.query
    search = request.args.get('search')
    mode = request.args.get('mode')
    exp = request.args.get('experience')
    
    if search:
        query = query.filter(Internship.title.contains(search) | Internship.company.contains(search) | Internship.description.contains(search))
    if mode and mode != 'all':
        query = query.filter_by(work_mode=mode)
    if exp and exp != 'all':
        query = query.filter_by(experience_level=exp)
        
    limit = 20 if (search or (mode and mode != 'all') or exp) else 5
    internships = query.limit(limit).all()
    interns_data = [{'id': i.id, 'title': i.title, 'company': i.company, 'mode': i.work_mode, 'exp': i.experience_level, 'stipend': i.stipend} for i in internships]
    return jsonify(interns_data)
