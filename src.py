from getActual import getActualWeather
from extractActual import extractActual
from getForeCast import getWeatherForecast
from extractForeCast import *
from sleep_till_future import sleep_till_future
import datetime
import time

#fetching API key and City ID from the config file
try:
    with open('config.txt', 'r') as configFile:
        configData = configFile.read().splitlines()
        cityRAW = str(configData[1])
        apiRAW = (configData[4])
        cityID = cityRAW[7:]
        apiKey = apiRAW[7:]
except Exception:
    raise

#get weather forecast extract it to readable data (both human and script readeable)
getWeatherForecast.getWeatherForecast()
extractForecast.extractForecast()
extractForecast.getForecastDates()


with open('datafiles/forecastDateAndTimes.txt', 'r') as forecastDatesAndTimesFile:
    futureDatesAndTimes = forecastDatesAndTimesFile.readlines()
    for s in range(1,39):
        sleepUntilDateAndTime = datetime.datetime.strptime(futureDatesAndTimes[s][0:-1], '%Y-%m-%d %H:%M:%S')
        sleep_till_future.sleep_till_future(sleepUntilDateAndTime)


#print(str(futureTimes[0])[2:6])
#print(str(futureTimes[0])[7:9])
#print(str(futureTimes[0])[10:12])
#print(str(futureTimes[0])[13:15])
#print(str(futureTimes[0])[16:18])
