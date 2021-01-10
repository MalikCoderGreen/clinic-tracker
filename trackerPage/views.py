from django.shortcuts import render
#from ipware import get_client_ip
from django.http import HttpResponse
from requests import get
import ipinfo

# Create your views here.


def index(request): 
    return render(request, 'trackerPage/index.html')

# Update**, I have the lat and long, need to find a way to pass it to maps.html for use.
def maps(request):
    # Code to get public ip address using API from ipify.org.
    my_ip = get('https://api.ipify.org').text
    print('My public IP address is: {}'.format(my_ip))
    access_token = '6d22498aabaf10'
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails(my_ip)
    user_loc = (details.latitude, details.longitude)
    """
    ip = ''
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    print("My ip address: {}\n".format(ip))
    """
    mapbox_access_token = 'pk.my_mapbox_access_token'
    loc_context = {
        'latitude': details.latitude,
        'longitude': details.longitude
    }
 
    return render(request, 'trackerPage/maps.html', {'loc_context': loc_context })


def faqs(request): 
    return render(request, 'trackerPage/faqs.html')


