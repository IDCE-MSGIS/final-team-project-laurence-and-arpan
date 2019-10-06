# Name: Laurence SanBoeuf, Arpan Parashar
# Assignment title: Final Project(Web-scraping current population for an entered country name)
# Time to complete: 4 Hours
# Description: Our function takes Country names as input and will tell you the current population of that country according to www.worldometers.info


# -*- coding: utf-8 -*-
# Keep the line above when running script
# Tells python what encoding the string is stored in


#imports Python libraries
import requests
from bs4 import BeautifulSoup 

country= str(input("Enter country name: "))                 #Asks the user to input country name 
country=country.lower()                                     #Converts country name to lower case to make it acceptable in the website url

# Create url for the requested location through string concatenation
url = 'https://www.worldometers.info/world-population/'+country+'-population/'

# Send request to retrieve the web-page using the get() function from the requests library
# The page variable stores the response from the web-page
page = requests.get(url)

# Create a BeautifulSoup object with the response from the URL
# Access contents of the web-page using .content
# html_parser is used since our page is in HTML format
soup=BeautifulSoup(page.content,"html.parser")


population = soup.findAll("div", {"class":"col-md-8 country-pop-description"})  #This line scraps out a paragraph containing population data from the website
for i in population:                                                            
  x= (i.text)                                                                   #Extracts text information from mixed data
  y= x.split(' ')[7]                                                            #This line split out code, split by " 's"(spaces) and then call back the 7th spot.
print ("The Current Population of "+country.capitalize()+" is: "+y)       #Returns population value with capitalized first letter of country name


  
  
