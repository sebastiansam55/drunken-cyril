import json
import sys
from urllib import unquote
filename = "priceBlinkData" #filename that the parsed results will show up in
dataname = sys.argv[1] #filename to read JSON data from recieved when called by php
#this is this the raw JSON
retailList = open(dataname, "r").read()
retailList = retailList[retailList.find("{"):][0:len(retailList)-2]
tempVar = json.loads(retailList)
i=0
f = open(filename, 'a')
for seller in tempVar['retailers']:
	#there's always only 5 of the newest
	if i>=5:
		sys.stdout.write("Write successful!")
		f.close()
		exit(0)
	f.write("Price: "+seller['price']+"\n")
	f.write("Shipping Price: "+seller['shipping'][seller['shipping'].find("+")+1:]+"\n")
	f.write("Retailer: "+seller['retailer_name']+"\n")
	f.write("Name: "+seller['name']+"\n")
	f.write("URL: "+unquote(seller['url'])+"\n")
	f.write("###########################\n")
	i+=1



