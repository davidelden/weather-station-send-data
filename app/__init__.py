import ConfigParser, sys, serial
from sqlalchemy import create_engine
import os

dirname = os.path.dirname(__file__)
parent_dir = os.path.dirname(dirname)
config_file_name = os.path.join(parent_dir, 'config.py')

config = ConfigParser.RawConfigParser()
config.read(config_file_name)

SQLALCHEMY_DATABASE_URI = config.get('SQLAlchemy', 'SQLALCHEMY_DATABASE_URI')

arduino = serial.Serial('/dev/ttyACM0', 9600) # Arduino in RasPi USB
# arduino = serial.Serial('/dev/tty.usbmodem1421', 9600) # Arduino in iMac USB
db = create_engine(SQLALCHEMY_DATABASE_URI)
