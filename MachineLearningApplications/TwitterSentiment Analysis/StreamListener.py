from tweepy.streaming import StreamListener

"""
    Responsible to override tweepy stream listener class to store and display tweet. 
"""


class TwitterStreamListener(StreamListener):

    def __init__(self, filenameForTweet):
        self.filenameForTweet = filenameForTweet

    def on_data(self, data):
        try:
            print(data)
            with open(self.filenameForTweet, 'a') as tweetFile:
                tweetFile.write(data)
            return True
        except BaseException as e:
            print(e)
        return True

    def on_error(self, data):
        print(data)
        if data == 420:
            # If Rates Limit occurs
            return False
