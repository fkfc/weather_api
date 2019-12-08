import pytest
from weather_api.models import City, Forecast, Report

CITY_ID_1 = 1
CITY_ID_2 = 2
CITY_NAME_1 = 'city_1'
CITY_NAME_2 = 'city_2'
CITY_STATE_1 = 'state_1'
CITY_STATE_2 = 'state_2'
CITY_COUNTRY_1 = 'BR'
TEMPERATURE_1 = 25
TEMPERATURE_2 = 30
TEMPERATURE_3 = 35
TEMPERATURE_4 = 40
PROBABILITY_1 = 20
PROBABILITY_2 = 40
PRECIPITATION_1 = 10
PRECIPITATION_2 = 20
DATE_1 = "2019-12-01"
DATE_2 = "2019-12-02"

@pytest.mark.parametrize("id,name,state,country", [
    (CITY_ID_1, CITY_NAME_1, CITY_STATE_1, CITY_COUNTRY_1),
    (CITY_ID_2, CITY_NAME_2, CITY_STATE_2, CITY_COUNTRY_1),
    (CITY_ID_2, CITY_NAME_1, CITY_STATE_1, CITY_COUNTRY_1)
])

def test_city_dict(id, name, state, country):
    city = City(id, name, state, country)
    city_dict = city.to_dict()
    assert city_dict['id'] == id
    assert city_dict['name'] == name
    assert city_dict['state'] == state
    assert city_dict['country'] == country

@pytest.mark.parametrize("city,date,rain_probability,rain_precipitation,temperature_min,temperature_max", [
    (City(CITY_ID_1, CITY_NAME_1, CITY_STATE_1, CITY_COUNTRY_1), DATE_1, PROBABILITY_1, PRECIPITATION_1, TEMPERATURE_1, TEMPERATURE_2),
    (City(CITY_ID_2, CITY_NAME_2, CITY_STATE_2, CITY_COUNTRY_1), DATE_2, PROBABILITY_2, PRECIPITATION_2, TEMPERATURE_3, TEMPERATURE_4)
])

def test_forecast_dict(city, date, rain_probability, rain_precipitation, temperature_min, temperature_max):
    forecast = Forecast(city, date, rain_probability, rain_precipitation, temperature_min, temperature_max)
    forecast_dict = forecast.to_dict()
    assert forecast_dict['date'] == date
    assert forecast_dict['rain']['probability'] == rain_probability
    assert forecast_dict['rain']['precipitation'] == rain_precipitation
    assert forecast_dict['temperature']['minimum'] == temperature_min
    assert forecast_dict['temperature']['maximum'] == temperature_max

@pytest.mark.parametrize("start_date,end_date,forecasts,hottest_city_id,hottest_city_temperature,avg_precipitations", [
    (
        DATE_1,
        DATE_2,
        [
            Forecast(City(CITY_ID_1, CITY_NAME_1, CITY_STATE_1, CITY_COUNTRY_1), DATE_1, PROBABILITY_1, PRECIPITATION_1, TEMPERATURE_1, TEMPERATURE_2),
            Forecast(City(CITY_ID_1, CITY_NAME_1, CITY_STATE_1, CITY_COUNTRY_1), DATE_2, PROBABILITY_1, PRECIPITATION_2, TEMPERATURE_1, TEMPERATURE_2),
            Forecast(City(CITY_ID_2, CITY_NAME_2, CITY_STATE_2, CITY_COUNTRY_1), DATE_1, PROBABILITY_1, PRECIPITATION_1, TEMPERATURE_3, TEMPERATURE_4)
        ],
        CITY_ID_2,
        TEMPERATURE_4,
        [(PRECIPITATION_1 + PRECIPITATION_2) / 2, PRECIPITATION_1]
    ),
    (
        DATE_1,
        DATE_2,
        [
            Forecast(City(CITY_ID_1, CITY_NAME_1, CITY_STATE_1, CITY_COUNTRY_1), DATE_1, PROBABILITY_1, PRECIPITATION_1, TEMPERATURE_3, TEMPERATURE_4),
            Forecast(City(CITY_ID_2, CITY_NAME_2, CITY_STATE_2, CITY_COUNTRY_1), DATE_1, PROBABILITY_1, PRECIPITATION_1, TEMPERATURE_1, TEMPERATURE_2),
            Forecast(City(CITY_ID_2, CITY_NAME_2, CITY_STATE_2, CITY_COUNTRY_1), DATE_2, PROBABILITY_1, PRECIPITATION_2, TEMPERATURE_1, TEMPERATURE_2),
        ],
        CITY_ID_1,
        TEMPERATURE_4,
        [PRECIPITATION_1, (PRECIPITATION_1 + PRECIPITATION_2) / 2]
    )
])

def test_report_dict(start_date, end_date, forecasts, hottest_city_id, hottest_city_temperature, avg_precipitations):
    report = Report(start_date, end_date, forecasts)
    report_dict = report.to_dict()
    assert report_dict['highest_temperature_max']['city']['id'] == hottest_city_id
    assert report_dict['highest_temperature_max']['temperature'] == hottest_city_temperature
    for i in range(len(avg_precipitations)):
        assert report_dict['average_precipitation'][i]['average_precipitation'] == avg_precipitations[i]
