# AI Career Recommendation System

A futuristic, AI-powered web application that analyzes user skills and interests to recommend optimal career trajectories. Built with Python Flask and designed with a high-end Cyberpunk/Sci-Fi aesthetic.

## 🚀 Features

- **Futuristic UI/UX**: Immersive dark mode, neon accents, and glassmorphism effects.
- **Dynamic Analysis**: Input your skills and interests to get career matches (Mock Logic).
- **Responsive Design**: Works on desktop and mobile.
- **Interactive Elements**: Hover effects, smooth transitions, and "system" animations.

## 🛠 Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3 (Custom Variables, Flexbox/Grid), JavaScript
- **Fonts**: Orbitron (Headers), Rajdhani (Body)

## 📦 Installation & Setup

1.  **Clone/Open the project** in your terminal.
2.  **Create a virtual environment** (recommended):
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```
3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the application**:
    ```bash
    python app.py
    ```
5.  **Access the App**:
    Open your browser and navigate to `http://127.0.0.1:5000`

## 📂 Project Structure

```text
/
├── app.py              # Main Flask application entry point
├── requirements.txt    # Python dependencies
├── static/             # Static assets
│   ├── css/
│   │   └── style.css   # Main stylesheet (Futuristic design)
│   ├── js/
│   │   └── main.js     # Frontend interaction logic
│   └── images/         # (Optional) Image assets
└── templates/          # HTML Templates
    ├── layout.html     # Base template with common head/nav
    ├── index.html      # Input form page
    └── results.html    # Career recommendation display
```

## 🎨 Design System

- **Primary Color**: Neon Cyan (`#00f3ff`)
- **Secondary Color**: Neon Purple (`#bc13fe`)
- **Background**: Deep Space Black (`#030305`)
- **Typography**: 'Orbitron' for high-tech headings, 'Rajdhani' for readable tech-styled body text.

## 🔮 Future Roadmap

- Integrate real Machine Learning model (e.g., TensorFlow/Scikit-Learn).
- Add user authentication and profile saving.
- Connect to job market APIs (LinkedIn, Indeed) for real-time data.
