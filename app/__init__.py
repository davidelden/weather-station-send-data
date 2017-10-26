import ConfigParser, sys, serial
from sqlalchemy import create_engine

config = ConfigParser.RawConfigParser()
config.read('config.py')

SQLALCHEMY_DATABASE_URI = config.get('SQLAlchemy', 'SQLALCHEMY_DATABASE_URI')

arduino = serial.Serial('/dev/ttyACM0', 9600) # Arduino in RasPi USB
# arduino = serial.Serial('/dev/tty.usbmodem1421', 9600) # Arduino in iMac USB
db = create_engine(SQLALCHEMY_DATABASE_URI)