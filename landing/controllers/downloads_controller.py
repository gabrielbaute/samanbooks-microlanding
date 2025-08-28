from datetime import datetime, timedelta
from typing import List, Optional
from flask import current_app
from sqlalchemy import func

from landing.database.models import Downloads
from landing.controllers.database_controller import DatabaseController
from landing.schemas import DownloadsCreate, DownloadsResponse

class DownloadsController(DatabaseController):
    def __init__(self, db):
        super().__init__(db)

    def register_download(self, data: DownloadsCreate) -> DownloadsResponse:
        """Registra una descarga con el nombre del archivo y timestamp."""
        download = Downloads(filename=data.filename, date=data.date)
        self.session.add(download)
        self._commit_or_rollback()
        return self._to_response(download, DownloadsResponse)

    def get_downloads_by_day(self, day: datetime) -> List[DownloadsResponse]:
        """Obtiene descargas de un día específico."""
        start = datetime(day.year, day.month, day.day)
        end = start + timedelta(days=1)
        downloads = Downloads.query.filter(Downloads.date >= start, Downloads.date < end).all()
        return self._bulk_to_response(downloads, DownloadsResponse)

    def get_downloads_by_range(self, start: datetime, end: datetime) -> List[DownloadsResponse]:
        """Obtiene descargas entre dos fechas."""
        downloads = Downloads.query.filter(Downloads.date >= start, Downloads.date <= end).all()
        return self._bulk_to_response(downloads, DownloadsResponse)

    def get_daily_download_counts(self, start: datetime, end: datetime) -> List[dict]:
        """Devuelve conteo de descargas por día en un rango."""
        results = (
            self.session.query(
                func.date(Downloads.date).label("day"),
                func.count().label("downloads_counts")
            )
            .filter(Downloads.date >= start, Downloads.date <= end)
            .group_by(func.date(Downloads.date))
            .order_by(func.date(Downloads.date))
            .all()
        )
        return [{"day": r.day, "downloads_counts": r.downloads_counts} for r in results]

    def get_download_counts_by_filename(self, start: datetime, end: datetime) -> List[dict]:
        results = (
            self.session.query(
                Downloads.filename,
                func.count().label("count")
            )
            .filter(Downloads.date >= start, Downloads.date <= end)
            .group_by(Downloads.filename)
            .order_by(func.count().desc())
            .all()
        )
        return [{"filename": r.filename, "count": r.count} for r in results]
