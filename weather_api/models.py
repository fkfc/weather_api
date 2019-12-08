class City:
    def __init__(self, id, name, state):
        self.id = id
        self.name = name
        self.state = state

    # custom comparator, overrides default method
    def __eq__(self, other):
        return self.id == other.id if isinstance(other, City) else False
    
    # custom comparator, overrides default method
    def __ne__(self, other):
        return self.id != other.id if isinstance(other, City) else True

    def __hash__(self):
        return self.id

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "state": self.state
        }


class Forecast:
    def __init__(self, city, date, rain_probability, rain_precipitation, temperature_min, temperature_max):
        self.city = city
        self.date = date
        self.rain_probability = float(rain_probability)
        self.rain_precipitation = float(rain_precipitation)
        self.temperature_min = float(temperature_min)
        self.temperature_max = float(temperature_max)
    def to_dict(self):
        return {            
            "date": self.date,
            "rain": {
                "probability": self.rain_probability,
                "precipitation": self.rain_precipitation
            },
            "temperature": {
                "minimum": self.temperature_min,
                "maximum": self.temperature_max
            }
        }


class Report:
    def __init__(self, start_date, end_date, forecasts):
        self.start_date = start_date
        self.end_date = end_date
        self.__calculateReport(forecasts)

    def __calculateReport(self, forecasts):
        self.highest_temperature_max_forecast = self._highest_temperature_max_forecast(forecasts)
        self.avg_precipitation_cities = self._avg_precipitation_cities(forecasts)

    def to_dict(self):
        return {
            "start_date": self.start_date,
            "end_date": self.end_date,
            "highest_temperature_max": {
                "city": self.highest_temperature_max_forecast.city.to_dict(),
                "temperature": self.highest_temperature_max_forecast.temperature_max
            },
            "average_precipitation": [avg_precipitation.to_dict() for avg_precipitation in self.avg_precipitation_cities]
        }

    # returns City with the highest 'temperature_max' in forecasts
    @staticmethod
    def _highest_temperature_max_forecast(forecasts):
        return max(forecasts, key=lambda forecast:forecast.temperature_max)

    # Returns array with AveragePrecipitation per city in forecasts
    @staticmethod
    def _avg_precipitation_cities(forecasts):
        print 'will compute average for ', forecasts
        c = map(lambda forecast:forecast.city, forecasts)
        print c
        print set(c)
        # list of cities present in the forecast array supplied
        cities = set(map(lambda forecast:forecast.city, forecasts))
        # forecasts array grouped by city
        forecasts_in_cities = [filter(lambda forecast:forecast.city == city, forecasts) for city in cities]        
        # return array of AveragePrecipitation objects
        return [AveragePrecipitation(city_forecasts) for city_forecasts in forecasts_in_cities]


class AveragePrecipitation:
    def __init__(self, city_forecasts):
        self.city = city_forecasts[0].city
        # array of precipitation values
        precipitations = map(lambda forecast:forecast.rain_precipitation, city_forecasts)
        # compute average precipitation
        self.average_precipitation = sum(precipitations) / len(precipitations)
    
    def to_dict(self):
        return {
            "city": self.city.to_dict(),
            "average_precipitation": self.average_precipitation
        }
