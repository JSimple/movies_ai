import tweepy
from keys import *

from generator import *

### OAUTH STUFF ###
client = tweepy.Client(
    consumer_key=whisper['api_key'],
    consumer_secret=whisper['api_secret'],
    access_token=whisper['access_token'],
    access_token_secret=whisper['access_token_secret']
)

## THE BOT ITSELF ##

logline = generate_logline()
client.create_tweet(text = logline)
