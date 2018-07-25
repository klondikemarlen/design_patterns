from command.interface.generic import Command


class CeilingFanOnCommand(Command):
    def __init__(self, ceiling_fan):
        self.ceiling_fan = ceiling_fan

    def execute(self):
        self.ceiling_fan.high()


class CeilingFanOffCommand(Command):
    def __init__(self, ceiling_fan):
        self.ceiling_fan = ceiling_fan

    def execute(self):
        self.ceiling_fan.off()
