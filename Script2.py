# Name: Laurence SanBoeuf, Arpan _
# Assignment title: Final Project
# Time to complete: ...
# Description:



# = These are notes related to the code
### = These are notes specifically related to our project; stuff that needs to be looked at


### I have split everything into groups to make it easier.







# -*- coding: utf-8 -*-

### ^-This may need to be changed!! ???

# Keep the line above when running script
# Tells python what encoding the string is stored in








# Import required libraries

### (do we need more libraries? do we need these libraries?)
import requests
from bs4 import BeautifulSoup







### country naming issues: In the URLS on the websites the countries are coded with
### a two digit code # "au" = australia, "in" = india. If we were to search for a
### country name or something like that we would need to have something to relate
### the country name to the two letter code so it can search for it. We can make a
### dictionary or a list or tuple? idk which

country = 'albania'
countrycode = [al: 'albania', af: 'afghanistan',]   ### this would take long to write
### it all out, maybe its possible to scrape these names? 








# Create url for the requested location through string concatenation

### url = 'https://forecast.weather.gov/MapClick.php?lat='+lat+"&lon="+lon  ## this was for the lab

url = 'https://www.census.gov/popclock/world/'+countrycode

### here is the url I want to use ""https://www.census.gov/popclock/world/as"""
### ("as" stands for australia, all countries have a two letter code in the URL)
### NOT THE US! https://www.census.gov/popclock/ <- the 'main' page has data on the US








# Send request to retrieve the web-page using the get() function from the requests library
# The page variable stores the response from the web-page
page = requests.get(url)

### this should be the same




# Create a BeautifulSoup object with the response from the URL
# Access contents of the web-page using .content
# html_parser is used since our page is in HTML format
soup=BeautifulSoup(page.content,"html.parser")

### This should also be the same, I think




# Locate element on page to be scraped
# This element is located within an id tag called current_conditions_detail
# find() locates the element in the BeautifulSoup object
### old code, needs to be changed :
### cur_weather_conditions = soup.find(id="current_conditions_detail")

population = soup.find(id="basic-facts" class="data-cell")


### here we need to take out the population data
### it is listed as <h2 data-population = "" >35.8</h2>






# Extract text from the selected BeautifulSoup object using .text
#  cur_weather_conditions = cur_weather_conditions.text

population = population.text
### ??? not sure this is right





#Final Output
#Return Scraped info
## old code -> print 'The Current Weather Details at '+ lat +  ", " + lon + " is:" + cur_weather_conditions


print 'The Population of'+country+'is'+population

### New code, should work?











#### EVERYTHING PAST HERE IS JUST CODE I DIDNT WANNA DELETE YET, in case we need something




weather_forecast = soup.findAll("h2", {"data-population": ""})

# Loop through the BeautifulSoup object to extract text text from every class instance using .text
# Store results in a list
for i in weather_forecast:
    i = i
    print i
    forecast.append(i)


    

forecast = '''

Tonight
ClearLow: 55 F

Thursday
Sunny thenChanceShowersHigh: 77 F

Friday
SunnyHigh: 73 F

Saturday
Mostly SunnyHigh: 77 F

Sunday
Mostly SunnyHigh: 71 F
'''

# Split string into a list
# Use two blank lines (\n\n) as the separator
# Creates a list item at every instance of separator
forecast_list = forecast.split('\n\n')

# Loop through list to make string replacements to each item
# Remove extra whitespaces or lines for a cleaner format
for day in forecast_list:
    day = day.replace('\n',': ')
    day = day.replace('High',', High')
    day = day.replace('Sunny thenChanceShowers', 'Sunny then Chance Showers')
    day = day.replace('ClearLow', 'Clear, Low')
    day = day.replace('F:','F')
    print day
    https://www.worldometers.info/world-population/kenya-population/
