class Stereo:
    def __init__(self, name):
        self.name = name

    def on(self):
        print("{} Stereo is On.".format(self.name))

    def off(self):
        print("{} Stereo is Off.".format(self.name))

    def set_cd(self):
        print("{} Stereo is set to CD.".format(self.name))

    def set_dvd(self):
        print("{} Stereo is set to DVD.".format(self.name))

    def set_radio(self):
        print("{} Stereo is set to Radio.".format(self.name))

    def set_volume(self, level):
        print("{} Stereo Volume is set to {}.".format(self.name, level))

