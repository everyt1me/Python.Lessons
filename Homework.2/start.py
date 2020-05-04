import json
import requests

response = requests.get('https://api.covid19api.com/summary.json')
if response.status_code == 200:
    source = response.read()
    data = json.loads(source)
else:
    print('An error occurred while attempting to retrieve data from the API.')

type(data)
data.keys()
type(data['Countries'])
data['Countries'].keys()
