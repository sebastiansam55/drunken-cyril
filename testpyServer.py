#!/usr/bin/env python
import requests
import json

def testPython():
	url = "http://127.0.0.1:1234"
	payload = {'titletag': 'test'}
	r = requests.post(url=url, data=json.dumps(payload))
	return 0
	
def testPHP():
	url = "http://192.168.1.105/test.php"
	payload = {'titletag': 'test'}
	r = requests.post(url=url, data=json.dumps(payload))
	return 0
	

if __name__ == '__main__':
	testPHP()