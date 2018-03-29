import json
import urllib2
import datetime
import csv

def get_details(placeID): 
	link = 'https://maps.googleapis.com/maps/api/place/details/json?placeid='+placeID+'&key=AIzaSyDQ9TE3K2mpWdAEn63gqhsxvw_i206QdK4'
	data = json.load(urllib2.urlopen(link))
	return data

def fill_data(placeID, index):
	with open('C:\Users\JP\Desktop\Maps Project\stores.json') as json_file:  
		jsonData = json.load(json_file)
		
	
	placeDetails = get_details(placeID)
	phoneNum = placeDetails['result']['formatted_phone_number']
	
	hours = placeDetails['result']['opening_hours']['weekday_text']
	weekday = datetime.datetime.today().weekday()
	hours = hours[weekday]
	
	jsonData['features'][index]['properties']['hours'] = hours
	jsonData['features'][index]['properties']['phone'] = phoneNum
	
	with open('growler.csv', 'rb') as f:
		file = csv.reader(f, delimiter=',')
		rows = list(file)
		row = rows[index]
	f.close()	
	jsonData['features'][index]['properties']['beer'] = row	
	
	with open('C:\Users\JP\Desktop\Maps Project\stores.json', 'w') as json_file:
		json.dump(jsonData, json_file)
		

with open('C:\Users\JP\Desktop\Maps Project\locationID.json') as json_file:  
		breweryKeys = json.load(json_file)

for x in breweryKeys:
	placeID = x['id']
	index = breweryKeys.index(x)
	fill_data(placeID, index)