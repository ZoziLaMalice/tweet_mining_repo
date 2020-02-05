import tweepy
import csv
from collections import Counter

# Get your Twitter API credentials and enter them here
consumer_key = ''
consumer_secret = ''

access_key = '-'
access_secret = ''

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

tweets = tweepy.Cursor(api.search,
                           q=query,
                           lang="en").items(200)

users_locs = [tweet.user.location for tweet in tweets]
print(users_locs)


for item, count in Counter(users_locs).most_common(10):
    print(item + "\t" + str(count))


data = api.rate_limit_status()

print(data['resources']['statuses']['/statuses/home_timeline'])

trends1 = api.trends_place(615702) # from the end of your code here is Paris
# trends1 is a list with only one element in it, which is a
# dict which we'll put in data.
data = trends1[0]
# grab the trends
trends = data['trends']
# grab the name from each trend
names = [trend['name'] for trend in trends]
# put all the names together with a ' ' separating them
trendsName = ' '.join(names)
print(names)

