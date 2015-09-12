import json, urllib, re
from urllib import urlencode
import googlemaps
import tempfile
import win32api
import win32print
start = raw_input("Start Address: ")
finish = raw_input("finish address: ")



url = 'http://maps.googleapis.com/maps/api/directions/json?%s' % urlencode((
			('origin', start),
			('destination', finish)
 ))
ur = urllib.urlopen(url)
result = json.load(ur)
filename = "output.txt"
with open(filename, "w") as output:
    for i in range (0, len (result['routes'][0]['legs'][0]['steps'])):
        s = (result['routes'][0]['legs'][0]['steps'][i]['html_instructions'])
        d = (result['routes'][0]['legs'][0]['steps'][i]['distance']['text'])
        l = (result['routes'][0]['legs'][0]['steps'][i]['duration']['text'])
        s = re.sub('<[A-Za-z\/][^>]*>', '', s)
        print s + d + l
        output.writelines(s + " " + d + "  " + l + '\n')
win32api.ShellExecute (
	0,
	"print",
	filename,
	'/d:"%s"' % win32print.GetDefaultPrinter (),
	'.',
	0
	)