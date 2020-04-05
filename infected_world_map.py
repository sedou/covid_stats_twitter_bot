import tweepy
import urllib.request
from twitter_creds import *

#url = 'https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/world-map.html'
img = 'https://www.cdc.gov/coronavirus/2019-ncov/images/outbreak-coronavirus-world.png'

saved_img = urllib.request.urlretrieve(img, "infected_world_map.png")
message = 'Locations with Confirmed COVID-19 Cases, by WHO Region:'
img_path = 'infected_world_map.png'

# posts message and map with infected locations
def post():
    api.update_with_media(img_path, message)
post()
