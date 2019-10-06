#!env/bin/python
import datetime, requests
from app import arduino, db, models, wu_post
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(db)
session = Session()

get_weather = session.query(models.WeatherData).order_by(models.WeatherData.id.desc()).first()
data = arduino.readline().split()
dateutc = datetime.datetime.utcnow()

while data[0] == 'AM2315' or data[0] == '0.00' or data[1] == '-4.00':
  data = arduino.readline().split()
  print data

if len(data) == 3 and data[0] != 'AM2315' and data[0] != '0.00':
  humidity = float(data[0])
  dewptf = float(data[1])
  tempf = float(data[2])
  db_data = models.WeatherData(dateutc=dateutc, humidity=humidity, dewptf=dewptf, tempf=tempf)

  # Insert data into db
  session.add(db_data)
  session.commit()

  print(get_weather)

  # Send data to WeatherUnderground
  wu_data = wu_post.wu_data(dateutc, humidity, dewptf, tempf)
  req = requests.get(url = wu_post.WU_API_ENDPOINT, params = wu_data)
  res = req._content

  print("WU Response: %s"%res)
