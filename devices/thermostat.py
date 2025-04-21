class Thermostat:
    def __init__(self):
        self._is_on = False
        self._current_temp = 20
        self._target_temp = 20
        self._mode = "off"  # "heat", "cool", "off"

    def turn_on(self):
        self._is_on = True

    def turn_off(self):
        self._is_on = False
        self._mode = "off"

    def set_temperature(self, temperature):
        if not 10 <= temperature <= 30:
            raise ValueError("Temperature must be between 10 and 30")
        self._target_temp = temperature

    def set_mode(self, mode):
        if mode not in ["heat", "cool", "off"]:
            raise ValueError("Mode must be 'heat', 'cool', or 'off'")
        self._mode = mode
        if mode == "off":
            self._is_on = False
        else:
            self._is_on = True

    def get_status(self):
        return {
            "is_on": self._is_on,
            "current_temperature": self._current_temp,
            "target_temperature": self._target_temp,
            "mode": self._mode
        }
