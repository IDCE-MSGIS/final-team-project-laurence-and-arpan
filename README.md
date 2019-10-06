## Final Project: Script 1
### Web-scraping Weather Forecast Information with Python
## Laurence SanBoeuf, Arpan Parashar
## Final Project
## Time to complete: 1 Hour

## Script 1:
For the first script, we are given an existing script gave a weather forecast for Worcester, Ma and edit it to be able to input any latitude and longitude and get back a weather forecast for that area. Lines of code needed to be added to take the latitude and longitude as inputs. The code then takes that input, puts it into a url and uses requests.get to access the website that relates to our coordinates. It then uses BeautifulSoup to access the content on the page. It uses soup.findAll() function to pull out the data that we want and then create a list using a “for” loop, .text, and .append. We then use day.replace() to replace certain words and add spaces. Although, adding spaces before some words like ‘showers’ in ‘ChanceShowers’ caused problem with alignment when ‘Shower’ was printed as first word of a sentence ( Showers likely high, Showers low). We also used day.upper() to capitalize the output and to make the data more presentable.


## Final Project: Script 2(
## Our function takes Country names as input and will tell you the current population of that country according to www.worldometers.info


## Final Project: Documentation
## Script 2:
For our second script, we took the lab on web-scraping and used this to create a function that allows users to input a country name and receive the current population back. We took our data from wordometers.info.

The code takes the country name as input, uses country.lower() to deal with input variation. The name is then put into the URL which has a temporary variable in the place of the country name. requests.get() accessed the website and BeautifulSoup allows access to the page content. Soup.findAll() pulls a paragraph from the site that has data on the country population. X.split(), splits the paragraph and an index value pulls the string that has the population value and a print function returns the value back to the user.
While trying to write this script we ran into a few issues. First, we had a problem where the site that we chose would not allow us to scrape the data. In the script, the data was visible and looked as though it was text, but it would not allow us to call it. The output would include headers and accompanying script around the data, but the data itself was missing. The TA, Priyanka, and Stack Overflow pointed out that many sites put their data in a form that cannot be scraped so we chose another site.
Another problem we had was related to trying to index the paragraph that was pulled from the site. The entire paragraph was at index [0]. So we found the .split() function, which basically makes an index out of the string, and you can input how you want it to split. 
In the paragraph, the population value came after a comma, so we split by commas. We got the population value back, but we were also getting everything up to the next comma. We discussed how to split again after the population value but every country would have a different number as the final integer in the population value, and the length of the population values were different by country as well, India has a population value with a length of 10 digits while Namibia has a population value with a length of 7 digits. So, we split by spaces instead of commas to work around this. 

There were also some issues that were not resolved, related to the naming convention for the countries on the worldometers.info. Most countries have a one-word name, and this is how it shows in the URL, but some countries have two or more words in their name, New Zealand, Cote d’Ivoire, Sierra Leone, and the URL has a “-“ in between each word in the name. Some country names are less standard. United States is listed as “US” in the URL. Democratic Republic of Congo is listed as DR Congo, and Czech Republic is listed as Czechia. Our current function must take the input exactly how it appears in the URL. These issues could be addressed by creating some sort of dictionary that has pairs of names: US, United States; Czech Republic, Czechia. When the user input a country name, the function would search the list for the name and use then find the proper name for each country before running the rest of the code. There is also an option to make a drop-down list, where you could choose the country instead of typing it in, completely removing any naming conflicts. 

