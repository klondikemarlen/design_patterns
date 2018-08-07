class TheatreLights:
    def __init__(self, name):
        self.name = "Theatre " + name + " Lights"
        self.percent = 100

    def dim(self, percent):
        self.percent = percent
        print(self.name + " dimming to {}%.".format(self.percent))

    def on(self):
        self.percent = 100
        print(self.name + " on.")
