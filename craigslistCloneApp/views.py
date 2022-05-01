import requests
from django.shortcuts import render
from requests.compat import quote_plus
from bs4 import BeautifulSoup
from . import models
#Note: Use local city's address
BASE_CRAIGSLIST_URL = "https://losangeles.craigslist.org/search/sss?query={}"
# Create your views here.
def home(request):
    return render(request, 'base.html')

def new_search(request):
    search = request.POST.get('search')
    #models.Search.objects.create(search=search)
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
    }
    finalURL = BASE_CRAIGSLIST_URL.format(quote_plus(search))
    print(finalURL)
    response = requests.get(finalURL, headers=headers)
    data = response.text
    #print(data)
    #Web Scraping
    soup = BeautifulSoup(data, features='html.parser')
    post_listings = soup.find_all('li', {'class':'result-row'})
    #print(post_listings)
    post_title = post_listings[0].find(class_='result-title').text
    post_url = post_listings[0].find('a').get('href')
    post_price = post_listings[0].find(class_='result-price').text
    print(post_title)
    print(post_url)
    print(post_price) 
    stuffForFrontEnd = {
        'search':search,
        #'final_postings':final_postings
    }
   
    return render(request, 'myApp/new-search.html', stuffForFrontEnd)
