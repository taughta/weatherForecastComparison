# weatherForecastComparison

-==### IN PROGRESS ###==-

A program that requests weather forecast (every 3 hours for 6 days) then waits until the forecast dates then requests the actual weather and compare the actual values against the forecasted values.. It will also create graphs about the differencies.

The service that provides weather data is: https://openweathermap.org/

This is a free weather service (up to 60 requests/min) so you can get your own API key here: https://openweathermap.org/appid

The available cities for weather data are listed here (take note of the ID of the city): http://openweathermap.org/help/city_list.txt

Once you have your API key and city ID you should insert these data into the config file and initialize the application and let the application run for a week to gather data.

The barebone logic of the application (after fetching configs):

  1) Get forecast for a every 3 hours of every day for a week.
  2) Wait until the next forecast's date and time.
  3) Request actual weather at this date & time.
  4) Compare actual data against forecast data and store it into a file.
  
  --- Repeat #2, #3 and #4 until enough time passed to get actual weather for ALL forecast date and have enough compared data.
  
  5) Create fancy graphs about the differencies.
