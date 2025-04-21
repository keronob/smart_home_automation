"""
Alert handler module for smart home system.
Manages and processes alerts from various devices and sensors.
"""

class AlertHandler:
    def __init__(self, next_handler=None):
        self._next = next_handler

    def set_next(self, handler):
        self._next = handler
        return handler

    def handle(self, event: dict):
        if self._next:
            self._next.handle(event)
