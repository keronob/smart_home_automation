# mediator/smart_home_hub.py

class SmartHomeHub:
    def __init__(self):
        self._devices = {}
        self._handlers = None   # Chain of Responsibility entry point

    def register_device(self, name: str, device):
        self._devices[name] = device
        print(f"📟 Device '{name}' registered.")

    def get_device(self, name: str):
        return self._devices.get(name)

    def set_handler_chain(self, handler_chain):
        self._handlers = handler_chain

    def notify(self, event: dict):
        print(f"📡 Hub: Received event {event}")
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
