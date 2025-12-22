# 🌌 UnniMaya: AI Career Recommendation System

**UnniMaya** is a high-end, futuristic web application designed to help users navigate their career paths using AI-driven insights. Built with a cyberpunk aesthetic, it analyzes user skills and interests to recommend tailored career trajectories, courses, and colleges.

---

## ✨ Features

- **🚀 AI-Driven Recommendations**: Uses a rule-based engine (scalable to ML) to match skills and interests to career paths.
- **🔐 Secure Authentication**: Full user signup, login, and session management system.
- **🛠️ Admin Control Center**: A dedicated dashboard for administrators to manage users, courses, and colleges.
- **🌐 Protected REST API**: Secure endpoints for programmatic access to course and college data.
- **🎨 Immersive UI/UX**: Cyberpunk/Sci-Fi design with glassmorphism, neon accents, and smooth micro-animations.
- **📱 Responsive Layout**: Fully optimized for desktop, tablet, and mobile experiences.
- **💬 Feedback System**: Integrated system for users to provide feedback on recommendations.

---

## 🛠 Tech Stack

- **Backend**: [Python 3.x](https://www.python.org/), [Flask](https://flask.palletsprojects.com/)
- **Database**: [SQLAlchemy](https://www.sqlalchemy.org/) (SQLite for development)
- **Security**: [Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/), [Flask-Login](https://flask-login.readthedocs.io/)
- **Frontend**: HTML5, CSS3 (Custom Variables, Flexbox/Grid), JavaScript
- **ML/Data**: [Scikit-learn](https://scikit-learn.org/), [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/)
- **Forms**: [Flask-WTF](https://flask-wtf.readthedocs.io/)
- **Fonts**: 'Orbitron' (Headers), 'Rajdhani' (Body)

---

## 📦 Installation & Setup

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/unnimaya.git
    cd unnimaya
    ```

2.  **Environment Setup**:
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables**:
    Create a `.env` file in the root directory (refer to `.env.example`):
    ```env
    SECRET_KEY=your_secure_random_key
    DATABASE_URL=sqlite:///site.db
    API_KEY=your_api_key_for_endpoints
    FLASK_DEBUG=True
    ```

5.  **Initialize Database & Run**:
    ```bash
    python app.py
    ```
    Access the app at `http://127.0.0.1:5000`

---

## 📂 Project Structure

```text
UnniMaya/
├── app.py              # Main entry point & Blueprint registration
├── models.py           # SQLAlchemy Database models (User, Course, College, Feedback)
├── forms.py            # Flask-WTF forms for registration, login, and admin tasks
├── extensions.py       # Extension initializations (DB, Bcrypt, LoginManager)
├── ml_model.py         # AI Recommendation Engine logic
├── routes_auth.py      # Authentication routes (Login, Signup, Logout)
├── routes_user.py      # Main user facing routes & profile management
├── routes_admin.py     # Admin dashboard and content management
├── routes_api.py       # SECURE REST API endpoints
├── static/             # CSS, JS, and Images
└── templates/          # Jinja2 HTML Templates
```

---

## 🛡 Admin Dashboard

Administrators can access the management suite at `/admin/dashboard`. 
- **Manage Users**: View and manage registered users.
- **Course Management**: Add or update career-related courses.
- **College Management**: Maintain a database of colleges and their affiliates.

---

## 🔌 API Usage

The system provides a protected API. All requests require an `x-api-key` header.

- **GET `/api/courses`**: Retrieve all available courses.
- **GET `/api/colleges`**: Retrieve all registered colleges.

---

## 🧪 Testing

The project includes basic verification and test suites.

- **App Verification**: `python verify_app.py` (Checks basic route integrity)
- **Test Suite**: `python test_suite.py` (Runs automated unit/functional tests)

---

## 🎨 Design System

- **Primary**: Neon Cyan (`#00f3ff`)
- **Secondary**: Neon Purple (`#bc13fe`)
- **Background**: Deep Space Black (`#030305`)
- **Glassmorphism**: 10px Blur with semi-transparent borders.

---

## 🔮 Roadmap

- [ ] Transition from rule-based to Scikit-learn Decision Tree model.
- [ ] Implement Job Opportunity suggestions based on recommendations.
- [ ] Add real-time notifications for career events.
- [ ] Integrate with LinkedIn/Indeed APIs for live job data.

---

© 2025 UnniMaya - Towards the Future of Careers.
