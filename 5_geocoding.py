# Geocoding

# Determine the geocoordinates of these famous Chicago landmarks:
#
# United Center
# Millenium Park
# Sears Tower
# Young Memorial Building
#
# You can:
# - web: http://maps.google.com combined with the "What's Here?" trick
# - webservice: https://developers.google.com/maps/documentation/geocoding/#JSON

from os import system
import json
from urllib.request import urlopen

url = "https://maps.googleapis.com/maps/api/geocode/json?address=Millenium+Park,+Chicago,+IL"
data = urlopen(url).read().decode("utf8")
# print(data)
result = json.loads(data)

longitude = result['results'][0]['geometry']['location']['lng']
print("The longitude is", longitude)





