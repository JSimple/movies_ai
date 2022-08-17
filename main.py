import tweepy
from keys import *
import os

from generator import *

### OAUTH STUFF ###
client = tweepy.Client(
    consumer_key=os.getenv("TWITTER_CONSUMER_KEY"),
    consumer_secret=os.getenv("TWITTER_CONSUMER_SECRET"),
    access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
    access_token_secret=os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
)

## THE BOT ITSELF ##

logline = generate_logline()
client.create_tweet(text = logline)
