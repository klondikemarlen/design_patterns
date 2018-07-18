from observer.interfaces.subject import Observable


class WeatherData(Observable):
    def __init__(self):
        super().__init__()
        self.temperature = None
        self.humidity = None
        self.pressure = None

    def measurements_changed(self):
        self.set_changed()
        self.notify_observers()

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()
