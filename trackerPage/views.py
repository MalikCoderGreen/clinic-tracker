from django.shortcuts import render
import json
from django.http import HttpResponse
from requests import get
import ipinfo

def index(request): 
    return render(request, 'trackerPage/index.html')

def maps(request):
    
    
    # Use API with get function.
    my_ip = get('https://api.ipify.org').text
    access_token = '6d22498aabaf10'
    # Get lat and long.
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails(my_ip)
    
 
    # Send to template through context. 
    loc_context = {
        "latitude": details.latitude,
        "longitude": details.longitude
    }
    
 
    return render(request, 'trackerPage/maps.html', loc_context)


def faqs(request): 
    return render(request, 'trackerPage/faqs.html')


