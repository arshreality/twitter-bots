from twython import Twython
import json

with open("twitter_credentials.json", "r") as file:
    creds = json.load(file)

CONSUMER_KEY = creds["CONSUMER_KEY"]
CONSUMER_SECRET = creds["CONSUMER_SECRET"]
ACCESS_KEY = creds["ACCESS_TOKEN"]
ACCESS_SECRET = creds["ACCESS_SECRET"]

# Authenticate to Twitter
twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

photo = open('jus-reign-there.gif', 'rb')
response = twitter.upload_media(media=photo)
twitter.update_status(status='come back my man',
                      media_ids=[response['media_id']])
