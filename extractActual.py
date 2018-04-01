# This class contains a method that extracts the following informations from the previously requested actual weather:
# - humidity
# - pressure
# - temp
# - deg
# - speed

class extractActual():
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
                    elif "deg" in line:
                        startingPoint = line.find('"')
                        actualExtractedFile.write(line[startingPoint:])
                    elif "speed" in line:
                        startingPoint = line.find('"')
                        actualExtractedFile.write(line[startingPoint:])