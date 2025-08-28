from datetime import datetime
from typing import Dict

from landing.database.db_config import db

class Downloads(db.Model):
    __tablename__ = 'downloads'
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    filename = db.Column(db.String(255), nullable=False)

    def __repr__(self) -> str:
        return f'<Download {self.filename}>'
    
    def to_dict(self) -> Dict:
        return {
            'id': self.id,
            'date': self.date,
            'filename': self.filename,
        }