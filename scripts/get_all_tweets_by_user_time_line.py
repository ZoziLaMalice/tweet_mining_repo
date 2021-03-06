# Download some tweet from Tweeter API

import sys
import csv
import os
import re

# http://www.tweepy.org/
import tweepy

# Get your Twitter API credentials and enter them here
consumer_key = ''
consumer_secret = ''

access_key = '-'
access_secret = ''


def get_all_tweets(screen_name):
    # Twitter only allows access to a users most recent 3240 tweets with this method

    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # initialize a list to hold all the tweepy Tweets
    alltweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name=screen_name, count=200)

    # save most recent tweets
    alltweets.extend(new_tweets)

    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print("getting tweets before %s" % (oldest))

        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)

        # save most recent tweets
        alltweets.extend(new_tweets)

        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print("...%s tweets downloaded so far" % (len(alltweets)))

    # transform the tweepy tweets into a 2D array that will populate the csv
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text] for tweet in alltweets]

    # write to a new csv file from the array of tweets
    outfile = os.path.normpath(os.getcwd() + os.sep + os.pardir) + '/comments/' + screen_name + "_tweets.csv"
    print("writing to " + outfile)
    with open(outfile, 'w', encoding='utf8') as file:
        writer = csv.writer(file, delimiter=',')
        # Adding the header.
        writer.writerow(["datetime", "author", "body"])
        writer.writerows(outtweets)


get_all_tweets('J_tsar')