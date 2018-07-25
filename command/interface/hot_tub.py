from command.interface.generic import Command


class HotTubOnCommand(Command):
    def __init__(self, hot_tub):
        self.hot_tub = hot_tub

    def execute(self):
        self.hot_tub.set_temperature(102)
        self.hot_tub.jets_on()
        self.hot_tub.circulate()

    def undo(self):
        self.hot_tub.set_temperature(50)
        self.hot_tub.jets_off()


class HotTubOffCommand(Command):
    def __init__(self, hot_tub):
        self.hot_tub = hot_tub

    def execute(self):
        self.hot_tub.set_temperature(50)
        self.hot_tub.jets_off()

    def undo(self):
        self.hot_tub.set_temperature(102)
        self.hot_tub.jets_on()
        self.hot_tub.circulate()
