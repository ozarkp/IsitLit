from geopy.geocoders import Nominatim
geolocator = Nominatim()
location = geolocator.geocode("105 W Main St Chapel Hill NC")
print(location.address)
print((location.latitude, location.longitude))
print(location.raw)


