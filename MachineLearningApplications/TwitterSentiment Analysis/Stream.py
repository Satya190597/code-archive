import Authentication
import StreamListener

"""
   Responsible for streaming tweets on console and store them in a json file on the basis of hash tags.
"""


class Stream:
    def __init__(self):
        self.auth = Authentication().authenticateTwitterApi()

    def stream_tweets(self, filenameForTweet, hashTagList):
        listener = StreamListener(filenameForTweet)
        stream = Stream(self.auth, listener)
        stream.filter(track=hashTagList)
