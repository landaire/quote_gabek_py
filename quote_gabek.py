import os, re, random, dateutil.parser, pytz
from twitter import *
from datetime import datetime, timedelta
from time import sleep

# External dependencies: pytz, twitter
# twitter: https://github.com/sixohsix/twitter
# pytz: http://sourceforge.net/projects/pytz/

trailing_words = ["So trill", "Trill", "True", "Real talk", "Why aren't I gay?", "If only he loved bots", "Oh",
                  "#realtalk", "#lovehim", "#trill", "#trillistniggaalive", "#thingshomosexualssay", "Sexy", "#random",
                  "#myboo", "#sosexy", "SENDING OUT AN SOS", "So that's what sank the Titanic?", "Whores these days...",
                  "#foreverandever", "Yeah, fuck @_skitzo", "I wonder if he's a local single in my area..."]

# Twitter credentials
t = Twitter(
            auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET,
                       CONSUMER_KEY, CONSUMER_SECRET)
           )

# Get my last tweet
last_tweet = t.statuses.user_timeline(screen_name="QuotesGabek", count=1)[0]
# If the last tweet was tweeted within an hour...
if dateutil.parser.parse(last_tweet["created_at"]) > pytz.UTC.localize(datetime.utcnow()):
  sleep(3600) # Sleep for an hour

last_tweet_id = None
# Open the last tweet
with open("last_tweet_id.txt", "a+") as f:
  if os.path.getsize("last_tweet_id.txt") > 0:
    f.seek(0)
    last_tweet_id = f.readline()
    if last_tweet_id != '':
      last_tweet_id = int(last_tweet_id)
  if last_tweet_id == None:
    last_tweet_id = 285524200033243136

while True:
  # Request gabe_k's tweets
  tweets = t.statuses.user_timeline(screen_name="gabe_k", count=30, include_rts=False)
  # Randomize the lists we have
  random.shuffle(tweets)
  random.shuffle(trailing_words)
  for tweet in tweets:
    if tweet["id"] > last_tweet_id and len(tweet["text"]) <= 115:
      tweet_text = "As gabe_k once said, \"%s.\"" % re.sub("\.$", "", tweet["text"])
      max_string = 140 - len(tweet_text)
      for word in trailing_words:
        if len(word) <= max_string:
          tweet_text += " %s" % word
          if len(word) + 1 <= max_string:
            tweet_text += "."
          break
      with open("last_tweet_id.txt", "w") as f:
        f.write(str(tweet["id"]))
      t.statuses.update(status=tweet_text)
      print "%s Tweeted: %s" % (str(datetime.now()), tweet_text)
      break
  sleep(3 * 60 * 60)