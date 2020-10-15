import json
from time import sleep
import requests
from bs4 import BeautifulSoup

pageexists = True
pagenumber = 1
json_reviews = []
#Extract reviews from all pages based on next button

while pageexists:
    url = 'https://www.trustpilot.com/review/marketfinance.com'
    if  pagenumber != 1:
        url = url+'?page='+str(pagenumber)
    pagenumber = pagenumber + 1
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')
    formatted_text = soup.prettify()
    nextpagebutton = soup.find('a', class_='next-page')
    if nextpagebutton == None:
        pageexists = False
#Get script tags
    script_tags = soup.findAll('script', {'data-initial-state': 'review-info'})
    for x in script_tags:
        jasontext = x.contents[0]

        oJson = json.loads(jasontext)
       #print(oJson['stars'])
        json_reviews.append(oJson)

   # sleep(5)
print(len(json_reviews))
#Write to Json file
with open('data.json', 'w') as outfile:
    json.dump(json_reviews, outfile)
