import json
from urllib.request import urlopen

url = "clear"

response = urlopen(url)

date = json.load(response)

ip = date["ip"]
org = date["org"]
city = date["city"]
pais = date['country']
regiao = date['region']

print(ip, org, city, pais, regiao)