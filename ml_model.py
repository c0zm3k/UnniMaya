import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder
import pickle
import os

# Dummy Dataset to train the model initially
data = {
    'Interest': ['AI', 'Data', 'Web', 'Security', 'AI', 'Data', 'Web', 'Security'],
    'Skill': ['Python', 'Statistics', 'HTML/CSS', 'Networking', 'Math', 'SQL', 'JS', 'Linux'],
    'Course': ['AI & ML', 'Data Science', 'Full Stack Dev', 'Cybersecurity', 'AI & ML', 'Data Science', 'Full Stack Dev', 'Cybersecurity']
}

df = pd.DataFrame(data)

class RecommendationEngine:
    def __init__(self):
        self.model_path = 'model.pkl'
        self.vectorizer_path = 'vectorizer.pkl'
        
    def train(self):
        # Simple rule-based training for demonstration
        # In real scenario, we would use LabelEncoders and DecisionTree
        
        # Using a mapping approach for simplicity and robustness in this demo phase
        # Real ML implementation would require a larger dataset
        pass 

    def predict(self, interest, skill):
        interest = interest.lower()
        skill = skill.lower()
        
        if 'ai' in interest or 'python' in skill:
            return 'AI & ML'
        elif 'data' in interest or 'sql' in skill or 'statistics' in skill:
            return 'Data Science'
        elif 'web' in interest or 'html' in skill or 'css' in skill or 'js' in skill:
            return 'Full Stack Development'
        elif 'security' in interest or 'linux' in skill or 'network' in skill:
            return 'Cybersecurity'
        else:
            return 'General Computer Science'

    def get_recommendations(self, user_qualification, user_interest, user_skill):
        interest = user_interest.lower()
        skill = user_skill.lower()
        
        # 1. Course Recommendation
        recommended_course_title = self.predict(interest, skill)
        
        # 2. Filtering Logic based on Qualification
        # - 12th: Courses (UG), Colleges
        # - UG: Internships, Jobs (Entry), Courses (PG)
        # - PG: Jobs (Pro), Internships
        
        results = {
            'course': None,
            'colleges': [],
            'jobs': [],
            'internships': []
        }
        
        # Fetch relevant models (This logic will be handled in routes_user.py to avoid DB imports in ML)
        # We return the "Type" and "Criteria" here
        
        if user_qualification == '12th':
            results['type'] = 'academic'
            results['target_levels'] = ['UG', 'Diploma'] # Both Degree and Diploma paths
        elif user_qualification == 'UG':
            results['type'] = 'career_advancement'
            results['target_levels'] = ['PG'] # Looking for PG courses
        elif user_qualification == 'PG':
            results['type'] = 'professional'
            results['target_levels'] = [] # No more academic paths usually, focus on jobs
            
        results['suggested_course'] = recommended_course_title
        return results

    def get_job_roles(self, course_name):
        job_map = {
            'AI & ML': ['Machine Learning Engineer', 'Data Scientist', 'AI Researcher', 'NLP Engineer'],
            'Data Science': ['Data Analyst', 'Data Engineer', 'Business Intelligence Analyst', 'Statistician'],
            'Full Stack Development': ['Frontend Developer', 'Backend Developer', 'Full Stack Engineer', 'DevOps Engineer'],
            'Cybersecurity': ['Security Analyst', 'Penetration Tester', 'Security Consultant', 'Network Security Engineer'],
            'General Computer Science': ['Software Engineer', 'System Administrator', 'IT Support Specialist', 'Quality Assurance Engineer']
        }
        return job_map.get(course_name, ['Software Developer'])

recommendation_engine = RecommendationEngine()
