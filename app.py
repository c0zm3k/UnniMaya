from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os

app = Flask(__name__)
# Security: Use Environment Variables
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default-dev-key-change-in-prod') 
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///site.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from flask_bcrypt import Bcrypt
from extensions import db, bcrypt, login_manager

db.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)

from routes_auth import auth
from routes_user import main
from routes_admin import admin_bp
from routes_api import api_bp

app.register_blueprint(auth)
app.register_blueprint(main)
app.register_blueprint(admin_bp)
app.register_blueprint(api_bp)

# Create DB
with app.app_context():
    from models import User, Course, College # Import models to ensure they are registered
    db.create_all()
    # Create Admin if not exists (handled in register but good to have a seeder)
    if 'User' in globals():
        pass 


# Routes are handled by Blueprints
if __name__ == '__main__':
    # Context Processor to inject current year
    @app.context_processor
    def inject_year():
        from datetime import datetime
        return {'year': datetime.utcnow().year}

    debug_mode = os.environ.get('FLASK_DEBUG', 'True') == 'True'
    port = int(os.environ.get('PORT', 3000))
    app.run(debug=debug_mode, port=port)
