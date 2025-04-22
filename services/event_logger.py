# services/event_logger.py
import json
from datetime import datetime
from pathlib import Path

class EventLogger:
    def __init__(self, log_file="events_log.json"):
        self.log_file = Path(log_file)
        if not self.log_file.exists():
            self.log_file.write_text("[]")

    def log_event(self, event: dict):
        event["timestamp"] = event.get("timestamp") or datetime.now().isoformat()
        history = self.get_events_history()
        history.append(event)
        self.log_file.write_text(json.dumps(history, indent=4))
        print(f"📝 Event logged: {event}")

    def read_logs(self):
        with open(self.log_file, "r") as file:
            for line in file:
                yield json.loads(line)

    def get_events_history(self):
        try:
            return json.loads(self.log_file.read_text())
        except (json.JSONDecodeError, FileNotFoundError, PermissionError) as e:
            print(f"Error reading events log: {str(e)}")
            return []
        except Exception as e:
            print(f"Unexpected error reading events log: {str(e)}")
            return []


    def clear_history(self):
        self.log_file.write_text("[]")
        print("🗑️ Events history cleared.")


    def log_action(self,device_name:str, action:str,details:dict=None):
        event = {
            "device": device_name,
            "action": action,
            "timestamp": datetime.now().isoformat(),
            "details": details or {}
        }
        history = self.get_events_history()
        history.append(event)
        self.log_file.write_text(json.dumps(history, indent=4))
        print(f"📝 Action logged: {event}")