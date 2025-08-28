"""Configuración de la aplicación Flask."""

import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

BASE_DIR=os.path.abspath(os.path.dirname(__file__))

# Función para convertir una cadena a un valor booleano
def str_to_bool(value):
    return value.lower() in ['true', '1', 'yes']

class Config:
    """Configuración de la aplicación Flask."""
    
    # Flask server
    BASEDIR = BASE_DIR
    APP_NAME = os.getenv('APP_NAME', 'SamanBooks')
    APP_VERSION = "0.1.0"
    APP_URL = os.getenv('APP_URL', 'http://localhost:5001')
    PORT = os.environ.get("PORT")
    DEBUG = os.environ.get("DEBUG")
    LANGUAGE = os.environ.get("LANGUAGE")
    SCHEDULER_API_ENABLED = os.environ.get("SCHEDULER_API_ENABLED") or True

    # Variables de entorno para el administrador
    ADMIN_USERNAME = os.getenv('ADMIN_USERNAME', 'Admin')
    ADMIN_EMAIL = os.getenv('ADMIN_EMAIL', 'admin@escuela.com')
    ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'password-seguro')

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or f'sqlite:///{os.path.join(BASE_DIR, "samanbookslanding.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS') or False


    # Encriptado
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'una_clave_secreta_segura'
    SECURITY_PASSWORD_SALT = os.getenv('SECURITY_PASSWORD_SALT')
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    RESET_TOKEN_EXP_MINUTES = int(os.getenv('RESET_TOKEN_EXP_MINUTES', 25))
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES', 30)))
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=int(os.getenv('JWT_REFRESH_TOKEN_EXPIRES', 30)))

    # Configuración de Flask-Mail
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USE_TLS = str_to_bool(os.environ.get('MAIL_USE_TLS', 'False'))
    MAIL_USE_SSL = str_to_bool(os.environ.get('MAIL_USE_SSL', 'True'))
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = (os.environ.get('APP_NAME'), os.environ.get('MAIL_USERNAME'))
    MAIL_DEBUG = int(os.environ.get('MAIL_DEBUG', 0))