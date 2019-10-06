# Name: Laurence SanBoeuf, Arpan _
# Assignment title: Final Project
# Time to complete: ...
# Description:



# = These are notes related to the code
### = These are notes specifically related to our project; stuff that needs to be looked at




# -*- coding: utf-8 -*-
# Keep the line above when running script
# Tells python what encoding the string is stored in



###########################################################################



import requests
from bs4 import BeautifulSoup

country= str(input("Enter country name: "))
country=country.lower()

# Create url for the requested location through string concatenation
url = 'https://www.worldometers.info/world-population/'+country+'-population/'

# Send request to retrieve the web-page using the get() function from the requests library
# The page variable stores the response from the web-page
page = requests.get(url)

# Create a BeautifulSoup object with the response from the URL
# Access contents of the web-page using .content
# html_parser is used since our page is in HTML format
soup=BeautifulSoup(page.content,"html.parser")



population = soup.findAll("div", {"class":"col-md-8 country-pop-description"})
for i in population:
  x= (i.text)
  y= x.split(' ')[7]
print ("The Current Population of "+country.capitalize()+" today is: "+y)


  
  
