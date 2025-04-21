# This file is part of the Smart Home Automation project.

class MotionSensor:
    def __init__(self, hub):
        self.hub = hub
        self._is_active = False

    def activate(self):
        self._is_active = True

    def deactivate(self):
        self._is_active = False

    def motion_detected(self):
        if not self._is_active:
            return

        print("🏃 Motion detected!")
        self.hub.notify({
            "type": "motion",
            "location": "Living Room"
        })

    def get_status(self):
        return {
            "is_active": self._is_active
        }
