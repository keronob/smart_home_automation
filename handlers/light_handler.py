from handlers.alert_handler import AlertHandler

class LightHandler(AlertHandler):
    def __init__(self, hub):
        super().__init__()
        self.hub = hub

    def handle(self, event: dict):
        if event.get("type") == "motion":
            light = self.hub.get_device("living_room_light")
            if light:
                light.turn_on()
                light.set_brightness(100)
        elif event.get("light_off"):
            light = self.hub.get_device("light")
            if light:
                light.turn_off()
        super().handle(event)