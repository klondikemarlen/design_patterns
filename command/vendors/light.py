class Light:
    def __init__(self, name):
        self.name = name

    def on(self):
        print("{} Light is On.".format(self.name))

    def off(self):
        print("{} Light is Off.".format(self.name))
