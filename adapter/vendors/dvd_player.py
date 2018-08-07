class DvdPlayer:
    def __init__(self, name):
        self.name = name + " DVD Player"
        self.movie = ""
        self.amplifier = None

    def on(self):
        print(self.name + " on.")

    def play(self, movie):
        self.movie = movie
        print(self.name + ' playing "' + self.movie + '".')

    def stop(self):
        print(self.name + ' stopped "' + self.movie + '".')

    def eject(self):
        self.movie = ""
        print(self.name + " eject.")

    def off(self):
        print(self.name + " off.")
