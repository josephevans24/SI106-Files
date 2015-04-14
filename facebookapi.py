import facebook
import json
import test
import requests

def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

fb_class_id = '1196007610428928'
    
r = requests.get("https://graph.facebook.com/?%s" % (fb_class_id))
print r.status_code
print r.text

# get access token from 
# https://developers.facebook.com/tools/explorer"
access_token = None

if access_token == None:
    access_token = raw_input("\nCopy and paste token from https://developers.facebook.com/tools/explorer\n>  ")

# create an instance of the class GraphAPI, which saves our access_token
graph = facebook.GraphAPI(access_token)
# access_token is automatically passed to FB, in the format FB wants it (not in the URL, unfortunately)
feed = graph.get_object("%s/feed" % (fb_class_id))

print type(feed)
print feed.keys()
print type(feed['data'])
print len(feed['data'])
print pretty(feed['data'][2])
print feed['data'][2]["message"]
