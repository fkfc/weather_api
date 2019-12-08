# WEATHER API
2019 - Felipe Kermentz Ferraz Costa


## Running
- Docker

    Build docker image:

        ```
        $ docker build -t weather_api . 
        ```
    
    Launch image:

        ```
        $ docker run -d -p 5000:5000 weather_api
        ```

- Manually

    Install dependencies:

        ```
        $ pip install -r requirements.txt
        ```

    Start the service:

        ```
        $ python run.py
        ```

- Running Tests

    Tests were made using pytest:

     ```$ python -m pytest```


## Usage

Default port: 5000


### 1. City Forecast Endpoint
**Parameters**

- city_id: City code

**URL**

```http://host:port/cidade?id=<city_id>```

Example: http://localhost:5000/cidade?id=4705

**Response example**
```
{
  "city": {
    "id": "4705", 
    "name": "Itacajá", 
    "state": "TO",
    "country": "BR"
  }, 
  "forecasts": [
    {
      "date": "2019-12-08", 
      "rain": {
        "precipitation": 15.0, 
        "probability": 90.0
      }, 
      "temperature": {
        "maximum": 33.0, 
        "minimum": 23.0
      }
    }, 
    {
      "date": "2019-12-09", 
      "rain": {
        "precipitation": 9.0, 
        "probability": 80.0
      }, 
      "temperature": {
        "maximum": 32.0, 
        "minimum": 23.0
      }
    }, 
    {
      "date": "2019-12-10", 
      "rain": {
        "precipitation": 10.0, 
        "probability": 86.0
      }, 
      "temperature": {
        "maximum": 32.0, 
        "minimum": 23.0
      }
    }, 
    {
      "date": "2019-12-11", 
      "rain": {
        "precipitation": 7.0, 
        "probability": 86.0
      }, 
      "temperature": {
        "maximum": 32.0, 
        "minimum": 24.0
      }
    }, 
    {
      "date": "2019-12-12", 
      "rain": {
        "precipitation": 8.0, 
        "probability": 80.0
      }, 
      "temperature": {
        "maximum": 34.0, 
        "minimum": 23.0
      }
    }, 
    {
      "date": "2019-12-13", 
      "rain": {
        "precipitation": 20.0, 
        "probability": 90.0
      }, 
      "temperature": {
        "maximum": 31.0, 
        "minimum": 24.0
      }
    }, 
    {
      "date": "2019-12-14", 
      "rain": {
        "precipitation": 1.0, 
        "probability": 60.0
      }, 
      "temperature": {
        "maximum": 36.0, 
        "minimum": 25.0
      }
    }
  ]
}
```


### 2. Statistics Report Endpoint
**Parameters**

- start_date: Beginning of the date range to search in, formatted as 'YYYY-MM-DD'
- end_date: End of the date range to search in, formatted as 'YYYY-MM-DD'

**URL**

```http://host:port/analise?data_inicial=<start_date>&data_final=<end_date>```

Example: http://localhost:5000/analise?data_inicial=2019-01-01&data_final=2019-12-31

**Response example**
```
{
  "start_date": "2019-01-01",
  "end_date": "2019-12-31", 
  "highest_temperature_max": {
    "city": {
      "id": 4705, 
      "name": "Itacajá", 
      "state": "TO",
      "country": "BR"
    }, 
    "temperature": 37.0
  },
  "average_precipitation": [
    {
      "average_precipitation": 12.0, 
      "city": {
        "id": 4704, 
        "name": "Babaçulândia", 
        "state": "TO",
        "country": "BR"
      }
    }, 
    {
      "average_precipitation": 7.142857142857143, 
      "city": {
        "id": 4705, 
        "name": "Itacajá", 
        "state": "TO",
        "country": "BR"
      }
    }, 
    {
      "average_precipitation": 18.714285714285715, 
      "city": {
        "id": 4703, 
        "name": "Duplo Céu", 
        "state": "SP",
        "country": "BR"
      }
    }
  ]
}
```
