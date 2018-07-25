from command.interface.generic import Command


class TVOnCommand(Command):
    def __init__(self, tv):
        self.tv = tv

    def execute(self):
        self.tv.on()
        self.tv.set_input_channel(0)
        self.tv.set_volume(19)

    def undo(self):
        self.tv.off()


class TVOffCommand(Command):
    def __init__(self, tv):
        self.tv = tv

    def execute(self):
        self.tv.off()

    def undo(self):
        self.tv.on()
        self.tv.set_input_channel(0)
        self.tv.set_volume(19)
