import csv

headers = {'Bar' : ['Latitude', 'Longitude']}

bars = {'Linda’s Bar & Grill' : [35.9147155918367, -79.0519305306122],
        'The Library' : [35.9132001632653, -79.055410755102],
        'Goodfellows' : [35.9134575918367, -79.0552146122449],
        'He’s Not Here' : [35.9124271249157, -79.0574665465222], 
        'The Crunkleton' : [35.9104271717172, -79.0630652020202], 
        'Carolina Brewery' : [35.9106269, -79.0627303],  
        'Tobacco Road Sports Cafe' : [35.907387, -79.0225825], 
        'Four Corners Grille' : [35.9142522, -79.0533615],  
        'West End Wine Bar' : [35.9106037878788, -79.0626115151515], 
        'Zogs Pool' : [35.9144793265306, -79.0528503877551]}



with open('Bars.csv', 'w', newline='') as f:
    c = csv.writer(f)

    
    for key, value in headers.items():
        c.writerow([key] + value)
        
    for key, value in bars.items():
        c.writerow([key] + value)
    
