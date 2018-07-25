from command.interface.generic import Command


class GarageDoorUpCommand(Command):
    def __init__(self, garage):
        self.garage = garage

    def execute(self):
        self.garage.up()


class GarageDoorDownCommand(Command):
    def __init__(self, garage):
        self.garage = garage

    def execute(self):
        self.garage.down()
