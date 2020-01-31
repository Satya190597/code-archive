from textblob import TextBlob

import numpy as np
import pandas as pd
import re

"""
    Responsible to generate data frames and perform sentiment analysis.
"""


class TweetAnalyzer:

    @staticmethod
    def cleanTweet(tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def analyzeSentimentByTextBlobModel(self, tweet):
        analysis = TextBlob(self.cleanTweet(tweet))
        if analysis.sentiment.polarity > 0:
            return 1
        elif analysis.sentiment.polarity == 0:
            return 0
        else:
            return -1

    """
        Functionality of analyzing and categorizing class
    """

    @staticmethod
    def tweetsToDataFrame(tweets):
        dataFrame = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
        dataFrame['id'] = np.array([tweet.id for tweet in tweets])
        dataFrame['len'] = np.array([len(tweet.text) for tweet in tweets])
        dataFrame['date'] = np.array([tweet.created_at for tweet in tweets])
        dataFrame['source'] = np.array([tweet.source for tweet in tweets])
        dataFrame['likes'] = np.array([tweet.favorite_count for tweet in tweets])
        dataFrame['retweets'] = np.array([tweet.retweet_count for tweet in tweets])
        return dataFrame
