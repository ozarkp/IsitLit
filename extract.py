import twitter

api = twitter.Api("jfIgPfPsklkSviBmNzJMx9ZEr",
                "fwgolbpwaSPRo7yCcUvnpph0Bryg3FTKiGGsM8f72knATwToKC",
                "2683524229-A76OJz1zlNO6j8GFhoCxl9Pehd9sCjOe0IZHVXZ",
                "ukrQxOi45xlxOa2qzuYWknTtPQrrqbnscKvPDWDKFkbs0")


notHere = api.GetSearch(geocode= [35.9124271249157, -79.0574665465222, ".02mi"], count=100, since = "2016-10-28")

goodFellows = api.GetSearch(geocode= [35.9134575918367, -79.0552146122449, ".02mi"], count=100, since = "2016-10-28")

lindasBar = api.GetSearch(geocode= [35.9147155918367, -79.0519305306122, ".02mi"], count=100, since = "2016-10-28")

crunkelton = api.GetSearch(geocode= [35.9104271717172, -79.0630652020202, ".02mi"], count=100, since = "2016-10-28")

carolina = api.GetSearch(geocode= [35.9106269, -79.0627303, ".02mi"], count=100, since = "2016-10-28")

westEnd = api.GetSearch(geocode= [35.9106037878788, -79.0626115151515, ".02mi"], count=100, since = "2016-10-28")

zogsPool = api.GetSearch(geocode= [35.9144793265306, -79.0528503877551, ".02mi"], count=100, since = "2016-10-28")

tobaccoRoad = api.GetSearch(geocode= [35.907387, -79.0225825, ".02mi"], count=100, since = "2016-10-28")

fourCorners = api.GetSearch(geocode= [35.9142522, -79.0533615, ".02mi"], count=100, since = "2016-10-28")

library = api.GetSearch(geocode= [35.9132001632653, -79.055410755102, ".02mi"], count=100, since = "2016-10-28")

print("He's Not Here: \n\n",notHere,goodFellows,lindasBar,crunkelton,carolina,westEnd,zogsPool,tobaccoRoad,fourCorners,library)