# This class contains a method that extracts the following informations from the previously requested weather FORECAST:
# - forecast time
# - humidity
# - pressure
# - temp
# - deg
# - speed

class extractForecast():
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
                    elif "deg" in line:
                        startingPoint = line.find('"')
                        forecastExtractedFile.write(line[startingPoint:])
                    elif "speed" in line:
                        startingPoint = line.find('"')
                        forecastExtractedFile.write(line[startingPoint:])

    def getForecastDates():
        with open('datafiles/forecastDateAndTimes.txt','w+') as forecastTimesFile:
            with open('dataFiles/forecastExtracted.txt', 'r') as forecastExtractedFile:
                futuretimes = []
                forecastFileData = forecastExtractedFile.readlines()
                for d in range(6, 240, 6):
                    forecastTimesFile.write((forecastFileData[d])[11:-3]+'\n')