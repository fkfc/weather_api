CREATE TABLE IF NOT EXISTS cities(
    id INTEGER PRIMARY KEY,
    name TEXT,
    state CHAR(50),
    country CHAR(50)
);

CREATE TABLE IF NOT EXISTS forecasts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city INTEGER,
    date CHAR(10),
    rain_probability REAL,
    rain_precipitation REAL,
    temperature_min REAL,
    temperature_max REAL
);
