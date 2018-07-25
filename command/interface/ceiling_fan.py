from command.interface.generic import Command
from command.vendors.ceiling_fan import CeilingFan


class CeilingFanUndoMixin(Command):
    def __init__(self, ceiling_fan):
        self.ceiling_fan = ceiling_fan
        self.prev_speed = ceiling_fan.get_speed()

    def execute(self):
        self.prev_speed = self.ceiling_fan.get_speed()

    def undo(self):
        if self.prev_speed == CeilingFan.HIGH:
            self.ceiling_fan.high()
        elif self.prev_speed == CeilingFan.MEDIUM:
            self.ceiling_fan.medium()
        elif self.prev_speed == CeilingFan.LOW:
            self.ceiling_fan.low()
        elif self.prev_speed == CeilingFan.OFF:
            self.ceiling_fan.off()


class CeilingFanHighCommand(CeilingFanUndoMixin, Command):
    def __init__(self, ceiling_fan):
        super().__init__(ceiling_fan)

    def execute(self):
        super().execute()
        self.ceiling_fan.high()


class CeilingFanMediumCommand(CeilingFanUndoMixin, Command):
    def __init__(self, ceiling_fan):
        super().__init__(ceiling_fan)

    def execute(self):
        super().execute()
        self.ceiling_fan.medium()


class CeilingFanLowCommand(CeilingFanUndoMixin, Command):
    def __init__(self, ceiling_fan):
        super().__init__(ceiling_fan)

    def execute(self):
        super().execute()
        self.ceiling_fan.low()


class CeilingFanOffCommand(CeilingFanUndoMixin, Command):
    def __init__(self, ceiling_fan):
        super().__init__(ceiling_fan)

    def execute(self):
        super().execute()
        self.ceiling_fan.off()
