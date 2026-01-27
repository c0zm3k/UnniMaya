import sys
sys.path.insert(0, '..')
from app import app
from src.extensions import db, bcrypt
from src.models import User, Course, Job, Internship, College
import random

def reset_database():
    with app.app_context():
        print("Clearing database...")
        db.drop_all()
        print("Recreating tables...")
        db.create_all()
        
        print("Creating admin user...")
        hashed_password = bcrypt.generate_password_hash('admin123').decode('utf-8')
        admin_user = User(
            username='admin',
            email='admin@futurefit.ai',
            password=hashed_password,
            role='admin',
            qualification='PG'
        )
        db.session.add(admin_user)

        # Generating Dummy Students
        pass_word = bcrypt.generate_password_hash('password123').decode('utf-8')
        
        students_data = [
            # 12th Passed
            {'username': 'sam_12th', 'email': 'sam@futurefit.ai', 'qual': '12th', 'skills': 'Math, Logic', 'interests': 'AI, Technology'},
            {'username': 'jane_12th', 'email': 'jane@futurefit.ai', 'qual': '12th', 'skills': 'Drawing, Creative Thinking', 'interests': 'UI/UX, Animation'},
            
            # UG Completed
            {'username': 'alex_ug', 'email': 'alex@futurefit.ai', 'qual': 'UG', 'skills': 'Python, SQL', 'interests': 'Data Science, Backend'},
            {'username': 'lily_ug', 'email': 'lily@futurefit.ai', 'qual': 'UG', 'skills': 'React, CSS', 'interests': 'Web Development, Design'},
            
            # PG Completed
            {'username': 'mark_pg', 'email': 'mark@futurefit.ai', 'qual': 'PG', 'skills': 'PyTorch, NLP', 'interests': 'Research, AI Ethics'},
            {'username': 'sara_pg', 'email': 'sara@futurefit.ai', 'qual': 'PG', 'skills': 'Kubernetes, Cloud', 'interests': 'Cybersecurity, Infrastructure'},
        ]

        for s in students_data:
            student = User(
                username=s['username'],
                email=s['email'],
                password=pass_word,
                role='user',
                qualification=s['qual'],
                skills=s['skills'],
                interests=s['interests']
            )
            db.session.add(student)

        # Lists for random generation
        locations = ['California', 'New York', 'London', 'Berlin', 'Tokyo', 'Singapore', 'Mumbai', 'Bangalore', 'Sydney', 'Toronto']
        college_prefixes = ['Elite', 'Global', 'Future', 'Tech', 'Imperial', 'Heritage', 'Universal', 'Modern', 'Pioneer', 'Horizon']
        college_types = ['Institute', 'University', 'Academy', 'College', 'Polytechnic']
        
        course_titles = {
            'UG': ['Computer Science', 'Data Analytics', 'Web Development', 'Digital Marketing', 'Business Management', 'Mechanical Engineering', 'Cloud Computing', 'UI/UX Design'],
            'PG': ['Artificial Intelligence', 'Cybersecurity', 'Financial Technology', 'Strategic Management', 'Quantum Computing', 'Big Data Engineering'],
            'Diploma': ['Full Stack Coding', 'Graphic Designing', 'Network Administration', 'Animation', 'SEO Specialist', 'Mobile Development']
        }

        job_roles_pool = ['Software Engineer', 'Data Analyst', 'Product Manager', 'UX Designer', 'Security Specialist', 'Cloud Architect', 'Marketing Lead', 'DevOps Engineer']
        company_names = ['TechNova', 'InnoSoft', 'AlphaStream', 'CloudBase', 'LogicX', 'DataCorp', 'NetSpeed', 'BluePrint']
        work_modes = ['Onsite', 'Hybrid', 'WFH']

        all_colleges = []
        all_courses = []
        all_jobs = []
        all_internships = []

        print("Generating 25 Colleges and their ecosystems...")
        for i in range(25):
            c_name = f"{random.choice(college_prefixes)} {random.choice(college_types)} {i+1}"
            c_loc = random.choice(locations)
            
            selected_courses_for_college = []
            for _ in range(random.randint(20, 25)):
                level = random.choice(['Diploma', 'UG', 'PG'])
                title = random.choice(course_titles[level])
                full_title = f"{title} ({level})"
                
                course = Course(
                    title=full_title,
                    description=f"A specialized {level} program in {title} at {c_name}.",
                    skills_required=f"Skill-{random.randint(1,10)}, Skill-{random.randint(11,20)}",
                    level=level
                )
                all_courses.append(course)
                selected_courses_for_college.append(full_title)
                
                # Add 10 Jobs for this course
                for _ in range(10):
                    job = Job(
                        title=f"{random.choice(job_roles_pool)} - {title}",
                        company=random.choice(company_names),
                        description=f"Exciting career opportunity in {title} at {random.choice(company_names)}.",
                        skills_required="Technical Skills, Problem Solving",
                        qualification_required=level,
                        work_mode=random.choice(work_modes)
                    )
                    all_jobs.append(job)

                # Add 10 Internships for this course
                for _ in range(10):
                    intern = Internship(
                        title=f"{random.choice(job_roles_pool)} Intern ({title})",
                        company=random.choice(company_names),
                        description=f"Hands-on experience in {title} with {random.choice(company_names)}.",
                        skills_required="Fast Learner, Basic Tech Knowledge",
                        duration=f"{random.randint(3, 6)} Months",
                        qualification_required=level,
                        work_mode=random.choice(work_modes)
                    )
                    all_internships.append(intern)

            college = College(
                name=c_name,
                location=c_loc,
                affiliates=", ".join(list(set(selected_courses_for_college))),
                cutoff_score=random.randint(70, 95),
                fees=random.randint(10000, 80000)
            )
            all_colleges.append(college)

        print(f"Stats: {len(all_colleges)} Colleges, {len(all_courses)} Courses, {len(all_jobs)} Jobs, {len(all_internships)} Internships.")
        print("Saving to database (this may take a moment)...")
        
        db.session.add_all(all_colleges)
        db.session.add_all(all_courses)
        db.session.add_all(all_jobs)
        db.session.add_all(all_internships)
        
        db.session.commit()
        print("Database populated successfully!")

if __name__ == '__main__':
    reset_database()
