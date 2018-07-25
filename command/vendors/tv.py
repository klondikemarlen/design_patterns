class TV:
    def __init__(self, location):
        self.location = location
        self.input_channel = 0
        self.volume = 11

    def on(self):
        print("{} TV is ON.".format(self.location))

    def off(self):
        print("{} TV is Off.".format(self.location))

    def set_input_channel(self, input_channel):
        self.input_channel = input_channel
        print("{} TV Channel set to {}".format(self.location, self.input_channel))

    def set_volume(self, volume):
        self.volume = volume
        print("{} TV Volume set to {}".format(self.location, self.volume))
