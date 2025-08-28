from landing.database import db
from landing.controllers.user_controller import UsersController
from landing.controllers.visits_controller import VisitsController
from landing.controllers.downloads_controller import DownloadsController

class ControllerFactory:
    """Controller Factory"""

    def __init__(self, db_instance=db, current_user=None):
        if not hasattr(db_instance, "session"):
            raise ValueError("El objeto db no parece ser una instancia válida de SQLAlchemy")
        
        self.db = db_instance
        self.current_user = current_user
    
    def get_controller(self, controller_name):
        if controller_name == "users":
            return UsersController(self.db, self.current_user)
        if controller_name == "visits":
            return VisitsController(self.db)
        if controller_name == "downloads":
            return DownloadsController(self.db) 
        return None