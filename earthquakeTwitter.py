#!/usr/bin/env python
import requests
import hashlib
import csv
import time
import json
import twitter

url = "http://earthquake.usgs.gov/earthquakes/catalogs/eqs7day-M1.txt"

def main():
	fetchCSV(url)
	global sha1
	global oauthData
	sha1 = mksha1("earthquakes.csv")
	oauthData = loadSecrets()
	global api
	api = twitter.Api(consumer_key=oauthData['consumerKey'], consumer_secret=oauthData['consumerSecret'], access_token_key=oauthData['accessToken'], access_token_secret=oauthData['accessTokenSecret'])
	api.VerifyCredentials()
	reader = loadCSV()
	latest = getLatest(reader)
	print latest
	minutes=0
	while True:
		if sha1==mksha1("earthquakes.csv"):
			time.sleep(60)
			minutes+=1
			print "Been running for "+str(minutes)+" minutes"
			fetchCSV(url)			
		else:
			print "tweeting"
			reader = loadCSV()
			latest = getLatest(reader)
			tweetText = "Earthquake in "+latest[9]+", it was a magnitude "+latest[6]
			status = tweet(tweetText)
			print status
			sha1 = mksha1("earthquakes.csv")	
	
def mksha1(filename):
	m = hashlib.sha1()
	m.update(open(filename).read())
	m.hexdigest()
	return m.hexdigest()

def fetchCSV(URL):
	url = URL
	r = requests.get(url=url)
	contents = r.content
	f = open("earthquakes.csv", "w")
	f.write(contents)
	f.close()
	
def loadCSV():
	reader = csv.reader(open("earthquakes.csv", "rb"))
	return reader

def tweet(message):
	try:
		status = api.PostUpdate(message)
	except:
		return "Failure!"
	return status
	
def loadSecrets():
	f = open("twitter", 'r')
	settings = json.loads(f.read())
	consumerKey = settings['consumerKey']
	consumerSecret = settings['consumerSecret']
	accessToken = settings['accessToken']
	accessTokenSecret = settings['accessTokenSecret']
	return {'consumerKey':consumerKey, 'consumerSecret':consumerSecret, 'accessToken':accessToken, 'accessTokenSecret':accessTokenSecret}

def getLatest(reader):
	#print reader.next()
	reader.next()
	return reader.next()
	
def searchReader(reader, row):
	reader.next()
	i=0
	for ROW in reader:
		if ROW==row:
			return [i]
		else:
			i+=1

if __name__ == '__main__':
	main()