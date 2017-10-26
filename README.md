# weather-station-send-data
Send weather data to database and WeatherUnderground from RaspberryPi.

This project uses the **ConfigParser** library, which reads variables from a configuration file. 

Add a `config.py` file to the root with the following variables (include headers in [ ]:

####[SQLAlchemy]
* SQLALCHEMY\_DATABASE\_URI

####[WeatherUnderground]
* WU\_STATION\_ID
* WU\_PASSWORD
* WU\_API\_ENDPOINT