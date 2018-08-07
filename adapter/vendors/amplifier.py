class Amplifier:
    def __init__(self, name):
        self.name = name + " Amplifier"
        self.tuner = None
        self.dvd_player = None
        self.cd_player = None
        self.volume = 3

    def on(self):
        print(self.name + " on.")

    def off(self):
        print(self.name + " off.")

    def set_dvd(self, dvd):
        self.dvd_player = dvd
        print(self.name + " setting DVD Player to " + dvd.name + ".")

    def set_surround_sound(self):
        print(self.name + " surround sound on (5 speakers, 1 subwoofer).")

    def set_volume(self, volume):
        self.volume = volume
        print(self.name + " setting volume to {}.".format(volume))
