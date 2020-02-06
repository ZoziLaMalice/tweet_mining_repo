import tweepy
import csv
from collections import Counter
import configparser as cp
from tqdm import tqdm
import os
import re

# Get your Twitter API credentials and enter them here
config = cp.ConfigParser()

config.read('config.ini')

# Get your Twitter API credentials and enter them here
consumer_key = config.get('AUTH', 'consumer_key')
consumer_secret = config.get('AUTH', 'consumer_secret')

access_key = config.get('AUTH', 'access_key')
access_secret = config.get('AUTH', 'access_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# csvFile = open('EconTwitter.csv', 'a')
# csvWriter = csv.writer(csvFile)
query = "#CoronavirusOutbreak" # -filter:retweets"
# number_of_tweets = 10
# tweets = api.search(q=query, count=number_of_tweets, tweet_mode="extended")

# for tweet in tweets:
#     print(tweet.user.screen_name,' --- ', tweet.user.location,' --- ', tweet.full_text)


date_since = "2019-11-16"
number_of_tweets = 1000

# get tweets
tweets_for_csv = []
for tweet in tqdm(tweepy.Cursor(api.search, q=query, lang="en").items(number_of_tweets)):
    # create array of tweet information: username, tweet id, date/time, text
    tweets_for_csv.append([tweet.id_str, tweet.user.screen_name, tweet.text])

query_to_filename = re.sub('#', '', query)

# write to a new csv file from the array of tweets
outfile = os.path.normpath(os.getcwd() + os.sep + os.pardir) + '/comments/' + query_to_filename + "_tweets.csv"
print("writing to " + outfile)
with open(outfile, 'w', encoding='utf8') as file:
    writer = csv.writer(file, delimiter=',')
    # Adding the header.
    writer.writerow(["datetime", "author", "body"])
    writer.writerows(tweets_for_csv)

# users_locs = [tweet.user.location for tweet in tweets_for_csv]
# print(users_locs)
#
#
# for item, count in Counter(users_locs).most_common(10):
#     print(item + "\t" + str(count))
#
#
# data = api.rate_limit_status()
#
# print(data['resources']['statuses']['/statuses/home_timeline'])
#
# trends1 = api.trends_place(615702) # from the end of your code here is Paris
# # trends1 is a list with only one element in it, which is a
# # dict which we'll put in data.
# data = trends1[0]
# # grab the trends
# trends = data['trends']
# # grab the name from each trend
# names = [trend['name'] for trend in trends]
# # put all the names together with a ' ' separating them
# trendsName = ' '.join(names)
# print(names)

