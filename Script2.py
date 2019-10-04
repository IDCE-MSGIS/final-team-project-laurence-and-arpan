# Name: Laurence SanBoeuf, Arpan _
# Assignment title: Final Project
# Time to complete: ...
# Description:



# = These are notes related to the code
### = These are notes specifically related to our project; stuff that needs to be looked at




# -*- coding: utf-8 -*-
# Keep the line above when running script
# Tells python what encoding the string is stored in





# Import required libraries

### (do we need more libraries? do we need these libraries?)
import requests
from bs4 import BeautifulSoup

# List to store response
forecast = []

# Create url for the requested location through string concatenation
url = 'https://www.worldometers.info/world-population/kenya-population/'

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
#population = soup.findAll("span", {"class": ""})

#for strings in population:
#  print strings

#####This KIND OF works. It gives back too much information, but the right information is there. I might try to mess with it more
###### but I THINK we could use this and then just use replace functions to pull out the numbers? does that seen like it makes any sense?





# Locate elements on page to be scraped
# findAll() locates all occurrences of div tag with the given class name
# stores it in the BeautifulSoup object
#population = soup.findAll("div", {"class":"col-md-8 country-pop-description"})
#for i in population:
#  print (i.text)

  
  
# Locate elements on page to be scraped
# findAll() locates all occurrences of div tag with the given class name
# stores it in the BeautifulSoup object
population = soup.findAll("div", {"class":"col-md-8 country-pop-description"})
for i in population:
  x= (i.text)
  y= x.split(' ')[7]
print ("The Current Population of "+country.upper+" today is: "+y)

  
  
