import ConfigParser
import os

dirname = os.path.dirname(__file__)
parent_dir = os.path.dirname(dirname)
config_file_name = os.path.join(parent_dir, 'config.py')

config = ConfigParser.RawConfigParser()
config.read(config_file_name)

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
