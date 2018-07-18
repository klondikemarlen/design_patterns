from observer.interfaces.display import DisplayElement
from observer.interfaces.observer import Observer


class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, observable):
        observable.add_observer(self)
        self.temperature = None
        self.humidity = None

    def update(self, obs, *args):
        self.temperature = obs.temperature
        self.humidity = obs.humidity
        self.display()

    def display(self):
        print("Current conditions: {}F degrees and {}% humidity".format(self.temperature, self.humidity))
