from flask import Flask, redirect, url_for
from flask_cors import CORS
from flask_migrate import Migrate
from database import db, init_db
from flask_jwt_extended import JWTManager, verify_jwt_in_request, get_jwt_identity
from flask_cors import CORS
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

def create_app():
    app = Flask(__name__,static_folder="../frontend/dist", static_url_path="/")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'placement_portal.db')
    app.config['JWT_SECRET_KEY'] = 'ajeesh_hms_secret_key'

    db.init_app(app)
    init_db(app)
    JWTManager(app)
    CORS(app)

    from routes.authentication import authentication_bp
    app.register_blueprint(authentication_bp)

    with app.app_context():
        db.create_all()

    @app.route('/')
    def home():
        try:
            # Check if JWT is present and valid
            verify_jwt_in_request(optional=True)
            identity = get_jwt_identity()
            if identity:
                role = identity['role']
                # Redirect based on role
                if role == 'admin':
                    return redirect(url_for('admin_bp.admin_dashboard'))
                elif role == 'company':
                    return redirect(url_for('company_bp.company_dashboard'))
                elif role == 'student':
                    return redirect(url_for('student_bp.student_dashboard'))
            # If no token → redirect to login
            print("No valid JWT token found, redirecting to login.")
            return redirect('/login')
        except Exception:
            print("An error occurred while processing the request.")
            return redirect('/login')

    return app



app = create_app()

for rule in app.url_map.iter_rules():
    print(rule.endpoint, rule.rule, sorted(rule.methods))

if __name__ == '__main__':
    print("Starting the Placement Portal Application...")

    # with app.app_context():
    #     print(db.metadata.tables.keys())


    app.run(debug=True)
