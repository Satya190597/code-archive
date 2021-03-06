from tweepy import API
from tweepy import Cursor

import Authentication

"""
    Client class to handle user request as twitter client.
"""


class Client:

    def __init__(self, twitterUser=None):
        self.auth = Authentication.TwitterAuthenticator().authenticateTwitterApi()
        self.twitterClient = API(self.auth)
        self.twitterUser = twitterUser

    def getTwitterClientApi(self):
        return self

    def getTweets(self, numOfTweets):
        tweets = []
        for tweet in Cursor(self.twitterClient.user_timeline, id=self.twitterUser).items(numOfTweets):
            tweets.append(tweet)
        return tweets

    def getFriendList(self, numOfFriends):
        friendList = []
        for friend in Cursor(self.twitterClient.friends, id=self.twitterUser).items(numOfFriends):
            friendList.append(friend)
        return friendList
