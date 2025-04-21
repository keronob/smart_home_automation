# main.py

from mediator.smart_home_hub import SmartHomeHub

# Devices
from devices.smart_light import SmartLight
from devices.alarm import Alarm
from devices.phone_dialer import PhoneDialer

# Handlers (Chain of Responsibility)
from handlers.light_handler import LightHandler
from handlers.alarm_handler import AlarmHandler
from handlers.phone_call_handler import PhoneCallHandler

# Sensors
from sensors.motion_sensors import MotionSensor
from sensors.smoke_sensor import SmokeSensor

# -------------------------------
# Initialize Hub (Mediator)
hub = SmartHomeHub()

# Register Devices
hub.register_device("living_room_light", SmartLight("Living Room"))
hub.register_device("alarm", Alarm("Security Alarm"))
hub.register_device("dialer", PhoneDialer("Emergency Dialer", "911"))

# Setup Chain of Responsibility
light_handler = LightHandler(hub)
alarm_handler = AlarmHandler(hub)
phone_call_handler = PhoneCallHandler(hub)

# Chain setup: Light → Alarm → Phone
light_handler.set_next(alarm_handler).set_next(phone_call_handler)
hub.set_handler_chain(light_handler)

# Create and activate sensors
motion_sensor = MotionSensor(hub)
smoke_sensor = SmokeSensor(hub, location="Kitchen")

motion_sensor.activate()
smoke_sensor.activate()

# -------------------------------
# Simulate Events

print("\n--- 🏃 Motion Sensor Triggered ---")
motion_sensor.motion_detected()

print("\n--- 🔥 Smoke Sensor Triggered ---")
smoke_sensor.detect_smoke()

print("\n--- 📋 Final System Status ---")
status = hub.get_system_status()
for device, s in status.items():
    print(f"{device}: {s}")
