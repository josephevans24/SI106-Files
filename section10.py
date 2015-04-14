import json
import requests

def get_airport_rest(airport_code):
    baseurl = 'http://services.faa.gov/airport/status/'
    url_parameters = {"format": "json"}

    response = requests.get(baseurl + airport_code, params = url_parameters)
    return response.json()


# returns the float version of the fahrenheit temperature
def convert_temp_string_to_float(temp_string):
	return float(temp_string[:4])

def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)


list_of_airport_codes = ['DTW', 'LAX', 'PDX', 'PHX', 'SFO', 'PIT', 'BOS', 'LGA', 'DCA', 'ZYX']

# step 1
# Understand what the get_airport_rest function does. What are its inputs, outputs, and what is its purpose?

# step 2
# For each airport, make a call to FAA api and convert the result into data dictionary
f = {}
for a in list_of_airport_codes:
	try:
		f[a] = get_airport_rest(a)

		
	except:
		print 'Not a valid FAA code'

# step 3
# Extract the temperatures from each of the airports (remember to convert them to floats using the helper functions
# above) and create a new dictionary with aiport codes as keys and their associated temperatures as their values
hot = {}
for key in f:
	hot[key] = convert_temp_string_to_float(f[key]['weather']['temp'])
print hot
# step 4
# output (print, for the user to see) the five airports that have the highest temperature
five = sorted(hot, key = lambda x: hot[x], reverse = True)
print five[:5]

