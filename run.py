from flask import Flask
from app.routes.main import main_bp
from app.routes.auth import auth_bp
from app.routes.owner import owner_bp
from app.routes.recommendations import recommendations_bp

app = Flask(__name__, template_folder='templates')  # Only create app once
app.secret_key = 'your_secret_key_here'  # Set secret key for sessions

# Register Blueprints
app.register_blueprint(main_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(owner_bp)
app.register_blueprint(recommendations_bp)

if __name__ == '__main__':
    app.run(debug=True)