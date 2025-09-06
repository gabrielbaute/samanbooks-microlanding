from datetime import datetime
from flask import Blueprint, request, render_template, flash, send_from_directory, url_for, redirect

from landing.controllers import ControllerFactory
from landing.webhook import NtfyWebhookService
from landing.enums import WebhookPriority
from landing.schemas import VisitsCreate, DownloadsCreate, WebhookPayload

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
    # Instancias
    webhook = NtfyWebhookService()
    controller = ControllerFactory().get_controller("downloads")
    download_data = DownloadsCreate(
            filename="SamanBooks-v0.1.0.apk",
            date=datetime.utcnow()
        )
    webhook_payload = WebhookPayload(
        event='Download',
        priority=WebhookPriority.default,
        description='Se ha generado una descarga',
        tags='Download',
        click=url_for('main.download_apk', _external=True),
        title='Descarga de APK',
        url=url_for('main.download_apk', _external=True),
        data=download_data.to_dict()
    )
    
    # Registrar y emitir
    controller.register_download(download_data)
    webhook.emit(webhook_payload)
    
    # Enviar apk
    return send_from_directory(
        directory="static/uploads",
        path="SamanBooks-v0.1.0.apk",
        as_attachment=True
    )