from ..models import City, Forecast
from .database import Database

class CityRepository:
    @staticmethod
    def save_city(city):
        existing_city = CityRepository.get_by_id(city.id)
        if existing_city == None:
            Database.execute(
                "INSERT INTO cities (id, name, state) values (?, ?, ?)",
                (city.id, city.name, city.state)
            )
        return city

    @staticmethod
    def get_by_id(city_id):
        rows = Database.execute(
            "SELECT name, state FROM cities WHERE id = ?",
            (city_id,)
        )
        return City(city_id, rows[0][0], rows[0][1]) if len(rows) > 0 else None

class ForecastRepository:
    @staticmethod
    def save_forecast(forecast):
        if not ForecastRepository.exists(forecast):
            Database.execute(
                "INSERT INTO forecasts \
                    (city, date, rain_probability, rain_precipitation, temperature_min, temperature_max) \
                VALUES \
                    (?, ?, ?, ?, ?, ?)",
                (forecast.city.id, forecast.date, forecast.rain_probability, forecast.rain_precipitation, forecast.temperature_min, forecast.temperature_max)
            )
        return forecast

    @staticmethod
    def exists(forecast):
        rows = Database.execute("SELECT id FROM forecasts WHERE city = ? AND date = ?", (forecast.city.id, forecast.date))
        return len(rows) > 0

    @staticmethod
    def get_by_date_range(start_date, end_date):
        rows = Database.execute(
            "SELECT \
                city, date, rain_probability, rain_precipitation, temperature_min, temperature_max \
            FROM forecasts \
            WHERE date BETWEEN ? AND ?",
            (start_date, end_date)
        )
        return [Forecast(CityRepository.get_by_id(row[0]), row[1], row[2], row[3], row[4], row[5]) for row in rows]
