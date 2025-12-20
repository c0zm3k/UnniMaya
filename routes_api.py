from flask import Blueprint, jsonify, request, abort
from models import Course, College
import os

api_bp = Blueprint('api_bp', __name__)

API_KEY = os.environ.get('API_KEY', 'default-api-key-123')

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
    courses = Course.query.all()
    # Serialize
    courses_list = [{'id': c.id, 'title': c.title, 'description': c.description, 'skills_required': c.skills_required} for c in courses]
    return jsonify(courses_list)

@api_bp.route('/api/colleges', methods=['GET'])
@require_api_key
def get_colleges():
    colleges = College.query.all()
    # Serialize
    colleges_list = [{'id': c.id, 'name': c.name, 'location': c.location, 'affiliates': c.affiliates, 'cutoff_score': c.cutoff_score, 'fees': c.fees} for c in colleges]
    return jsonify(colleges_list)
