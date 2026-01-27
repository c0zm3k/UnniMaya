# 🌌 FutureFit - AI Career Architect

> **A high-scale, Neumorphic AI Recommendation System for 12th, UG, and PG students.**

**FutureFit** is a premium career guidance platform that uses sophisticated mapping to align students with their ideal futures. Whether you are finishing school, completing a degree, or specializing further, FutureFit provides a tailored roadmap including courses, colleges, professional jobs, and strategic internships.

---

## 📸 Core Aesthetic

FutureFit utilizes a bespoke **Neumorphic (Soft UI)** design system, creating a tactile and immersive digital experience.

| Landing Page | Mobile Navigation |
| --- | --- |
| ![Landing Page](file:///C:/Users/LENOVO/.gemini/antigravity/brain/8e19e96a-bac2-4052-b23a-fb209505860c/uploaded_media_1769502549678.png) | ![Mobile Menu](file:///C:/Users/LENOVO/.gemini/antigravity/brain/8e19e96a-bac2-4052-b23a-fb209505860c/uploaded_media_1769501740936.png) |

---

## ✨ New & Advanced Features

### 🎓 Qualification-Aware Recommendations
The engine now adapts to your current educational standing:
*   **12th/School Passed:** Suggests **Undergraduate degrees** and **Diploma** courses alongside top colleges.
*   **UG Completed:** Focuses on **Postgraduate specialization**, **Internships**, and **Entry-level jobs**.
*   **PG Completed:** Recommends **Professional careers** and **Advanced research internships**.

### 💼 Career Expansion Module
*   **Massive Dataset:** Re-seeded with over **11,500 total records** including 25 colleges and 5,600+ career openings.
*   **Work Modes:** Every Job and Internship now displays its operational status: **Onsite**, **Hybrid**, or **WFH (Work From Home)**.
*   **Diploma Support:** Added specialized diploma paths for immediate skill acquisition.

### 📱 Mobile-First Responsive Design
*   **Hamburger Navigation:** Smart collapsible menu for seamless mobile browsing.
*   **Touch-Optimized:** All interactive elements are designed for finger-friendly tapping.
*   **Fluid Breakpoints:** Adapts perfectly across phones, tablets, and desktops.

---

## 🛠️ Tech Stack

*   **Logic:** Python 3.10+, Flask
*   **Database:** SQLAlchemy (ORM) with a high-volume SQLite backend
*   **Style:** Custom **Neumorphic CSS Framework** + Tailwind CSS
*   **Auth:** Flask-Login with Bcrypt Hashing

---

## 🚀 Getting Started

### Installation
1. **Clone & Enter**
   ```bash
   git clone https://github.com/nihadniaze/FutureFit.git
   cd FutureFit
   ```
2. **Environment Setup**
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate  # Windows
   pip install -r requirements.txt
   ```
3. **Database Reset (Optional)**
   ```bash
   python scripts/reset_db.py  # Severs all tables and populates 11,000+ records
   ```
4. **Launch**
   ```bash
   python app.py
   ```

---

## 🔐 Credentials & Test Accounts

We have pre-configured 7 accounts for immediate testing.
**Common Password for all students:** `password123`

| Level | Role/Username | Email | Focus Area |
| :--- | :--- | :--- | :--- |
| **Admin** | `admin` | `admin@futurefit.ai` | System Management (`admin123`) |
| **12th** | `sam_12th` | `sam@futurefit.ai` | AI & Technology |
| **12th** | `jane_12th` | `jane@futurefit.ai` | UI/UX & Creative |
| **UG** | `alex_ug` | `alex@futurefit.ai` | Data Science & Backend |
| **UG** | `lily_ug` | `lily@futurefit.ai` | Full Stack & Design |
| **PG** | `mark_pg` | `mark@futurefit.ai` | AI Research & Ethics |
| **PG** | `sara_pg` | `sara@futurefit.ai` | Cloud & Security |

---

## 📂 Project Structure

```text
FutureFit/
├── src/                  # Core application modules
│   ├── models.py         # Database schemas
│   ├── forms.py          # WTForms definitions
│   ├── extensions.py     # Flask extensions (DB, Bcrypt, LoginManager)
│   ├── ml_model.py       # AI recommendation engine
│   ├── routes_auth.py    # Authentication routes
│   ├── routes_user.py    # User dashboard & recommendations
│   ├── routes_admin.py   # Admin panel routes
│   └── routes_api.py     # REST API endpoints
├── static/               # Frontend assets
│   ├── css/              # Neumorphic stylesheets
│   └── js/               # JavaScript files
├── templates/            # Jinja2 HTML templates
├── scripts/              # Utility scripts
│   ├── reset_db.py       # Database seeding
│   └── check_counts.py   # Data verification
├── tests/                # Test suites
├── app.py                # Application entry point
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

© 2026 FutureFit - Architecting the Future of Workforce.
