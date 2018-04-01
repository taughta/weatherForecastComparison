# This class contains a method that requests weather forecast by sending a GET request to OpenWeatherMap.
# The ID of the city and the API key is fetched from the main thread and used in the request URL.
# The forecast data is saved into a file both in "raw" and "pretty" format.

class getWeatherForecast(object):

    def getWeatherForecast():
        from src import cityID,apiKey
        import json
        import urllib3

        # fetching weather forecast
        http = urllib3.PoolManager()
        requestURL = 'http://api.openweathermap.org/data/2.5/forecast?id='+cityID+'&units=metric&appid='+apiKey
        forecastWeatherHTTP = http.request('GET', requestURL)
        forecastWeatherRAW = str(forecastWeatherHTTP.data)

        # writing forecast data into a file
        with open('dataFiles/forecastWeatherRAW.txt', 'w+') as forecastWeatherFILE:
            forecastWeatherFILE.write(forecastWeatherRAW[2:-1])

        # writing the pretty version of actual data into a file
        with open('dataFiles/forecastWeatherPRETTY.txt', 'w+') as prettyForecastFile:
            forecastWeatherParsed = json.loads(forecastWeatherRAW[2:-1])
            prettyData = json.dumps(forecastWeatherParsed, indent=4, sort_keys=True)
            prettyForecastFile.write(prettyData)

        return forecastWeatherRAW