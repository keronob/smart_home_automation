class PhoneCallHandler:
    def __init__(self):
        self._emergency_number = "911"
        self._is_active = False
        self._current_call = None
        self._escalation_level = 0  # 0: none, 1: contacts, 2: emergency services

    def handle_emergency(self, escalation_level):
        self._escalation_level = escalation_level
        if escalation_level >= 2:
            self._call_emergency_services()

    def _call_emergency_services(self):
        self._is_active = True
        self._current_call = self._emergency_number
        # Simulate emergency call
        print(f"Emergency services contacted at {self._emergency_number}")

    def end_call(self):
        self._is_active = False
        self._current_call = None

    def get_status(self):
        return {
            "is_active": self._is_active,
            "current_call": self._current_call,
            "escalation_level": self._escalation_level
        }
