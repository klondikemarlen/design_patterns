from observer.interfaces.display import DisplayElement
from observer.interfaces.observer import Observer


class ForecastDisplay(Observer, DisplayElement):
    def __init__(self, observable):
        observable.add_observer(self)
        self.forecast = None
        self.current_pressure = None
        self.last_pressure = None

    def update(self, obs, *args):
        self.last_pressure = self.current_pressure
        self.current_pressure = obs.pressure

        try:
            if self.current_pressure > self.last_pressure:
                self.forecast = "Improving weather on the way!"
            elif self.current_pressure == self.last_pressure:
                self.forecast = "More of the same"
            elif self.current_pressure < self.last_pressure:
                self.forecast = "Watch out for cooler, rainy weather"
        except TypeError:
            self.forecast = "Not enough data yet"
        self.display()

    def display(self):
        print("Forecast: {}".format(self.forecast))
