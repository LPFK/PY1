# documentation :  https://docs.python.org/3/library/json.html
import requests
import json
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
data = response.json()
print(json.dumps(data, indent=4))