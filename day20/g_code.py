import requests

# get url
url = 'https://maps.googleapis.com/maps/api/geocode/json'

# identify parameters
payload = {'key' : 'AIzaSyCt-yPcHa_94Iiw769LiEJ7VSjeGV0IyXM', 'address' : 'boston'}

# make request
r = requests.get(url, params = payload)
print(r)

# process information
data = r.json()
location = data['results'][0]
print(location.keys())
formatted = location['formatted_address']
print(formatted)



results = data['results']
print(results)
top_results = results[0]
pretty_address = top_results['formatted_address']
print("You're at %s" % pretty_address)
address_components = top_results['address_components']
print(len(address_components))

# print all address components:
for x in address_components:
    if 'political' in x['types']:
        print(x['short_name'])
        
# print all address components
# for x in address_components:
    # if 'administrative_area_level_1' in x['types']:
        # print("your state is", x['long_name')
    
geometry = top_results['geometry']
print(geometry)
location = geometry['location']
print(location)
lat = location['lat']
lng = location['lng']
print 