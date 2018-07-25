class Stereo:
    def __init__(self, name):
        self.name = name

    def on(self):
        print("Stereo is On.")

    def off(self):
        print("Stereo is Off.")

    def set_cd(self):
        print("Stereo is set to CD.")

    def set_dvd(self):
        print("Stereo is set to DVD.")

    def set_radio(self):
        print("Stereo is set to Radio.")

    def set_volume(self, level):
        print("Stereo Volume is set to {}.".format(level))

