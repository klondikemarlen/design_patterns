class Projector:
    def __init__(self, name):
        self.name = name + " Projector"
        self.dvd_player = None

    def on(self):
        print(self.name + " on.")

    def wide_screen_mode(self):
        print(self.name + " in widescreen mode (16x9 aspect ratio).")

    def off(self):
        print(self.name + " off.")
