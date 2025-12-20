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
        # Simple keyword matching logic that mimics the "Decision Tree" logic
        # Ideally, we load the pickled model here.
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
