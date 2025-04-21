class SmartLight:
    def __init__(self):
        self._is_on = False
        self._brightness = 0

    def turn_on(self):
        self._is_on = True

    def turn_off(self):
        self._is_on = False
        self._brightness = 0

    def set_brightness(self, level):
        if not 0 <= level <= 100:
            raise ValueError("Brightness must be between 0 and 100")
        self._brightness = level
        if level > 0:
            self._is_on = True
        else:
            self._is_on = False

    def get_status(self):
        return {
            "is_on": self._is_on,
            "brightness": self._brightness
        }
