from datetime import datetime
from flask import Blueprint, request, render_template, flash, send_from_directory, url_for, redirect

from landing.controllers import ControllerFactory
from landing.schemas import VisitsCreate, DownloadsCreate

main_bp = Blueprint("main", __name__, template_folder="templates")

@main_bp.before_app_request
def track_main_visits():
    if request.blueprint == "main" and request.endpoint not in ("static",):
        controller = ControllerFactory().get_controller("visits")
        controller.register_visit(
            VisitsCreate(
                route=request.path,
                date=datetime.utcnow()
            )
        )

@main_bp.route("/")
def home():
    return redirect(url_for("main.index"))

@main_bp.route("/index")
def index():
    return render_template("index.html")

@main_bp.route("/planes")
def planes():
    return render_template("planes.html")

@main_bp.route("/sobre-fallas")
def fallas():
    return render_template("fallas.html")

@main_bp.route("/download-apk")
def download_apk():
    flash(f"Descargando APK 👋", "success")

    controller = ControllerFactory().get_controller("downloads")
    controller.register_download(
        DownloadsCreate(
            filename="SamanBooks-v0.1.0.apk",
            date=datetime.utcnow()
        )
    )

    return send_from_directory(
        directory="static/uploads",
        path="SamanBooks-v0.1.0.apk",
        as_attachment=True
    )