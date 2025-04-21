# handlers/phone_call_handler.py
from handlers.alert_handler import AlertHandler

class PhoneCallHandler(AlertHandler):
    def __init__(self,hub):
        super().__init__()
        self.hub = hub

    def handle(self, event: dict):
        if event.get("escalate"):
            phone_dialer = self.hub.get_device("dialer")
            if phone_dialer:
                phone_dialer.call_emergency()
        super().handle(event)