from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from datetime import datetime, timedelta

from landing.controllers import ControllerFactory

metrics_bp = Blueprint("metrics", __name__, template_folder="templates")

@metrics_bp.route("/metrics")
@login_required
def metrics_dashboard():
    controller = ControllerFactory().get_controller("visits")

    # Rango por defecto: últimos 7 días
    end = datetime.utcnow()
    start = end - timedelta(days=7)

    daily_counts = controller.get_daily_counts(start, end)
    route_counts = controller.get_route_counts(start, end)

    return render_template(
        "metrics/dashboard.html",
        daily_counts=daily_counts,
        route_counts=route_counts,
        start=start.strftime("%Y-%m-%d"),
        end=end.strftime("%Y-%m-%d")
    )

@metrics_bp.route('/metrics/<path:route>')
def metrics_by_route(route):
    decoded_route = '/' + route  # reconstruye la ruta original
    controller = ControllerFactory().get_controller("visits")
    visits = controller.get_visits_for_route(decoded_route)
    daily_counts = controller.get_daily_counts_for_route(decoded_route)
    return render_template('metrics/route_dashboard.html',
                           route=decoded_route,
                           visits=visits,
                           daily_counts=daily_counts)

@metrics_bp.route("/metrics/downloads")
def downloads_metrics():
    controller = ControllerFactory().get_controller("downloads")

    # Rango por defecto: últimos 7 días
    end = datetime.utcnow()
    start = end - timedelta(days=7)

    daily_counts = controller.get_daily_download_counts(start, end)
    filename_counts = controller.get_download_counts_by_filename(start, end)

    return render_template(
        "metrics/downloads_metrics.html",
        daily_counts=daily_counts,
        filename_counts=filename_counts,
        start=start.strftime("%Y-%m-%d"),
        end=end.strftime("%Y-%m-%d")
    )
