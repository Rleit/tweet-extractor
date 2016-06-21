from pymongo import MongoClient
from pprint import pprint

if __name__ == '__main__':

    client = MongoClient("mongodb://localhost:27017")
    db = client.paleotweets

    cursor = db.tweets.find()
    cnt = 0
    for tweet in cursor:
    	#pprint(tweet)
    	cnt += 1
    print('total tweets stored : ', cnt)

    # To drop the collection
    #db.tweets.drop()
