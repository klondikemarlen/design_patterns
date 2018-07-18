from observer.weather_data import WeatherData
from observer.displays.current_conditions import CurrentConditionsDisplay
from observer.displays.statistics import StatisticsDisplay
from observer.displays.forecast import ForecastDisplay
from observer.displays.heat_index import HeatIndexDisplay

weather_data = WeatherData()

current_display = CurrentConditionsDisplay(weather_data)
statistics_display = StatisticsDisplay(weather_data)
forecast_display = ForecastDisplay(weather_data)
heat_index_display = HeatIndexDisplay(weather_data)

weather_data.set_measurements(80, 65, 30.4)
weather_data.set_measurements(82, 70, 29.2)
weather_data.set_measurements(78, 90, 29.2)
