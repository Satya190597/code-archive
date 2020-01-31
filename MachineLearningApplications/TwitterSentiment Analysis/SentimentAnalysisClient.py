import Client
import Analyzer
import numpy as np


class Sentiments:

    def __init__(self, user, numberOfTweets):
        self.user = user
        self.numberOfTweets = numberOfTweets

    def getSentimentsOnlyByTextBlob(self):
        client = Client.Client()
        api = client.getTwitterClientApi()
        tweets = api.twitterClient.user_timeline(screen_name=self.user,count=self.numberOfTweets)
        tweetAnalyzer = Analyzer.TweetAnalyzer()
        dataFrame = tweetAnalyzer.tweetsToDataFrame(tweets)
        dataFrame['sentiment'] = np.array([tweetAnalyzer.
                                          analyzeSentimentByTextBlobModel(tweet) for tweet in dataFrame['Tweets']])
        print(dataFrame.head(self.numberOfTweets))


if __name__ == '__main__':
    twitterUser = input("Enter Twitter User : ")
    noOfTweets = int(input("Enter Number Of Tweets : "))

    sentiments = Sentiments(twitterUser, noOfTweets)
    sentiments.getSentimentsOnlyByTextBlob()

