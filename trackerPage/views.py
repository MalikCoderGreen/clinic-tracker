from django.shortcuts import render
import json
from django.http import HttpResponse
from requests import get
import ipinfo

def index(request): 
    return render(request, 'trackerPage/index.html')

# View to handle showing openstreetmap with user lat and long. 
def maps(request):
   
    # This will parse the IP to remove the colon and everything after it. 
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    

    # Remove everything after colon. 
    parsed_ip = ip[:ip.find(":")]


    # Use API with get function.
    #my_ip = get('https://api.ipify.org').text
    access_token = '6d22498aabaf10'
    # Get lat and long.
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails(parsed_ip)
    
 
    # Send to template through context. 
    loc_context = {
        "latitude": details.latitude,
        "longitude": details.longitude
    }
    
 
    return render(request, 'trackerPage/maps.html', loc_context)


def faqs(request): 
    return render(request, 'trackerPage/faqs.html')


