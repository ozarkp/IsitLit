import twitter
import random
import csv

def extract():

	api = twitter.Api("jfIgPfPsklkSviBmNzJMx9ZEr",
	                "fwgolbpwaSPRo7yCcUvnpph0Bryg3FTKiGGsM8f72knATwToKC",
	                "2683524229-A76OJz1zlNO6j8GFhoCxl9Pehd9sCjOe0IZHVXZ",
	                "ukrQxOi45xlxOa2qzuYWknTtPQrrqbnscKvPDWDKFkbs0")

	doyels = api.GetSearch(geocode= [35.945659, -78.9968429, ".02mi"], count=100, since = "2015-10-01", until = "2016-10-29")

	bowbarr = api.GetSearch(geocode= [35.9108786, -79.0662031, ".02mi"], count=100, since = "2015-10-01", until = "2016-10-29")

	driade = api.GetSearch(geocode= [35.9257446, -79.0379503931717, ".02mi"], count=100, since = "2015-10-01", until = "2016-10-29")

	residence = api.GetSearch(geocode= [35.9136319, -79.0577673, ".02mi"], count=100, since = "2015-10-01", until = "2016-10-29")

	town = api.GetSearch(geocode= [35.881897752574, -79.0659107894652, ".02mi"], count=100, since = "2015-10-01", until = "2016-10-29")

	mule = api.GetSearch(geocode= [35.91120765, -79.0596764795248, ".02mi"], count=100, since = "2015-10-01", until = "2016-10-29")

	comedy = api.GetSearch(geocode= [35.9105855, -79.0628674, ".02mi"], count=100, since = "2015-10-01", until = "2016-10-29")

	local = api.GetSearch(geocode= [35.9102084, -79.0638329, ".02mi"], count=100, since = "2015-10-01", until = "2016-10-29")

	nightlight = api.GetSearch(geocode= [35.9113008171748, -79.0632202883517, ".02mi"], count=100, since = "2015-10-01", until = "2016-10-29")

	strowd = api.GetSearch(geocode= [35.9140624, -79.053859, ".02mi"], count=100, since = "2015-10-01", until = "2016-10-29")

	gotham = api.GetSearch(geocode= [35.911586877551, -79.0596412244898, ".02mi"], count=100, since = "2015-10-01", until = "2016-10-29")

	spankys = api.GetSearch(geocode= [35.913721, -79.055659, ".02mi"], count=100, since = "2015-10-01", until = "2016-10-29")

	notHere = api.GetSearch(geocode= [35.9124271249157, -79.0574665465222, ".02mi"], count=100, since = "2016-10-01", until = "2016-10-29")

	goodFellows = api.GetSearch(geocode= [35.9134575918367, -79.0552146122449, ".02mi"], count=100, since = "2016-10-01", until = "2016-10-29")

	lindasBar = api.GetSearch(geocode= [35.9147155918367, -79.0519305306122, ".02mi"], count=100, since = "2016-10-01", until = "2016-10-29")

	crunkelton = api.GetSearch(geocode= [35.9104271717172, -79.0630652020202, ".02mi"], count=100, since = "2016-10-01", until = "2016-10-29")

	carolina = api.GetSearch(geocode= [35.9106269, -79.0627303, ".02mi"], count=100, since = "2016-10-01", until = "2016-10-29")

	westEnd = api.GetSearch(geocode= [35.9106037878788, -79.0626115151515, ".02mi"], count=100, since = "2016-10-01", until = "2016-10-29")

	zogsPool = api.GetSearch(geocode= [35.9144793265306, -79.0528503877551, ".02mi"], count=100, since = "2016-10-01", until = "2016-10-29")

	tobaccoRoad = api.GetSearch(geocode= [35.907387, -79.0225825, ".02mi"], count=100, since = "2016-10-01", until = "2016-10-29")

	fourCorners = api.GetSearch(geocode= [35.9142522, -79.0533615, ".02mi"], count=100, since = "2016-10-01", until = "2016-10-29")

	library = api.GetSearch(geocode= [35.9132001632653, -79.055410755102, ".02mi"], count=100, since = "2016-10-01", until = "2016-10-29")


	#Create dictionary and variables to track the number of tweets
	d = {}
	doyelsTweets = 0
	bowbarrTweets = 0
	driadeTweets = 0
	residenceTweets = 0
	townTweets = 0
	muleTweets = 0
	comedyTweets = 0
	gothamTweets = 0
	localTweets = 0
	nightlightTweets = 0
	strowdTweets = 0
	libTweets = 0
	notHereTweets = 0
	goodFellowsTweets = 0
	lindasBarTweets = 0
	crunkeltonTweets = 0
	carolinaTweets = 0
	westEndTweets = 0
	zogsPoolTweets = 0
	tobaccoRoadTweets = 0
	fourCornersTweets = 0


	#Count the number of statuses for each attraction, removing tweets about hiring to show tweets from customers
	for status in doyels:

		if "job" not in status.text and "hiring" not in status.text and "hire" not in status.text and "work" not in status.text:

			doyelsTweets += 1

	d["Doyel's Sports Bar"] = [35.945659, -78.9968429, doyelsTweets]

	for status in bowbarr:

		if "job" not in status.text and "hiring" not in status.text and "hire" not in status.text and "work" not in status.text:

			bowbarrTweets += 1

	d["Bowbarr"] = [35.9108786, -79.0662031, bowbarrTweets]

	for status in driade:

		if "job" not in status.text and "hiring" not in status.text and "hire" not in status.text and "work" not in status.text:

			driadeTweets += 1

	d["Caffe Driade"] = [35.9257446, -79.0379503931717, driadeTweets]

	for status in residence:

		if "job" not in status.text and "hiring" not in status.text and "hire" not in status.text and "work" not in status.text:

			residenceTweets += 1

	d["La Residence"] = [35.9136319, -79.0577673, residenceTweets] 

	for status in town:

		if "job" not in status.text and "hiring" not in status.text and "hire" not in status.text and "work" not in status.text:

			townTweets += 1

	d["Townhall Grill"] = [35.91120765, -79.0596764795248, townTweets]

	for status in mule:

		if "job" not in status.text and "hiring" not in status.text and "hire" not in status.text and "work" not in status.text:

			muleTweets += 1

	d["Dead Mule Club"] = [35.91120765, -79.0596764795248, muleTweets]

	for status in comedy:

		if "job" not in status.text and "hiring" not in status.text and "hire" not in status.text and "work" not in status.text:

			comedyTweets += 1

	d["DSI Comedy Theater"] = [35.911586877551, -79.0596412244898, comedyTweets]

	for status in gotham:

		if "job" not in status.text and "hiring" not in status.text and "hire" not in status.text and "work" not in status.text:

			gothamTweets += 1

	d["Gotham"] = [35.911586877551, -79.0596412244898, gothamTweets]

	for status in local:

		if "job" not in status.text and "hiring" not in status.text and "hire" not in status.text and "work" not in status.text:

			localTweets += 1

	d["Local 506"] = [35.9102084, -79.0638329, localTweets]

	for status in nightlight:

		if "job" not in status.text and "hiring" not in status.text and "hire" not in status.text and "work" not in status.text:

			nightlightTweets += 1

	d["Nightlight Bar & Club"] = [35.9113008171748, -79.0632202883517, nightlightTweets]

	for status in strowd:

		if "job" not in status.text and "hiring" not in status.text and "hire" not in status.text and "work" not in status.text:

			strowdTweets += 1

	d["The Strowd"] = [35.9140624, -79.053859, strowdTweets]

	for status in library:

		if "job" not in status.text and "hiring" not in status.text and "hire" not in status.text and "work" not in status.text:

			libTweets += 1
			
	d["The Library"] = [35.913721, -79.055659,libTweets]


	for status in notHere:

		if "job" not in status.text and "hiring" not in status.text and "hire" not in status.text and "work" not in status.text:

			notHereTweets += 1

	d["He's Not Here"] = [35.9124271249157, -79.0574665465222, notHereTweets]


	for status in goodFellows:

		if "job" not in status.text and "hiring" not in status.text and "hire" not in status.text and "work" not in status.text:

			goodFellowsTweets += 1

	d["Goodfellows"] = [35.9134575918367, -79.0552146122449, goodFellowsTweets]


	for status in lindasBar:

		if "job" not in status.text and "hiring" not in status.text and "hire" not in status.text and "work" not in status.text:

			lindasBarTweets += 1

	d["Linda's Bar & Grill"] = [35.9147155918367, -79.0519305306122, lindasBarTweets]


	for status in crunkelton:

		if "job" not in status.text and "hiring" not in status.text and "hire" not in status.text and "work" not in status.text:

			crunkeltonTweets += 1

	d["The Crunkelton"] = [35.9104271717172, -79.0630652020202, crunkeltonTweets]


	for status in carolina:

		if "job" not in status.text and "hiring" not in status.text and "hire" not in status.text and "work" not in status.text:

			carolinaTweets += 1

	d["Carolina Brewery"] = [35.9106269, -79.0627303, carolinaTweets]


	for status in westEnd:

		if "job" not in status.text and "hiring" not in status.text and "hire" not in status.text and "work" not in status.text:

			westEndTweets += 1

	d["West End Wine Bar"] = [35.9106037878788, -79.0626115151515, westEndTweets]


	for status in zogsPool:

		if "job" not in status.text and "hiring" not in status.text and "hire" not in status.text and "work" not in status.text:

			zogsPoolTweets += 1

	d["Zogs Pool"] = [35.9144793265306, -79.0528503877551, zogsPoolTweets]


	for status in tobaccoRoad:

		if "job" not in status.text and "hiring" not in status.text and "hire" not in status.text and "work" not in status.text:

			tobaccoRoadTweets += 1

	d["Tobacco Road Sports Cafe"] = [35.907387, -79.0225825, tobaccoRoadTweets]


	for status in fourCorners:

		if "job" not in status.text and "hiring" not in status.text and "hire" not in status.text and "work" not in status.text:
				
			fourCornersTweets += 1

	d["Four Corners Grille"] = [35.9142522, -79.0533615, fourCornersTweets]


	return d

	headers = {'Attraction' : ['Latitude', 'Longitude', 'tweets']}

	
	with open('hotspots.csv', 'w', newline='') as f:

		c = csv.writer(f)
		for key, value in headers.items():

			c.writerow([key] + value)
			
		for key, value in d.items():

			c.writerow([key] + value)


if __name__ == '__main__':

	print(extract())