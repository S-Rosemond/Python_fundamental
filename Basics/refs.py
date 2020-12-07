# handle url
import urllib.request, urllib.parse
# JSON
import json


# encode url
endpoint = url + urllib.parse.urlencode(param)
# open url, can have context = urlopen(url,context =ctx)
res = urllib.request.urlopen(url)
# decode into unicode or read b''|byte string
res.read()
res.decode()
data = res.read().decode()
# JSON : if res is json string, parse with load
json_data = json.loads(data)
