import requests
from django.shortcuts import render
from requests.compat import quote_plus
from bs4 import BeautifulSoup
from . import models
BaseCraigslistURL = 'https://www.searchcraigslist.org/'
# Create your views here.
def home(request):
    return render(request, 'home.html')

def newSearch(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    finalURL = BaseCraigslistURL.format(quote_plus(search))
    response = requests.get(finalURL)
    data = response.text
    print(data)
    stuffForFrontEnd = {
        'search':search,
    }
   
    return render(request, 'myApp/newSearch.html', stuffForFrontEnd)
