from datetime import datetime
from typing import Dict

from landing.database.db_config import db

class Visits(db.Model):
    __tablename__ = 'visitas'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow) # Hora en que se registró
    route = db.Column(db.String(255)) # Ruta a la que se registró
    
    def __repr__(self) -> str:
        return f"Visita {self.id} en ruta {self.route} el {self.date}"
    
    def to_dict(self) -> Dict[str, any]:
        return {
            'id': self.id,
            'day': self.date.strftime('%Y-%m-%d'),
            'route': self.route,
        }