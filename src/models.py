from datetime import datetime


class MoistureReading:
    def __init__(self, raw_value: float, voltage: float):
        self.timestamp = datetime.utcnow()
        self.raw_value = raw_value
        self.voltage = voltage

    def to_tuple(self) -> tuple:
        return (self.timestamp, self.raw_value, self.voltage)
