# import libraries
import urllib2
import json
import csv
import re
from bs4 import BeautifulSoup

with open('growler.csv', 'wb') as f:
	writer = csv.writer(f)

	print 'Philips'
	# specify the url
	quote_page = 'https://phillipsbeer.com/growlers/'
	# query the website and return the html to the variable page
	page = urllib2.urlopen(quote_page)
	# parse the html using beautiful soup and store in variable soup
	soup = BeautifulSoup(page, 'html.parser')
	# Take out the <div> of name and get its value
	beers = soup.find_all('span', attrs={'class': 'beer-name'})
	beer_count = len(beers)
	beer_names = []
	for x in range(0, beer_count):
		name_box = beers[x]
		name = ' '+name_box.text.strip() # strip() is used to remove starting and trailing
		beer_names.append(name)
	writer.writerow(beer_names)

	print 'Vancouver Island Brewery'
	writer.writerow(['Current taps not listed'])
	
	print 'Driftwood'
	quote_page = 'https://driftwoodbeer.com/contact/'
	page = urllib2.urlopen(quote_page)
	soup = BeautifulSoup(page, 'html.parser')
	beer_list = soup.find('ul', attrs={'class': 'growler-fill'})
	beer_list = beer_list.find_all('li')
	beer_names = []
	beer_count = len(beer_list) -1
	for x in range(0, beer_count):
		name_box = beer_list[x]
		name = ' '+name_box.text.strip().strip(' $1234')
		beer_names.append(name)
	writer.writerow(beer_names)
	
	print 'Hoyne'
	writer.writerow(['Current taps not listed'])
	
	print 'Lighthouse'
	quote_page = 'http://www.lighthousebrewing.com/'
	page = urllib2.urlopen(quote_page)
	soup = BeautifulSoup(page, 'html.parser')
	beers = soup.find_all('ul', attrs={'class': 'growler-list'})
	beers = beers[0].find_all('li')
	beer_count = len(beers) - 1
	beer_names = []
	for x in range(0, beer_count):
		name_box = beers[x]
		name = ' '+name_box.text.strip().strip('.%123456789') # strip() is used to remove starting and trailing
		beer_names.append(name)
	writer.writerow(beer_names)
	
	print 'TWA Dogs'
	quote_page = 'https://victoriacaledonian.com/lounge/'
	page = urllib2.urlopen(quote_page)
	soup = BeautifulSoup(page, 'html.parser')
	beers = soup.find('section', attrs={'class': 'section-ontap'})
	beers = beers.find_all('a')
	beer_count = len(beers) - 1
	beer_names = []
	for x in range(0, beer_count):
		name_box = beers[x]
		name = ' '+name_box.text.strip().replace(u"\u2019", "'") # strip() is used to remove starting and trailing
		beer_names.append(name)
	writer.writerow(beer_names)
	
	print 'Sooke OceanSide Brewery'
	quote_page = 'http://www.sookeoceansidebrewery.com/'
	page = urllib2.urlopen(quote_page)
	soup = BeautifulSoup(page, 'html.parser')
	beers = soup.find('ul', attrs={'class': 'folder-child'})
	beers = beers.find_all('li')
	beer_count = len(beers)
	beer_names = []
	for x in range(0, beer_count):
		name_box = beers[x]
		name = ' '+name_box.text.strip()
		beer_names.append(name)
	writer.writerow(beer_names)
	
	print 'Sooke Brewery'
	quote_page = 'http://www.sookebrewing.com/#contact'
	page = urllib2.urlopen(quote_page)
	soup = BeautifulSoup(page, 'html.parser')
	beers = soup.find_all('div', attrs={'class': 'fusion-one-half'})
	beer_count = len(beers)
	beer_names = []
	for x in range(2, beer_count):
		beer = beers[x].find('h3')
		name = ' '+beer.text.strip()
		beer_names.append(name)
	writer.writerow(beer_names)
	
	print 'Category 12'
	writer.writerow(['Current taps not listed'])
	
	print 'Canoe'
	quote_page = 'https://www.canoebrewpub.com/beer/'
	page = urllib2.urlopen(quote_page)
	soup = BeautifulSoup(page, 'html.parser')
	beers = soup.find_all('div', attrs={'id': 'beer-menu-core'})
	beers = beers[0].find_all('li')
	beer_count = len(beers)
	beer_names = []
	for x in range(0, beer_count):
		name = ' '+beers[x].text.strip()
		beer_names.append(name)
	beers = soup.find_all('div', attrs={'id': 'beer-menu-seasonal'})
	beers = beers[0].find_all('li')
	beer_count = len(beers)
	for x in range(0, beer_count):
		name = ' '+beers[x].text.strip()
		beer_names.append(name)
	beers = soup.find_all('div', attrs={'id': 'beer-menu-signature'})
	beers = beers[0].find_all('li')
	beer_count = len(beers)
	for x in range(0, beer_count):
		name = ' '+beers[x].text.strip()
		beer_names.append(name)
	beers = soup.find_all('div', attrs={'id': 'beer-menu-windward-series'})
	beers = beers[0].find_all('li')
	beer_count = len(beers)
	for x in range(0, beer_count):
		name = ' '+beers[x].text.strip()
		beer_names.append(name)
	writer.writerow(beer_names)

	print 'Swans'
	writer.writerow(['Current taps not listed'])
	
	print 'Spinnackers'
	quote_page = 'http://www.spinnakers.com/beer/?filter=on-tap'
	page = urllib2.urlopen(quote_page)
	soup = BeautifulSoup(page, 'html.parser')
	beers = soup.find_all('div', attrs={'class': 'drinkblocks'})
	beer_count = len(beers)
	beer_names = []
	for x in range(0, beer_count):
		name_box = beers[x]
		name = ' '+name_box.text.strip().replace(u"\u2018", "'").replace(u"\u2019", "'")
		beer_names.append(name)
	writer.writerow(beer_names)
	
	print 'Moon Under Water'
	quote_page = 'http://www.moonunderwater.ca/ourbeer/?category=Currently+Available'
	page = urllib2.urlopen(quote_page)
	soup = BeautifulSoup(page, 'html.parser')
	beers = soup.find_all('h1', attrs={'data-content-field': 'title'})
	beer_count = len(beers)
	beer_names = []
	for x in range(0, beer_count):
		name_box = beers[x]
		name = ' '+name_box.text.strip().replace(u"\u2018", "'").replace(u"\u2019", "'")
		beer_names.append(name)
	writer.writerow(beer_names)
	
	print '4 mile'
	writer.writerow(['Current taps not listed'])
	
	print 'Axe & Barrel'
	quote_page = 'http://www.axeandbarrel.com/drinks/'
	page = urllib2.urlopen(quote_page)
	soup = BeautifulSoup(page, 'html.parser')
	beers = soup.find_all('h3', attrs={'class': 'p1'})
	beer_count = len(beers)
	beer_names = []
	for x in range(0, beer_count):
		name_box = beers[x]
		name = name_box.text.strip().replace(u"\u2018", "'").replace(u"\u2019", "'")
		name = ' '+name.split(":")[0]
		beer_names.append(name)
	writer.writerow(beer_names)

f.close()
	


