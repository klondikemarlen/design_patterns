from observer.interfaces.display import DisplayElement
from observer.interfaces.observer import Observer


class StatisticsDisplay(Observer, DisplayElement):
    def __init__(self, observable):
        observable.add_observer(self)
        self.minimum = None
        self.maximum = None
        self.past_temperatures = []

    def update(self, obs, *args):
        temperature = obs.temperature
        self.past_temperatures.append(temperature)
        try:
            if temperature < self.minimum:
                self.minimum = temperature
            if temperature > self.maximum:
                self.maximum = temperature
        except TypeError:
            self.minimum = temperature
            self.maximum = temperature
            self.display()

    @property
    def average(self):
        return sum(self.past_temperatures) / len(self.past_temperatures)

    def display(self):
        print("Avg/Max/Min _temperature = {:0.1f}/{:0.1f}/{:0.1f}".format(self.average, self.maximum, self.minimum))
