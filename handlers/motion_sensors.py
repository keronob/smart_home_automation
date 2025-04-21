from devices.smart_light import SmartLight
from devices.alarm import Alarm


class MotionSensor:
    def __init__(self):
        self._light = SmartLight()
        self._alarm = Alarm()
        self._is_active = False

    def activate(self):
        self._is_active = True

    def deactivate(self):
        self._is_active = False

    def motion_detected(self):
        if not self._is_active:
            return

        self._light.turn_on()
        self._light.set_brightness(100)
        self._alarm.trigger()

    def get_status(self):
        return {
            "is_active": self._is_active,
            "light_status": self._light.get_status(),
            "alarm_status": self._alarm.get_status() if hasattr(self._alarm, 'get_status') else None
        }
