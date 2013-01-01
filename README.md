Quote Gabek
==============

Bot script for the Twitter account [@QuotesGabek](http://twitter.com/QuotesGabek). To run, you will need the [twitter](https://github.com/sixohsix/twitter) and [pytz](http://sourceforge.net/projects/pytz/) modules.

Twitter module
==============

On line #15 you will see:

    # Twitter credentials
    t = Twitter(
                auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)
               )

Supply your proper tokens/secrets, and you're good to go!
