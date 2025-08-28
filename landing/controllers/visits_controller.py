from datetime import datetime, timedelta
from typing import List, Optional
from flask import current_app
from sqlalchemy import func

from landing.database.models import Visits
from landing.controllers.database_controller import DatabaseController
from landing.schemas import VisitsCreate, VisitsResponse

class VisitsController(DatabaseController):
    def __init__(self, db):
        super().__init__(db)

    def register_visit(self, data: VisitsCreate) -> VisitsResponse:
        """Registra una visita con la ruta actual y timestamp."""
        visit = Visits(route=data.route, date=data.date)
        self.session.add(visit)
        self._commit_or_rollback()
        return self._to_response(visit, VisitsResponse)

    def get_visits_by_day(self, day: datetime) -> List[VisitsResponse]:
        """Obtiene visitas de un día específico."""
        start = datetime(day.year, day.month, day.day)
        end = start + timedelta(days=1)
        visits = Visits.query.filter(Visits.date >= start, Visits.date < end).all()
        return self._bulk_to_response(visits, VisitsResponse)

    def get_visits_by_range(self, start: datetime, end: datetime) -> List[VisitsResponse]:
        """Obtiene visitas entre dos fechas."""
        visits = Visits.query.filter(Visits.date >= start, Visits.date <= end).all()
        return self._bulk_to_response(visits, VisitsResponse)

    def get_daily_counts(self, start: datetime, end: datetime) -> List[dict]:
        """Devuelve conteo de visitas por día en un rango."""
        results = (
            self.session.query(
                func.date(Visits.date).label("day"),
                func.count().label("count")
            )
            .filter(Visits.date >= start, Visits.date <= end)
            .group_by(func.date(Visits.date))
            .order_by(func.date(Visits.date))
            .all()
        )
        return [{"day": r.day, "count": r.count} for r in results]

    def get_route_counts(self, start: datetime, end: datetime) -> List[dict]:
        """Devuelve conteo de visitas por ruta en un rango."""
        results = (
            self.session.query(
                Visits.route,
                func.count().label("count")
            )
            .filter(Visits.date >= start, Visits.date <= end)
            .group_by(Visits.route)
            .order_by(func.count().desc())
            .all()
        )
        return [{"route": r.route, "count": r.count} for r in results]

    def get_visits_for_route(self, route: str):
        """Obtiene las últimas 100 visitas para una ruta específica."""
        return Visits.query.filter_by(route=route).order_by(Visits.date.desc()).limit(100).all()

    def get_daily_counts_for_route(self, route: str):
        """Devuelve conteo diario de visitas para una ruta específica."""
        results = self.session.query(
            func.date(Visits.date).label('day'),
            func.count().label('count')
        ).filter_by(route=route).group_by(func.date(Visits.date)).order_by('day').all()

        return [{"day": r.day, "count": r.count} for r in results]
