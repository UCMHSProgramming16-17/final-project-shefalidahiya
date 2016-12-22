import requests

# TODO: set up URL for request
endpoint = 'https://api.darksky.net/forecast/'
api_key = 'da5d52438b53e27259e8e2bdc2f7c51f'
lat = '28.385071'
lon = '-81.563808'
payload = {'lang': 'en', 'exclude': 'hourly, minutely, daily, alerts, flags'}

# url for request
url = endpoint + api_key + '/' + lon + ',' + lat
print(url)

# TODO: make a request
r = requests.get(url, params=payload)
print(r)

weather = r.json()
print(weather['currently']['summary'])