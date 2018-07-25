class CeilingFan:
    OFF = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3

    def __init__(self, name):
        self.name = name
        self.speed = CeilingFan.OFF

    def high(self):
        self.speed = CeilingFan.HIGH
        print("{} Ceiling Fan speed is HIGH.".format(self.name))

    def medium(self):
        self.speed = CeilingFan.MEDIUM
        print("{} Ceiling Fan speed is MEDIUM.".format(self.name))

    def low(self):
        self.speed = CeilingFan.LOW
        print("{} Ceiling Fan speed is LOW.".format(self.name))

    def off(self):
        self.speed = CeilingFan.OFF
        print("{} Ceiling Fan speed is OFF.".format(self.name))

    def get_speed(self):
        return self.speed
