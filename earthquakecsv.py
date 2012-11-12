import requests
import csv

def search(forthis, fromthis):
	print forthis
	for row in fromthis:
		for row_item in row:
			if row_item==forthis:
				print row_item
				return [row_item, row]

def search_coords(coord, fromthis):
	for i in range(0,9):
		fromthis.next()
	for row in fromthis:
		print round(float(row[4]))
		if round(float(row[4]))==float(str(coord)+".0"):
			print row[4]
			return [row[4], row[5], row]
		elif round(float(row[5]))==float(str(coord)+".0"):
			print row[5]
			return [row[4], row[5], row]
				
def prettyprint(rowlist):
	datetime = rowlist[3]
	lat_long = (rowlist[4], rowlist[5])
	magnitude = rowlist[6]
	region = rowlist[9]
	print("Location: \t\t"+region)
	print("Magnitude: \t\t"+magnitude)
	print("Lat_Long Coords: \t"+str(lat_long))
	print("DateTime: \t\t"+datetime)
	
def searchloop():
	reader = csv.reader(open("earthquakes.csv", "rb"))
	for i in range(0,10):
		print(str(i)+". "+values[i])
	value = int(raw_input("0-9: "))
	search_for_this = raw_input("What to search for?")
	if value==0:
		rowlist = search(search_for_this, reader)[1]
		prettyprint(rowlist)
	elif value==4 or value==5:
		rowlist = search_coords(search_for_this, reader)[2]
		prettyprint(rowlist)
	elif value==6:
		rowlist = search(search_for_this, reader)[1]
		print rowlist
		prettyprint(rowlist)
	else:
		print("Function not available")
		
def displayloop():
	print("Displaying latest 5")
	reader = csv.reader(open("earthquakes.csv", "rb"))
	i=0
	for row in reader:
		prettyprint(row)
		print("")
		if i==9:
			exit()
		i+=1

values= ["Src","Eqid","Version", "Datetime", "Lat", "Long", "Magnitude", "Depth", "NST", "Region"]


url = "http://earthquake.usgs.gov/earthquakes/catalogs/eqs7day-M1.txt"
r = requests.get(url=url)
contents = r.content
f = open("earthquakes.csv", "w")
f.write(contents)
f.close()
search_ = raw_input("Search mode? [Y/n]")

if search_=="y" or search_=="Y":
	searchloop()
else:
displayloop()
