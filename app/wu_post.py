import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('config.py')

WU_STATION_ID = config.get('WeatherUnderground', 'WU_STATION_ID')
WU_PASSWORD = config.get('WeatherUnderground', 'WU_PASSWORD')
WU_API_ENDPOINT = config.get('WeatherUnderground', 'WU_API_ENDPOINT')

def wu_data(dateutc, humidity, dewptf, tempf):
  return  {
            'ID': WU_STATION_ID,
            'PASSWORD': WU_PASSWORD,
            'dateutc': dateutc,
            'humidity': humidity,
            'dewptf': dewptf,
            'tempf': tempf,
            'softwaretype': 'RaspberryPi',
            'action': 'updateraw'
          }