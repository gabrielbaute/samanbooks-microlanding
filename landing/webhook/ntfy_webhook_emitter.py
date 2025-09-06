import requests
import logging
from typing import Optional, Dict

from landing.schemas import WebhookPayload
from landing.config import Config

class NtfyWebhookService:
    def __init__(self, topic: str):
        self.topic = topic
        self.webhook_url = f"https://ntfy.sh/{topic}"
        self.app_name = Config.APP_NAME
        self.app_version = Config.APP_VERSION
        self.service_name = 'NtfyWebhookService'
        self.logger = logging.getLogger(f'[{self.service_name}]')

    def _format_message(self, payload: WebhookPayload) -> str:
        """Formatear el mensaje para NTFY."""
        return f"[{payload.event}] {self.app_name} v{self.app_version} → {payload.description}"

    def _format_headers(self, payload: WebhookPayload) -> Dict[str, str]:
        """Formatear los encabezados para NTFY."""
        return {
            "Title": payload.title or f"{self.app_name} - {payload.event}",
            "Priority": payload.priority.value,
            "Tags": payload.tags,
            "Click": payload.url,
            "Topic": self.topic
        }

    def emit(self, payload: WebhookPayload) -> Optional[int]:
        """Emitir una notificación NTFY con el payload dado."""
        message = self._format_message(payload)
        headers = self._format_headers(payload)
        try:
            response = requests.post(self.webhook_url, data=message.encode("utf-8"), headers=headers)
            response.raise_for_status()
            self.logger.debug(f"Notificación NTFY enviada: {response.status_code}")
            return response.status_code
        except requests.RequestException as e:
            self.logger.error(f"Error al enviar notificación NTFY: {e}")
            return None
