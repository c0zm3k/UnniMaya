from ml_model import recommendation_engine

def test_job_roles():
    courses = ['AI & ML', 'Data Science', 'Full Stack Development', 'Cybersecurity', 'Unknown']
    for course in courses:
        jobs = recommendation_engine.get_job_roles(course)
        print(f"Course: {course}, Jobs: {jobs}")

if __name__ == "__main__":
    test_job_roles()
