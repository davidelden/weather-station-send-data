from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import *

Base = declarative_base()

class WeatherData(Base):
  __tablename__ = 'weather_data'

  id = Column(INTEGER, primary_key=True)
  dateutc = Column(TIMESTAMP)
  humidity = Column(REAL)
  dewptf = Column(REAL)
  tempf = Column(REAL)

  def __repr__(self):
    return "<Weather dateutc='%s', humidity='%s', dewptf='%s', tempf='%s'>" % (self.dateutc, self.humidity, self.dewptf, self.tempf)