
import tweepy

# Get your Twitter API credentials and enter them here
consumer_key = ""
consumer_secret = ""
access_key = "-"
access_secret = ""

# Twitter only allows access to a users most recent 3240 tweets with this method

# authorize twitter, initialize tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# 200 tweets to be extracted
number_of_tweets=2
tweets = api.user_timeline(screen_name='MonsieurDream')

[print(tweet.text) for tweet in tweets]