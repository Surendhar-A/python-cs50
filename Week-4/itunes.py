import requests
import sys
import json

if len(sys.argv) !=2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

print(json.dumps(response.json), indent = 2)

obj = response.json()

for i in obj["results"]:
    print(i["trackName"])
