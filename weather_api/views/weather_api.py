from flask import Blueprint, request, jsonify
from ..services import WeatherService

weather_api = Blueprint('weather_api', __name__)

@weather_api.route("/cidade")
def get_forecasts_from_city():
    city_id = request.args.get('id')
    forecasts = WeatherService.get_forecasts_for_city(city_id)
    if forecasts == None or len(forecasts) == 0:
        return None
    else:
        return jsonify(
            {
                "city": forecasts[0].city.to_dict(),
                "forecasts": [forecast.to_dict() for forecast in forecasts]
            }
        )


@weather_api.route("/analise")
def get_report_from_date_range():
    start_date = request.args.get('data_inicial')
    end_date = request.args.get('data_final')
    report = WeatherService.get_report_for_date_range(start_date, end_date)
    if report == None:
        return None
    else:
        return jsonify(report.to_dict())
