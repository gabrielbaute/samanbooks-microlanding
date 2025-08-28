from flask_wtf import CSRFProtect
from flask_login import LoginManager
from flask_migrate import Migrate

from landing.database import db
from landing.database.models import Users

migrate = Migrate()
login_manager = LoginManager()
csrf = CSRFProtect()

def init_login_manager(app):
    """Función que inicializa la extensión LoginManager."""
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Por favor, inicie sesión para acceder a esta página.'
    login_manager.login_message_category = 'info'

    @login_manager.user_loader
    def load_user(user_id):
        """Función que carga un usuario por su ID."""
        return db.session.get(Users, int(user_id))

    return login_manager

def init_migrate(app, db):
    """Función que inicializa la extensión Migrate."""
    migrate.init_app(app, db)

def init_csrf(app):
    """Función que inicializa la extensión CSRFProtect."""
    app.config['WTF_CSRF_ENABLED'] = True
    csrf.init_app(app)