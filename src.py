from getActual import getActualWeather
from extractActual import extractActual
from getForeCast import getWeatherForecast
from extractForeCast import *


try:
    with open('config.txt', 'r') as configFile:
        configData = configFile.read().splitlines()
        cityRAW = str(configData[1])
        apiRAW = (configData[4])
        cityID = cityRAW[7:]
        apiKey = apiRAW[7:]
except Exception:
    raise

getActualWeather.getActualWeather()
extractActual.extractActual()
getWeatherForecast.getWeatherForecast()
extractForecast.extractForecast()
extractForecast.getForecastDates()
extractForecast.getForecastDates()

