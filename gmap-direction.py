import json, urllib, re
from urllib import urlencode
import googlemaps
start = "" #add address, State, Country as shown
finish = "" #add address, State, Country as shown

url = 'http://maps.googleapis.com/maps/api/directions/json?%s' % urlencode((
			('origin', start),
			('destination', finish)
 ))
ur = urllib.urlopen(url)
result = json.load(ur)

with open("output.txt", "w") as output:
    for i in range (0, len (result['routes'][0]['legs'][0]['steps'])):
        s = (result['routes'][0]['legs'][0]['steps'][i]['html_instructions'])
        d = (result['routes'][0]['legs'][0]['steps'][i]['distance']['text'])
        l = (result['routes'][0]['legs'][0]['steps'][i]['duration']['text'])
        print s + d + l
        output.writelines(s + " " + d + " " + l + '\n')