from mediator.smart_home_hub import SmartHomeHub
from devices.smart_light import SmartLight
from devices.alarm import Alarm
from devices.phone_dialer import PhoneDialer
from handlers.light_handler import LightHandler
from handlers.alarm_handler import AlarmHandler
from handlers.phone_call_handler import PhoneCallHandler

def create_hub():
    hub = SmartHomeHub()

    # Register devices
    hub.register_device("living_room_light", SmartLight("Living Room"))
    hub.register_device("alarm", Alarm("Security Alarm"))
    hub.register_device("dialer", PhoneDialer("Emergency Dialer", "911"))

    # Setup handler chain
    light_handler = LightHandler(hub)
    alarm_handler = AlarmHandler(hub)
    phone_handler = PhoneCallHandler(hub)

    light_handler.set_next(alarm_handler).set_next(phone_handler)
    hub.set_handler_chain(light_handler)

    return hub
