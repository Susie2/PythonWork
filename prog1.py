import os
import urllib
import json

print "Hello World!"


resp = urllib.urlopen("http://m.weather.com.cn/data/101270101.html")

# raw = resp.read()
# json_str = unicode(raw, "utf-8")
# print json_str
json_obj = json.load(resp)

print json_obj['weatherinfo']['city']
print json_obj['weatherinfo']['weather1']



os.system("pause")