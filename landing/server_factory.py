from flask import Flask
from datetime import datetime

from landing.database import init_db, db
from landing.config import Config, create_initial_admin
from landing.server_extensions import init_migrate, init_login_manager, init_csrf
from landing.routes import register_blueprints

def create_app():
    app = Flask(
        __name__,
        template_folder="./templates",
        static_folder="./static",
        )
    
    app.config.from_object(Config)

    init_db(app)
    init_migrate(app, db)
    init_login_manager(app)
    init_csrf(app)
    register_blueprints(app)

    with app.app_context():
        db.create_all()
        create_initial_admin()
    
    @app.context_processor
    def inject_app_name():
        return {
            "app_name": app.config["APP_NAME"],
            "app_version": app.config["APP_VERSION"],
            "server_language": app.config["LANGUAGE"],
            "now": datetime.now() 
            }

    return app