from adapter.vendors.amplifier import Amplifier
from adapter.vendors.tuner import Tuner
from adapter.vendors.dvd_player import DvdPlayer
from adapter.vendors.cd_player import CdPlayer
from adapter.vendors.projector import Projector
from adapter.vendors.screen import Screen
from adapter.vendors.theatre_lights import TheatreLights
from adapter.vendors.popcorn_popper import PopcornPopper
from adapter.home_theatre_example.home_theatre import HomeTheatreFacade


def test_home_theatre():
    amp = Amplifier("Top-O-Line")
    tuner = Tuner()
    dvd = DvdPlayer("Top-O-Line")
    cd = CdPlayer()
    projector = Projector("Top-O-Line")
    screen = Screen()
    lights = TheatreLights("Ceiling")
    popper = PopcornPopper()

    home_theatre = HomeTheatreFacade(amp, tuner, dvd, cd, projector, screen, lights, popper)
    home_theatre.watch_movie("Raiders of the Lost Ark")
    home_theatre.end_movie()
