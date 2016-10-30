from geopy.geocoders import Nominatim
geolocator = Nominatim()
location = geolocator.geocode("159 E Franklin St Chapel Hill NC")
print(location.address)
print((location.latitude, location.longitude))
print(location.raw)


