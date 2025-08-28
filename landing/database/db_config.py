import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    db_path = os.path.join(os.getcwd(), 'instance')
    if not os.path.exists(db_path):
        os.makedirs(db_path)
    elif not os.access(db_path, os.W_OK):
        raise PermissionError(f"No se puede escribir en {db_path}")
    db.init_app(app)