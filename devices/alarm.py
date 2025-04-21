"""
Alarm device module for smart home security system.
Manages security state and integrates with motion sensors for automated responses.
"""


class Alarm:
    def __init__(self):
        self._is_armed = False
        self._is_triggered = False
        self._sensitivity = 50  # Default sensitivity level

    def arm(self):
        """Arm the alarm system."""
        self._is_armed = True
        self._is_triggered = False

    def disarm(self):
        """Disarm the alarm system."""
        self._is_armed = False
        self._is_triggered = False

    def trigger(self):
        """Trigger the alarm if armed."""
        if self._is_armed:
            self._is_triggered = True

    def set_sensitivity(self, level):
        """Set the alarm sensitivity level."""
        if not 0 <= level <= 100:
            raise ValueError("Sensitivity must be between 0 and 100")
        self._sensitivity = level

    def get_status(self):
        """Get the current status of the alarm."""
        return {
            "is_armed": self._is_armed,
            "is_triggered": self._is_triggered,
            "sensitivity": self._sensitivity
        }
