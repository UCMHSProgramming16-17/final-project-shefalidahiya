# import requests library
import requests

# define endpoint for darksky
endpoint = 'https://api.darksky.net/forecast/'
# define api key
api_key = 'da5d52438b53e27259e8e2bdc2f7c51f'
lon = input('longitude? ')
lat = input('latitude? ')

# url for request
url = endpoint + api_key + '/' + lon + ',' + lat
print(url)

# To do: make a request
r = requests.get(url)
print(r)

weather = r.json()
print(weather['currently'])
print(weather['hourly']['summary'])