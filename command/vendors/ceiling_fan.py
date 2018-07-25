OFF = 0
LOW = 1
MEDIUM = 2
HIGH = 3

SPEEDS = ["OFF", "LOW", "MEDIUM", "HIGH"]


class CeilingFan:
    def __init__(self, name):
        self.name = name
        self.speed = OFF

    def high(self):
        self.speed = HIGH
        print("Ceiling Fan speed is HIGH.")

    def medium(self):
        self.speed = MEDIUM
        print("Ceiling Fan speed is MEDIUM.")

    def low(self):
        self.speed = LOW
        print("Ceiling Fan speed is LOW.")

    def off(self):
        self.speed = OFF
        print("Ceiling Fan speed is OFF.")

    def get_speed(self):
        print("Ceiling Fan speed is {}.".format(SPEEDS[self.speed]))
        return self.speed
