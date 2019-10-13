
## install geopy using pip command
from geopy.geocoders import Nominatim
import certifi
import ssl

ctx = ssl.create_default_context(cafile=certifi.where())
geolocator = Nominatim(user_agent="oneshellß", ssl_context=ctx)

location = geolocator.reverse("13.737668, 79.995887")
print(location.raw)
