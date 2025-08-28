from landing.routes.main_routes import main_bp
from landing.routes.auth_routes import auth_bp
from landing.routes.metrics_routes import metrics_bp

def register_blueprints(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(metrics_bp)