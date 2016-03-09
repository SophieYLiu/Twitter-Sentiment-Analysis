from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


#consumer key, consumer secret, access token, access secret.
ckey="BqvlW9MRaWhgfcRPzUAtcBOF2"
csecret="oNd79FpgzC2MsOpu6hmWYmlQNPGE5bJVPfZGK6OLbtQfqWYacx"
atoken="160994399-GGT9NFRPFGwDsISJ0sCcj8DE6VGw7uDQwJtPraNr"
asecret="v3n4RzHgyQH02BXLytxUIo90G2PsbwBVi4dhjB6IJgrNd"

class listener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.sample()
		
