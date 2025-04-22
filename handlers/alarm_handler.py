# handlers/alarm_handler.py

from handlers.alert_handler import AlertHandler

class AlarmHandler(AlertHandler):
    def __init__(self, hub):
        super().__init__()
        self.hub = hub

    def handle(self, event: dict):
        alarm = self.hub.get_device("alarm")
        if not alarm:
            return

        if event.get("type") in ["motion", "smoke", "intrusion"]:
            if not alarm.get_status()["is_armed"]:
                alarm.arm()
                print("⚠️ Alarm armed due to suspicious activity.")
                self.hub.event_logger.log_action(
                    device_name="alarm",
                    action="Alarm Auto Armed",
                    details={
                        "event_type": event.get("type"),
                        "location": event.get("location", "Kitchen"),
                    }
                )

            alarm.trigger()
            self.hub.event_logger.log_action(
                device_name="alarm",
                action="Alarm Triggered",
                details={
                    "event_type": event.get("type"),
                    "location": event.get("location", "Kitchen"),
                }
            )

        super().handle(event)
