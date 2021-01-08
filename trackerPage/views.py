from django.shortcuts import render
from ipware import get_client_ip
from django.http import HttpResponse

# Create your views here.
def index(request):
    ip = ''
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    print("My ip address: {}\n".format(ip))

    #return HttpResponse("Welcome Home<br>You are visiting from: {}".format(ip)) 
    return render(request, 'trackerPage/index.html')


def faqs(request): 
    return render(request, 'trackerPage/faqs.html')


