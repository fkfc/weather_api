# http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/4704/days/15?token=b22460a8b91ac5f1d48f5b7029891b53

from db.repositories import ForecastRepository, CityRepository
from models import Report, City, Forecast
import requests

# Provides Forecasts and Reports retrieval methods
# Abstracts the Repositories and source data API requests
class WeatherService:
    _api_user_token = "b22460a8b91ac5f1d48f5b7029891b53"

    # Returns an array of Forecasts
    @staticmethod
    def get_forecasts_for_city(city_id):
        url = "http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/%s/days/15?token=%s" % (city_id, WeatherService._api_user_token)
        response = requests.get(url)
        if response.status_code != 200:
            return None
        else:
            response_data = response.json()
            city = CityRepository.save_city(
                City(city_id, response_data["name"], response_data["state"], response_data["country"])
            )
            return [
                ForecastRepository.save_forecast(
                    Forecast(
                        city,
                        data["date"],
                        data["rain"]["probability"],
                        data["rain"]["precipitation"],
                        data["temperature"]["min"],
                        data["temperature"]["max"]
                    )
                ) for data in response_data["data"]
            ]



    # Return a Report model object
    @staticmethod
    def get_report_for_date_range(start_date, end_date):
        forecasts = ForecastRepository.get_by_date_range(start_date, end_date)
        return Report(start_date, end_date, forecasts)
