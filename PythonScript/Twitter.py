import os
import tweepy

def TwitterAuthorize():
    consumer_key = os.environ["consumer_key"]
    consumer_secret = os.environ["consumer_secret"]
    access_key = os.environ["access_key"]
    access_secret = os.environ["access_secret"]

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    return api


def SimpleTweet(api):
    api.update_status("tweepyから投稿")

api = TwitterAuthorize()
SimpleTweet(api)