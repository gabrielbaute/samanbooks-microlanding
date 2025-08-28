from typing import Optional
from flask import current_app

from landing.controllers import ControllerFactory
from landing.config.config import Config
from landing.schemas import UserCreate

def create_initial_admin() -> Optional[bool]:
    """Creates initial admin for app"""
    admin_username = Config.ADMIN_USERNAME
    admin_email = Config.ADMIN_EMAIL
    admin_password = Config.ADMIN_PASSWORD

    try:
        if not all([admin_username, admin_email, admin_password]):
            current_app.logger.warning("Credenciales de admin no configuradas en las variables de entorno")
            return False
        
        # Crear controller sin usuario actual (es el primer admin del sistema)
        controller = ControllerFactory(current_user=None).get_controller("users")
        
        new_admin = UserCreate(
            username=admin_username,
            email=admin_email,
            password=admin_password
        )
        admin = controller.create_user(new_admin)
        
        if not admin:
            current_app.logger.warning("No se pudo crear el usuario admin por motivos desconocidos")
            return False

        current_app.logger.info("Usuario admin creado exitosamente")
        return True
    
    except Exception as e:
        current_app.logger.error(f"Error al crear usuario admin: {e}")
        return False