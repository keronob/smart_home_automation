# mediator/smart_home_hub.py
from services.event_logger import EventLogger
class SmartHomeHub:
    def __init__(self):
        self._devices = {}
        self._handlers = None   # Chain of Responsibility entry point
        self.event_logger = EventLogger()

    def register_device(self, name: str, device):
        self._devices[name] = device
        print(f"📟 Device '{name}' registered.")

    def get_device(self, name: str):
        return self._devices.get(name)

    def set_handler_chain(self, handler_chain):
        self._handlers = handler_chain

    def get_event_history(self):
        return self.event_logger.get_events_history()

    def clear_event_history(self):
        self.event_logger.clear_history()
        print("🗑️ Event history cleared.")

    def notify(self, event: dict):
        print(f"📡 Hub: Received event {event}")
        self.event_logger.log_event(event)
        if self._handlers:
            self._handlers.handle(event)
        else:
            print("⚠️ No handler chain configured.")

    def get_system_status(self):
        status = {}
        for name, device in self._devices.items():
            if hasattr(device, "get_status"):
                status[name] = device.get_status()
        return status
