"""
Alarm device module for smart home security system.
Manages security state and integrates with motion sensors for automated responses.
"""


class Alarm:
    def __init__(self, name: str):
        self.name = name
        self._is_armed = False
        self._is_triggered = False
        self._sensitivity = 50  # Default sensitivity level (0–100)

    def arm(self):
        self._is_armed = True
        self._is_triggered = False
        print(f"🔒 {self.name} is now ARMED.")

    def disarm(self):
        self._is_armed = False
        self._is_triggered = False
        print(f"🔓 {self.name} is now DISARMED.")

    def trigger(self):
        if self._is_armed:
            self._is_triggered = True
            print(f"🚨 {self.name} has been TRIGGERED!")

    def set_sensitivity(self, level: int):
        if not 0 <= level <= 100:
            raise ValueError("Sensitivity must be between 0 and 100")
        self._sensitivity = level
        print(f"🎚️ {self.name} sensitivity set to {self._sensitivity}.")

    def get_status(self):
        return {
            "is_armed": self._is_armed,
            "is_triggered": self._is_triggered,
            "sensitivity": self._sensitivity
        }