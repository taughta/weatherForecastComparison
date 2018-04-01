# This class contains a method that requests the actual weather by sending a GET request to OpenWeatherMap.
# The ID of the city and the API key is fetched from the main thread and used in the request URL.
# The actual weather data is saved into a file both in "raw" and "pretty" format.

class getActualWeather():

    def getActualWeather():
        from src import cityID, apiKey
        import json
        import urllib3

        # fetching actual weather
        http = urllib3.PoolManager()
        requestURL = 'http://api.openweathermap.org/data/2.5/weather?id='+cityID+'&units=metric&appid='+apiKey
        actualWeatherHTTP = http.request('GET', requestURL)
        actualWeatherRAW = str(actualWeatherHTTP.data)

        # writing actual data into a file
        with open('dataFiles/actualWeatherRAW.txt', 'w+') as actualWeatherFILE:
            actualWeatherFILE.write(actualWeatherRAW[2:-1])

        # writing the pretty version of actual data into a file
        with open('dataFiles/actualWeatherPRETTY.txt', 'w+') as prettyActualFile:
            actualWeatherParsed = json.loads(actualWeatherRAW[2:-1])
            prettyData = json.dumps(actualWeatherParsed, indent=4, sort_keys=True)
            prettyActualFile.write(prettyData)

        return actualWeatherRAW