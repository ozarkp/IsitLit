import csv

headers = {'Attraction' : ['Latitude', 'Longitude', 'tweets']}

attractions = {'Gotham': [35.911586877551, -79.0596412244898, 0], 
        'Townhall Grill': [35.91120765, -79.0596764795248, 1], 
        'Caffe Driade': [35.9257446, -79.0379503931717, 0], 
        'The Library': [35.913721, -79.055659, 9], 
        'La Residence': [35.9136319, -79.0577673, 0], 
        'Tobacco Road Sports Cafe': [35.907387, -79.0225825, 0], 
        'West End Wine Bar': [35.9106037878788, -79.0626115151515, 3], 
        'Carolina Brewery': [35.9106269, -79.0627303, 3], 
        'Dead Mule Club': [35.91120765, -79.0596764795248, 0], 
        'Nightlight Bar & Club': [35.9113008171748, -79.0632202883517, 0], 
        'The Crunkelton': [35.9104271717172, -79.0630652020202, 0], 
        'DSI Comedy Theater': [35.911586877551, -79.0596412244898, 2], 
        'Zogs Pool': [35.9144793265306, -79.0528503877551, 0], 
        "Doyel\'s Sports Bar": [35.945659, -78.9968429, 0], 
        "Linda\'s Bar & Grill": [35.9147155918367, -79.0519305306122, 0], 
        'Goodfellows': [35.9134575918367, -79.0552146122449, 1], 
        'The Strowd': [35.9140624, -79.053859, 5], 
        'Bowbarr': [35.9108786, -79.0662031, 0], 
        'Local 506': [35.9102084, -79.0638329, 13], 
        'Four Corners Grille': [35.9142522, -79.0533615, 0], 
        "He\'s Not Here": [35.9124271249157, -79.0574665465222, 0]}



with open('hotspots.csv', 'w', newline='') as f:
    c = csv.writer(f)

    
    for key, value in headers.items():
        c.writerow([key] + value)
        
    for key, value in attractions.items():
        c.writerow([key] + value)
    

