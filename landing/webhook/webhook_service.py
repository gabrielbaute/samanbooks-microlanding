import requests
import datetime
import logging

from landing.schemas import WebhookPayload
from landing.config import Config

class WebhookService:
    def __init__(self):
        self.app_name = Config.APP_NAME
        self.app_version = Config.APP_VERSION
        self.webhook_url = Config.WEBHOOK_URL
        self.service_name = 'WebhookService'
        self.logger = logging.getLogger(f'[{self.service_name}]')

    def emit(self, payload: WebhookPayload):
        enriched_payload = {
            "event": payload.event,
            "data": payload.data,
            "meta": {
                "app_name": self.app_name,
                "app_version": self.app_version,
                "timestamp": datetime.datetime.utcnow().isoformat()
            }
        }
        try:
            response = requests.post(self.webhook_url, json=enriched_payload)
            response.raise_for_status()
            self.logger.debug(f"Webhook enviado: {response.status_code}")
        except requests.RequestException as e:
            self.logger.error(f"Error al enviar webhook: {e}")
