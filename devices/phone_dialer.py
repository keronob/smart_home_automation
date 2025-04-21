# devices/phone_dialer.py

class PhoneDialer:
    def __init__(self, name="Emergency Dialer", emergency_number="911"):
        self.name = name
        self._emergency_number = emergency_number
        self._is_active = False
        self._current_call = None
        self._escalation_level = 0

    def call_emergency(self):
        self._is_active = True
        self._current_call = self._emergency_number
        print(f"📞 {self.name}: Calling emergency services at {self._emergency_number}")

    def end_call(self):
        self._is_active = False
        self._current_call = None

    def get_status(self):
        return {
            "is_active": self._is_active,
            "current_call": self._current_call,
            "escalation_level": self._escalation_level
        }
