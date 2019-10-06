# Name- Laurence SanBoeuf, Arpan Parashar
# Assignment title- Web-scraping weather forecast for the location entered by the user.
# Time taken- 1 Hour 30 minutes
# Description- This code scraps five-day weather data from the US weather forecast website for a location entered by its latitude and longitude by the user.
'''
# Assignment title: Final Project- Web-scraping Weather Forecast
# Date: 09/23/2019
# Description: The script web-scrapes the weather.gov website to extract the 5-Day weather forecast for a given location
# Inputs: Latitude & Longitude in Decimal Degrees
# Outputs: 5-Day Weather Forecast
'''

# import required libraries
import requests
from bs4 import BeautifulSoup

# List to store response
forecast = []

# Provide the latitude and longitude for the location you would like to check the forecast for
lat = str(input("Please enter the Latitude: "))
lon = str(input("Please enter the Longitude: "))

# Create url for the requested location through string concatenation
url = 'https://forecast.weather.gov/MapClick.php?lat='+lat+"&lon="+lon
# Check if the URL exists
# print url

# Send request to retrieve the web-page using the get() function from the requests library
# The page variable stores the response from the web-page
page = requests.get(url)

# Create a BeautifulSoup object with the response from the URL
# Access contents of the web-page using .content
# html_parser is used since our page is in HTML format
soup=BeautifulSoup(page.content,"html.parser")

# Locate elements on page to be scraped
# findAll() locates all occurrences of div tag with the given class name
# stores it in the BeautifulSoup object
weather_forecast = soup.findAll("li", {"class": "forecast-tombstone"})

# Loop through the BeautifulSoup object to extract text text from every class instance using .text
# Store results in a list
for i in weather_forecast:
    i = i.text
    forecast.append(i)

# Print list to remove unicode characters
for day in forecast:                          #These lines of code add spaces before, after and between the words to manipulate strings and make the output more presentable.
    day = day.replace('Low', ' Low')                        
    day = day.replace('High', ' High')
    day = day.replace('and', ' and')
    day = day.replace('Night', ' Night')
    day = day.replace('Showers', ' Showers')
    day = day.replace('then',' then ')
    day = day.replace('Scattered','Scattered ')
    day = day.replace('Clouds',' Clouds')
    day = day.replace('Likely', ' Likely')
    print day.upper()                         #Converts and prints output in Upper Case
