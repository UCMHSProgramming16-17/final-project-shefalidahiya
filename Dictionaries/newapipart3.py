# import requests library
import requests

# get url
url = 'https://maps.googleapis.com/maps/api/geocode/json'


user_input = input("location? ")

# identify parameters
payload = {'key' : 'AIzaSyCt-yPcHa_94Iiw769LiEJ7VSjeGV0IyXM', 'address' : user_input}

# make request
r = requests.get(url, params = payload)

# process information
data = r.json()
location = data['results'][0]
results = data['results']
top_results = results[0]
geometry = top_results['geometry']
location = geometry['location']

lat = format(location['lat'])
lng = format(location['lng'])

# define endpoint for darksky
endpoint = 'https://api.darksky.net/forecast/'
# define api key
api_key = 'da5d52438b53e27259e8e2bdc2f7c51f'

# url for request
url = endpoint + api_key + '/' + lng + ',' + lat

# To do: make a request
r = requests.get(url)
print(r)

weather = r.json()
print(weather['currently'])
print(weather['hourly']['summary'])

