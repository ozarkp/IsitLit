import csv

headers = {'Attraction' : ['Latitude', 'Longitude', 'Tweets',
                           'Is It Lit?','Check It Out!']}
#Lit key:
#mild: 0-4, hot:5-9, sizzling: 10 and up

attraction ={'Gotham': [35.911586877551, -79.0596412244898, 0, 'mild',
                    'http://www.facebook.com/pages/Gotham/111560098884075'], 
        'Townhall Grill': [35.91120765, -79.0596764795248, 1, 'mild',
                           'http://www.thetownhallgrill.com/'], 
        'Caffe Driade': [35.9257446, -79.0379503931717, 0, 'mild',
                         'http://www.caffedriade.com/'], 
        'The Library': [35.913721, -79.055659, 9, 'hot',
                        'http://www.facebook.com/TheLibraryCH/'], 
        'La Residence': [35.9136319, -79.0577673, 0, 'mild',
                         'http://www.laresidencedining.com/'], 
        'Tobacco Road Sports Cafe': [35.907387, -79.0225825, 0, 'mild',
                                     'http://www.tobaccoroadsportscafe.com/'], 
        'West End Wine Bar': [35.9106037878788, -79.0626115151515, 3, 'mild',
                              'http://www.westendwinebar.com/'], 
        'Carolina Brewery': [35.9106269, -79.0627303, 3, 'mild',
                             'http://www.carolinabrewery.com/'], 
        'Dead Mule Club': [35.91120765, -79.0596764795248, 0, 'mild',
                           'http://www.visitnc.com/listing/the-dead-mule-club'], 
        'Nightlight Bar & Club': [35.9113008171748, -79.0632202883517, 0, 'mild',
                                  'http://www.nightlightclub.com/'], 
        'The Crunkelton': [35.9104271717172, -79.0630652020202, 0, 'mild',
                           'http://www.thecrunkleton.com/'], 
        'DSI Comedy Theater': [35.911586877551, -79.0596412244898, 2, 'mild',
                               'http://www.dsicomedytheater.com/'], 
        'Zogs Pool': [35.9144793265306, -79.0528503877551, 0, 'mild',
                      'http://www.zogsartbar.com/'], 
        'Doyel\'s Sports Bar': [35.945659, -78.9968429, 0, 'mild',
                                'http://www.facebook.com/Doyles-Sports-Bar-283703518284/'], 
        'Linda\'s Bar & Grill': [35.9147155918367, -79.0519305306122, 0, 'mild',
                                 'http://www.lindas-bar.com/'], 
        'Goodfellows': [35.9134575918367, -79.0552146122449, 1, 'mild',
                        'http://www.goodfellowsbar.com/'], 
        'The Strowd': [35.9140624, -79.053859, 5, 'hot',
                       'http://www.thestrowd.com/'], 
        'Bowbarr': [35.9108786, -79.0662031, 0, 'mild',
                    'http://www.facebook.com/bowbarr/'], 
        'Local 506': [35.9102084, -79.0638329, 13, 'sizzling',
                      'http://www.local506.com/'], 
        'Four Corners Grille': [35.9142522, -79.0533615, 0, 'mild',
                                'http://www.fourcornersgrille.com/'], 
        'He\'s Not Here': [35.9124271249157, -79.0574665465222, 0, 'mild',
                           'http://www.hesnotherenc.com/']}



with open('Attractions.csv', 'w', newline='') as f:
    c = csv.writer(f)

    
    for key, value in headers.items():
        c.writerow([key] + value)
        
    for key, value in attraction.items():
        c.writerow([key] + value)
    

