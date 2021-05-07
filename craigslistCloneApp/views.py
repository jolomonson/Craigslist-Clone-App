import requests
from django.shortcuts import render
from requests.compat import quote_plus
from bs4 import BeautifulSoup

Base_Craigslist_URL = 'https://'
# Create your views here.
def home(request):
    return render(request, 'home.html')

def newSearch(request):
    search = request.POST.get('search')
    '''
    response = requests.get('https://.../{search|title}')
    data = response.text
    print(data)
    '''
    stuffForFrontEnd = {
        'search':search,

    }
    return render(request, 'myApp/newSearch.html', stuffForFrontEnd)
