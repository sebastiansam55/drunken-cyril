#!/usr/bin/env python
import requests
import json

username = "icallitvera"
password = "password"
version = "123421546"
register = "register"
#url = "http://ssebastian.koding.com/mineAuth.php"
url = "http://192.168.1.105/mineAuth.php?user="+username+"&password="+password+"&version="+version
#url = "http://httpbin.org/post"
r = requests.get(url=url)

print r.content