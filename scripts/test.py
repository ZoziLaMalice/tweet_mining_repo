import tweepy
import csv

# Get your Twitter API credentials and enter them here
consumer_key = ""
consumer_secret = ""
access_key = "-"
access_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

csvFile = open('EconTwitter.csv', 'a')
csvWriter = csv.writer(csvFile)
query = "@MonsieurDream"
number_of_tweets = 10
tweets = api.search(q=query, count=number_of_tweets, tweet_mode="extended")

for tweet in tweets:
    print(tweet.created_at, tweet.full_text)

