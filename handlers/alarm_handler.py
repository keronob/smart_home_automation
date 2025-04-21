# handlers / alarm_handler.py

from handlers.alert_handler import AlertHandler

class AlarmHandler(AlertHandler):
    def __init__(self, hub):
        super().__init__()
        self.hub = hub

    def handle(self, event: dict):
        if event.get("type") == "intrusion":
            alarm = self.hub.get_device("alarm")
            if alarm:
                alarm.trigger()
        elif event.get("alarm_off"):
            alarm = self.hub.get_device("alarm")
            if alarm:
                alarm.turn_off()
        super().handle(event)