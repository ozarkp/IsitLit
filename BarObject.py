"""
Author: Liza 

Bar object. 
"""

from geopy.geocoders import Nominatim
	

class Bar:

	def __init__(self, name, long, lat):
		self._name = name
		self._long = long
		self._lat  = lat 
		self.count = 0


	def __str__(self):
		address = self.getAddressLocation()
		string = "%s, at %s has %d people in it right now" \
		% (self._name, address, self.count)
		return string


	#getter methods  
	def getCount(self):
		return self.count

	def getLong(self):
		return self._long

	def getLat(self):
		return self._lat

	def getAddressLocation(self):
		stringRep = str(self._long) + ", " + str(self._lat)
		print(stringRep)
		geolocator = Nominatim()
		location = geolocator.reverse(stringRep)
		return location.address


	#setter methods
	def addCount(self):
		self.count += 1


def main():
	bar = Bar("The Library", 35.9131478, -79.0570661)
	print(bar)

if __name__ == "__main__":
	main()




