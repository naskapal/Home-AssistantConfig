from lxml import html
import requests
import datetime
import sys
from time import gmtime, strftime

now = datetime.datetime.now()
month = strftime("%m", gmtime())
day = strftime("%d", gmtime())
# YN921 YVO YUL
page = requests.get('https://www.airportia.com/widgets/flight/YN921/index.html')
tree = html.fromstring(page.content)
#This will create a list of buyers:
arrival = [x.text for x in tree.xpath('//td[@class="Arrival"]')]
sarrival = [x.text for x in tree.xpath('//td[@class="Scheduled-Arrival"]')]
departure = [x.text for x in tree.xpath('//td[@class="Departure"]')]
sdeparture = [x.text for x in tree.xpath('//td[@class="Scheduled-Departure"]')]
#buyers = [x.text if x.text else '1' for x in buyers1]
#This will create a list of prices
prices = tree.xpath('//td[@class="Date"]/a/text()')
from_city = tree.xpath('//td[@class="From"]/a/text()')
to_city = tree.xpath('//td[@class="To"]/a/text()')
#print (buyers)
get_indexes = lambda prices, xs: [i for (y, i) in zip(xs, range(len(xs))) if prices == y]
#print ('indexes', get_indexes(day+"/"+month,prices))
for member in get_indexes(day+"/"+month,prices):
  if to_city[member]=="YVO" and from_city[member]=="YUL":
    print (str(arrival[member])+'_'+str(sarrival[member])+'_'+str(departure[member])+'_'+str(sdeparture[member]))
    #print ('from', from_city[member])
    #print ('to', to_city[member])
#print ('Prices: ', prices)
#print ('From: ',from_city)
#print('To: ',to_city)
