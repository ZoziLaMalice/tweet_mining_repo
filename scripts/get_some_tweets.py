# Download some tweet from Tweeter API

import sys
import csv
import os
import re
from tqdm import tqdm
import configparser as cp

# http://www.tweepy.org/
import tweepy

config = cp.ConfigParser()
config.read('config.ini')

# Get your Twitter API credentials and enter them here
consumer_key = config.get('AUTH', 'consumer_key')
consumer_secret = config.get('AUTH', 'consumer_secret')

access_key = config.get('AUTH', 'access_key')
access_secret = config.get('AUTH', 'access_secret')


# method to get a user's last tweets
def get_tweets(username):
    # http://tweepy.readthedocs.org/en/v3.1.0/getting_started.html#api
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    # set count to however many tweets you want
    number_of_tweets = 1000

    # get tweets
    tweets_for_csv = []
    for tweet in tqdm(tweepy.Cursor(api.user_timeline, id=username).items(number_of_tweets)):
        # create array of tweet information: username, tweet id, date/time, text
        tweets_for_csv.append([tweet.id_str, username, tweet.text])




    # write to a new csv file from the array of tweets
    outfile = os.path.normpath(os.getcwd() + os.sep + os.pardir) + '/comments/' + username + "_tweets.csv"
    print("writing to " + outfile)
    with open(outfile, 'w', encoding='utf8') as file:
        writer = csv.writer(file, delimiter=',')
        # Adding the header.
        writer.writerow(["datetime", "author", "body"])
        writer.writerows(tweets_for_csv)



# if we're running this as a script
if __name__ == '__main__':

    # # get tweets for username passed at command line
    # if len(sys.argv) == 2:
    #     get_tweets(sys.argv[1])
    # else:
    #     print("Error: enter one username")

    # alternative method: loop through multiple users
    users = ['MonsieurDream']

    for user in users:
        get_tweets(user)
