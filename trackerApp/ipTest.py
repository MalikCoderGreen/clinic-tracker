import socket
from requests import get
import ipinfo



my_ip = get('https://api.ipify.org').text
print('My public IP address is: {}'.format(my_ip))
access_token = '6d22498aabaf10'
handler = ipinfo.getHandler(access_token)
details = handler.getDetails(my_ip)

print(details.city)
print(details.loc)