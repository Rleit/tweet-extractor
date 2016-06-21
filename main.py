from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from pymongo import MongoClient
import json
import time
import datetime

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key=""
consumer_secret=""

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token=""
access_token_secret=""

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def __init__(self):

        self.db = MongoClient("mongodb://localhost:27017").paleotweets

    def on_data(self, data):
        print(data)
        tweet = json.loads(data)
        proper_date = datetime.datetime.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y')
        tweet['proper_date'] = proper_date
        self.db.tweets.insert(tweet)
        return True

    def on_error(self, status):
        print(status)

def start_stream(auth, l):
    while True:
        try:
            stream = Stream(auth, l)
            stream.filter(track=['paléo', 'paleo'])
        except: 
            print('stream broken')
            time.sleep(1)
            continue
        print('relaunch stream')

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    start_stream(auth, l)