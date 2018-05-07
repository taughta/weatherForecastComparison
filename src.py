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

### DEFINING FUNCTIONS

# This function requests the actual weather by sending a GET request to OpenWeatherMap.
# The ID of the city and the API key is fetched from the config and used in the request URL.
# The actual weather data is saved into a file both in "raw" and "pretty" format.

def getActualWeather():
    from src import cityID, apiKey
    import json
    import urllib3

    # fetching actual weather
    http = urllib3.PoolManager()
    requestURL = 'http://api.openweathermap.org/data/2.5/weather?id=' + cityID + '&units=metric&appid=' + apiKey
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

# This function requests weather forecast by sending a GET request to OpenWeatherMap.
# The ID of the city and the API key is fetched from the config and used in the request URL.
# The forecast data is saved into a file both in "raw" and "pretty" format.

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

# A function that extracts the following information from the previously
# requested actual weather to be compared against the forecast data:
# humidity, pressure, temperature, wind speed

def extractActual():
    with open('dataFiles/actualWeatherPRETTY.txt', 'r') as prettyActualFile:
        with open('dataFiles/actualExtracted.txt', 'w+') as actualExtractedFile:
            for num, line in enumerate(prettyActualFile, 1):
                if "humidity" in line:
                    startingPoint = line.find('"')
                    actualExtractedFile.write(line[startingPoint:])
                elif "pressure" in line:
                    startingPoint = line.find('"')
                    actualExtractedFile.write(line[startingPoint:])
                elif '"temp"' in line:
                    startingPoint = line.find('"')
                    actualExtractedFile.write(line[startingPoint:])
                elif "speed" in line:
                    startingPoint = line.find('"')
                    actualExtractedFile.write(line[startingPoint:])
                elif "description" in line:
                    startingPoint = line.find('"')
                    actualExtractedFile.write(line[startingPoint:])

# This function extracts the following informations from the previously requested weather FORECAST::
# forecast time, humidity, pressure, temperature, wind speed

def extractForecast():
    with open('dataFiles/forecastWeatherPRETTY.txt', 'r') as prettyForeCastFile:
        with open('dataFiles/forecastExtracted.txt', 'w+') as forecastExtractedFile:
            for num, line in enumerate(prettyForeCastFile, 1):
                if "dt_txt" in line:
                    startingPoint = line.find('"')
                    forecastExtractedFile.write(line[startingPoint:])
                elif "humidity" in line:
                    startingPoint = line.find('"')
                    forecastExtractedFile.write(line[startingPoint:])
                elif "pressure" in line:
                    startingPoint = line.find('"')
                    forecastExtractedFile.write(line[startingPoint:])
                elif '"temp"' in line:
                    startingPoint = line.find('"')
                    forecastExtractedFile.write(line[startingPoint:])
                elif "speed" in line:
                    startingPoint = line.find('"')
                    forecastExtractedFile.write(line[startingPoint:])
                elif "description" in line:
                    startingPoint = line.find('"')
                    forecastExtractedFile.write(line[startingPoint:])

def getForecastDates():
    with open('datafiles/forecastDateAndTimes.txt', 'w+') as forecastTimesFile:
        with open('dataFiles/forecastExtracted.txt', 'r') as forecastExtractedFile:
            forecastFileData = forecastExtractedFile.readlines()
            for d in range(0, 240, 6):
                forecastTimesFile.write((forecastFileData[d])[11:-3] + '\n')

def sleep_till_future(futureDate):

    # The function takes the current time, and calculates for how many seconds should sleep until a user provided minute in the future.

    t = datetime.datetime.today()
    seconds_till_future = (futureDate - t).total_seconds()

    assert futureDate > t, '***ERROR! Future date is actually in the past (futureDate < currentDate).'

    print("Current date (MMDDYYYY): " + str(t.month) + "." + str(t.day) + "." + str(t.year) + " " + str(
        t.hour) + ":" + str(t.minute))
    print("Sleep until (MMDDYYYY):  " + str(futureDate.month) + "." + str(futureDate.day) + "." + str(
        futureDate.year) + " " + str(futureDate.hour) + ":" + str(futureDate.minute))
    print("I will sleep " + str(seconds_till_future) + " seconds.")

    time.sleep(seconds_till_future)
    print("I slept for " + str(seconds_till_future) + " seconds!")

#compare actual weather against forecast data at the forecast date
def compare(futureDate):
    with open('dataFiles/actualExtracted.txt','r') as actualFile:
        actualData = actualFile.readlines()
        actualHumidity = float(actualData[0][12:-2])
        actualPressure = float(actualData[1][12:-2])
        actualTemp = float(actualData[2][8:-2])
        actualDesc = str(actualData[3][16:-2])
        actualSpeed = float(actualData[4][9:-1])

    with open('dataFiles/forecastExtracted.txt','r') as forecastFile:
        forecastData = forecastFile.readlines()
        for s in range(0,len(forecastData)):
            if str(futureDate) in forecastData[s]:
                forecastHumidity = float(forecastData[s+1][12:-2])
                forecastPressure = float(forecastData[s+2][12:-2])
                forecastTemp = float(forecastData[s+3][8:-2])
                forecastDesc = str(forecastData[s+4][16:-3])
                forecastSpeed = float(forecastData[s+5][9:-1])

    humidityDiff = round(forecastHumidity - actualHumidity)
    pressureDiff = round(forecastPressure - actualPressure)
    tempDiff = round(forecastTemp - actualTemp)
    descDiff = str(forecastDesc + " vs. " + actualDesc)
    speedDiff = round(forecastSpeed - actualSpeed)

    differencies = {"humidityDiff":humidityDiff,"pressureDiff":pressureDiff,"tempDiff":tempDiff,"descDiff":descDiff,"speedDiff":speedDiff}

    with open('datafiles/comparisonResults.txt','a+') as compResultsFile:
        compResultsFile.write(str(futureDate)+"\n")
        compResultsFile.write(str(differencies)+"\n\n")

#get weather forecast extract it to readable data (both human and script readeable)
getWeatherForecast()
extractForecast()
getForecastDates()

with open('datafiles/forecastDateAndTimes.txt', 'r') as forecastDatesAndTimesFile:
    futureDatesAndTimes = forecastDatesAndTimesFile.readlines()
    for s in range(1,len(futureDatesAndTimes):
        sleepUntilDateAndTime = datetime.datetime.strptime(futureDatesAndTimes[s][0:-1], '%Y-%m-%d %H:%M:%S')
        sleep_till_future(sleepUntilDateAndTime)
        getActualWeather()
        extractActual()
        compare(sleepUntilDateAndTime)

#creating graphs 
import matplotlib.pyplot as plt
import ast

with open('dataFiles\comparisonResults.txt') as compFile:
    comparisonResults = compFile.readlines()
    allHumiDiff = []
    allPressureDiff = []
    allTempDiff = []
    allSpeedDiff = []
    singleLine = [0]
    for i in range(1,len(comparisonResults),3):
        # convert string formatted dictinaries to actual dictinaries then adding to lists to use it for graph creation
        diffData = ast.literal_eval(comparisonResults[i][:-1])
        allHumiDiff.append(diffData["humidityDiff"])
        allPressureDiff.append(diffData["pressureDiff"])
        allTempDiff.append(diffData["tempDiff"])
        allSpeedDiff.append(diffData["speedDiff"])

    # generate x axis integer numbers
    xAxis = [i for i in range(0,len(allTempDiff))]

    # associating strings (time passed since forecast) to X axis integers
    xAxisString = []
    for x in range(3, len(comparisonResults)+1,3):
        xAxisString.append("+%ih" %x)


    #setting the size of the graph
    plt.figure(figsize=(15, 9))

    # setting the annotation style
    annotStyle = dict(size=10, color = 'purple', fontweight = 'bold',va = 'center', ha = 'left', bbox=dict(boxstyle = "circle",fc = 'w',pad=0.3))

    # temperature graph creation
    tempgraph = plt.subplot(4, 1, 1)
    plt.xticks(xAxis,xAxisString)
    plt.plot(xAxis, allTempDiff, marker = 'o', color = 'c')
    plt.title('Temperature (forecast vs. actual)')
    # annotating values
    for x in range(0,len(allTempDiff)):
        tempgraph.annotate('%i' %allTempDiff[x], xy=(xAxis[x], allTempDiff[x]), **annotStyle)

    # wind speed graph creation
    windSpeedGraph = plt.subplot(4, 1, 2)
    plt.xticks(xAxis, xAxisString)
    plt.plot(xAxis, allSpeedDiff, marker = 'o', color = 'm')
    plt.title('Wind Speed (forecast vs. actual)')
    # annotating values:
    for w in range(0,len(allSpeedDiff)):
        windSpeedGraph.annotate('%i' %allSpeedDiff[w], xy = (xAxis[w], allSpeedDiff[w]), **annotStyle)

    # humidity graph creation
    humidityGraph = plt.subplot(4,1,3)
    plt.xticks(xAxis,xAxisString)
    plt.plot(xAxis, allHumiDiff, marker = 'o', color = 'y')
    plt.title("Humidity (forecast vs. actual)")
    # annotating values:
    for jh in range(0,len(allHumiDiff)):
        humidityGraph.annotate('%i' %allHumiDiff[jh], xy = (xAxis[jh], allHumiDiff[jh]), **annotStyle)

    # pressure graph creation
    pressureGraph = plt.subplot(4, 1, 4)
    plt.xticks(xAxis,xAxisString)
    plt.plot(xAxis, allPressureDiff, marker = 'o', color = 'g' )
    plt.title("Pressure (forecast vs. actual)")
    for ko in range(0,len(allPressureDiff)):
        pressureGraph.annotate('%i' %allPressureDiff[ko], xy = (xAxis[ko], allPressureDiff[ko]), **annotStyle)

    # make it fance
    plt.tight_layout()

    # save and display the graph
    # the graph will be displayed always, saving the graph is tried
    try:
        plt.savefig('weatherGraphs.png')
    except Exception:
        raise
    finally:
        plt.show()

    print('The graph is saved as "weatherGraphs.png" to actual folder.\n')
