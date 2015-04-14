import test106 as test
import requests 
import json

# This is a function we've provided for you so you can print stuff 
# in a pretty, easy-to-read way. 
def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

#### Exercises: A RESTful API

# The FAA has put out a REST API for accessing current information 
# about US airports. You'll be using it in the following exercises.

## NOTE: Almost all of the following exercises build on one another. 
## You can use code you wrote in earlier exercises in later ones. 
## If you keep this in mind, this problem set'll be even easier for you!

# First, point your web browser to the following URL:
#   http://services.faa.gov/airport/status/DTW?format=json
#
# The text that is shown in your browser is a JSON-formatted dictionary.
# It can easily be converted into a python dictionary and processed in a 
# manner similar to what we have done with the Facebook feed previously.
# The exercise below guides you through the process of writing python
# code that uses this RESTful API to extract information about some
# airports.

# [PROBLEM 1]

## Encoding query parameters in a URL
# (1a) Manually write out the dictionary you will need to pass
# to the params argument when you make a request. The key should
# be 'format', and the value should be 'json', since this is the only
# parameter required by the API. Save the dictionary in a variable
# called url_parameters.



# put that one line of code here:

url_parameters = {'format': 'json'}


# (1b) Now, write the whole assignment statement to make a
#      request to the base url for the FAA api, concatenate
#      the airport string "DTW" to the base url, and pass that
#      and the url_parameters dictionary to the requests.get
#      method. Use the code we've put below with the baseurl
#      and airport variables.
#      Save the response in a variable called airport_response.

#      The base url:  http://services.faa.gov/airport/status/
cloud = requests.get('http://services.faa.gov/airport/status/' +'DTW', params = url_parameters)

# Note that if you run the correct line of code and you do not
# have an internet connection, you will get an error!

# Remember, requests.get() says 'go get data from the internet from...'.
    
print '---------------'
baseurl = 'http://services.faa.gov/airport/status/'
airport = 'DTW'
# Write your line of code below:
airport_response = requests.get(baseurl)

# Again, simple -- we're doing this step by step.

## Testing problem 1
print "--------------"
test.testEqual(url_parameters, {'format':'json'}, "testing correct output for 1(a)")
test.testEqual(type(airport_response),type(requests.get("http://google.com")), "testing correct type of expression for 1(b)")


# [PROBLEM 2]
## Grabbing data off the web
# (2)  Put the request you made in problem 1 in a proper try/except clause.
#      Then, use the .json() method on the response you get back to turn the data
#      in one big Python dictionary. Save that in the variable
#      airport_data.
#   Follow the comments!

print '---------------'

try:
    # Place the request you wrote in 1(b) here.
    cloud = requests.get('http://services.faa.gov/airport/status/' +'DTW', params = url_parameters)
    # Now assign airport_data as described above.
    airport_data = cloud.json()
    


    #print pretty(airport_data) # uncomment, if you're curious what you got back

    ## Testing problem 2
    test.testEqual(type(airport_data), type({}), "testing type in problem 2")
    test.testEqual(airport_data['city'], u"Detroit", "testing whether you got a reasonable result in problem 2")
except:
    print "Failed tests for problem 2"

# [PROBLEM 3] Extracting relevant information from a dictionary

# Now you have a JSON-formatted Python dictionary with a
# bunch of data from the FAA about the airport with code DTW.  
# Remember how you had to concatenate the "DTW" string to the base url 
# for the API, and then add the parameters, to make a request to this
# API. 



# From the airport data dictionary, extract the name, 
# the reason field from within the status,
# the current temperature, and the last time it was updated.

# HINT: Look at the nested data chapter.

# Save these pieces of info in variables called, respectively: 
#   airport_name, status_reason, current_temp, recent_update

# Write your code below!
print '---------------------------------'
# print pretty(airport_data) # uncomment this to see what the dictionary looks like
airport_name = airport_data['IATA']
status_reason = airport_data['status']['reason']
current_temp = airport_data['weather']['temp']
recent_update = airport_data['weather']['meta']['updated']

# Here is testing and printing your results.
try:
    print airport_name
    print status_reason
    print current_temp
    print recent_update

    ## TESTS - PROBLEM 4
    test.testEqual(airport_name,u"DTW","testing p4 airport name")
    test.testEqual(type(status_reason),type(u""),"testing type in p4 - status_reason")
    test.testEqual(type(current_temp), type(u""), "testing type in p4 -- current_temp")
    test.testEqual(type(recent_update), type(u""),"testing type in p4 -- recent_update")
except:
    print "Failed tests for problem 4"
    
print '---------------------------------'

# [PROBLEM 4]

## Generalizing your code
# Now you'll think about the code you've written in earlier steps
# and make generalized versions!

# (4a) Write a function called get_airport() that accepts 
# a three-letter airport code and returns a data dictionary 
# like the one you get in Problem 3. 
# This function should work no matter where it is called, with just
# the input of an airport code like "DTW"!
# You can assume that the requests module is available, though.

# Hint: If you input "DTW" into your get_airport function, you should get
# a different result returned than if you invoke the function with
# the input "LAX", and so on. 

# put your code here:
def get_airport(txt):
    new = (baseurl + txt)
    next = requests.get(new, params = url_parameters)
    final = next.json()
    return final
print get_airport('DTW')

# This code will try to call get_airport and use the pretty function
# to print out the result in a neat way so you can read it.
try:
    print pretty(get_airport('DTW'))
    print "testing calls to get_airport with various airport codes"
    test.testEqual(type(get_airport("DTW")),type({"a":1}))
    test.testEqual(type(get_airport("LAX")),type({"a":1}))
    test.testEqual(get_airport("DTW") == get_airport("LAX"), False)
except:
    print "You have not written the function get_airport yet, or there's an error in it"

print '---------------------------------'

# (4b) Write another function called extract_airport_data() that accepts 
#      an airport code string,
#      and returns a tuple of the airport name, status reason, current temp, and recent update.

#      This function should call the get_airport() function.  

# put your code here
def extract_airport_data(txt):
    squad = get_airport(txt)
    turnt = (squad['IATA'], squad['status']['reason'], squad['weather']['temp'], squad['weather']['meta']['updated'])
    return turnt

try:
    print "trying to call the extract_airport_data function"
    tuple_result = extract_airport_data('SFO')
    print "------"
    print "trying to print the tuple that is returned from a call to extract_airport_data"
    print tuple_result
    print "Testing type of extract_airport_data's return value"
    test.testEqual(type(extract_airport_data("SFO")),type(("hi","bye")))
except:
    print "You have not written the function extract_airport_data yet or have another error"

# There are no other tests
print '---------------------------------'

# (4c) Iterate over the fav_airports list and print out the abbreviated info for
# each, by calling extract_airport_data().

fav_airports = ['PIT', 'BOS', 'LGA', 'DCA']
# write your code here:
for a in fav_airports:
    print extract_airport_data(a)

# [PROBLEM 5]
# Error handling and exceptions
# (5a) Uncomment the request for a bogus airport below.  It should throw an exception.
#      Wrap the call to extract_airport_data in a try/except block.
# 
print '---------------'

# wrap this following line of code in a try/except block as described above!
# If the request fails, your code should 
#  print out "Sorry, that didn't work."

# Uncomment this and add code to this to make this a 'safe' request with try/except
try:
    extract_airport_data("JAC")
except:
    print "Sorry this didn't work"


# (5b) Now, generalize this to define a function safe_airport_data.
# This is very similar to extract_airport_data,
# except that it should accept an airport code string as input,
# and it should return a tuple the same as the extract_airport_data
# function, with:
# airport_name,status_reason,current_temp,recent_update
# for any airport data that is safely retrieved. Otherwise,
# the function should return None
# Hint: call extract_airport_data in this function!

# Write your code here:
def safe_airport_data(txt):
    try:
        return extract_airport_data(txt)
    except:
        return None

# tests for 5(b)
print "----------------"
try:
    print "testing safe_airport_data"
    test.testEqual(type(safe_airport_data("SFO")),type(("hello","goodbye")))
    test.testEqual(safe_airport_data("sdfaddgsa"),None)
except:
    print "Failed tests of safe_airport_data"

# Trying out your own airports (5c) 
# Create a list including your 3 top airport codes,
# and one airport code that doesn't really exist.  
# Print out the extracted data by calling safe_airport_data on each
# and, if a string is returned, printing it out.
# If no string is returned, print out: "Failed for airport <the airport code it failed for>".

# uncomment this code and fill in your_favs
your_favs = ['ABI', 'ABE', 'PHX', 'SWAG']

# Write the rest of your code for this problem here:
for b in your_favs:
    c = safe_airport_data(b)
    if c == None:
        print 'Failed for airport <the airport code it failed for>'
    else:
        print c
    


## [PROBLEM 6]
# Using real live data to write a CSV file!
# Make a new list, like your_favs, called airport_list,
# with at least four different FAA airport codes. 

# Then, use iteration and invocations of the safe_airport_data function 
# to write a CSV file called "airport_temps.csv" with 4 columns in it: 
# airport_name, status_reason, current_temp, recent_update

# The CSV file you write should have at LEAST five rows -- 
# one for the header (the column names),
# and four for the data from each of the airports in your airport_list.

# Write your code here:
airport_list = ['DTW', 'DFW', 'ORD', 'JFK']
outfile = open("airport_temps.csv", "w")
header = ("airport_name", "status_reason", "current_temp", "recent_update")
outfile.write('"%s", "%s", "%s", "%s"\n' % header)
for swag in airport_list:
    team = safe_airport_data(swag)
    outfile.write('%s,%s,%s,%s\n' % team)
outfile.close()
    


# Open the document in Excel or Google Sheetes to make sure that it is properly formatted. (We will do that when we are grading!)
