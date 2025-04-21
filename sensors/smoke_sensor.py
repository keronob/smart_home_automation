# sensors/smoke_sensor.py

from datetime import datetime

class SmokeSensor:
    def __init__(self, hub, location="Kitchen"):
        self.hub = hub
        self._is_active = False
        self.location = location

    def activate(self):
        self._is_active = True

    def deactivate(self):
        self._is_active = False

    def detect_smoke(self):
        if not self._is_active:
            return

        print(f"🔥 Smoke detected in {self.location}!")
        event = {
            "type": "smoke",
            "location": self.location,
            "escalate": True,
            "timestamp": datetime.now().isoformat()
        }
        self.hub.notify(event)

    def get_status(self):
        return {
            "is_active": self._is_active,
            "location": self.location
        }
