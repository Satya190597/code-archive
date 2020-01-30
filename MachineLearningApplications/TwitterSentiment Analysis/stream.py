from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import  credential
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re

from textblob import TextBlob

"""
	Twitter Clients
"""

class TwitterCLient():
	def __init__(self,twitterUser=None):
		self.auth = TwitterAuthenticator().authenticate_twitter_app()
		self.twitterCLient = API(self.auth)
		self.twitterUser = twitterUser

	def getTwitterClientApi(self):
		return self

	def get_tweets(self,numOfTweets):
		tweets = []
		for tweet in Cursor(self.twitterCLient.user_timeline,id=self.twitterUser).items(numOfTweets):
			tweets.append(tweet)
		return tweets
	
	def getFriendList(self,numOfFriens):
		friendList = []
		for friend in Cursor(self.twitterCLient.friends,id=self.twitterUser).items(numOfFriens):
			friendList.append(friend)
		return friendList
"""
	Twitter Authenticater
"""

class TwitterAuthenticator():
	def authenticate_twitter_app(self):
		auth = OAuthHandler(credential.API_KEY,credential.API_SECRET_KEY)	
		auth.set_access_token(credential.ACCESS_TOKEN,credential.ACCESS_TOKEN_SECRET)
		return auth
		
class TwitterStreamer():
	def __init__(self):
		self.auth = TwitterAuthenticator().authenticate_twitter_app()

	"""
		Class for streaming and processing tweets
	"""
	def stream_tweets(self,filenameForTweet,hashTagList):
		# This handles twitter authentication and the connection to the twitter streaming api
 		
		listener = TwitterListener(filenameForTweet)
		
		
		stream = Stream(self.auth,listener)

		stream.filter(track = hashTagList)


class TwitterListener(StreamListener):
    
	def __init__(self,filenameForTweet):
		self.filenameForTweet = filenameForTweet
	
	def on_data(self,data):
		try:
			print(data)
			with open(self.filenameForTweet,'a') as tf:
				tf.write(data)
			return True
		except BaseException as e:
			print(e)
		return True

	def on_error(self,data):
		print(data)
		if data==420:
			# If Rates Limit occurs
			return False

class TweetAnalyzer():
	def cleanTweet(slef,tweet):
		return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


	def analyzeSentiment(self,tweet):
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
	def tweetsToDataFrame(self,tweets):
		df = pd.DataFrame(data=[tweet.text for tweet in tweets],columns=['Tweets'])

		df['id'] = np.array([tweet.id for tweet in tweets])
		df['len'] = np.array([len(tweet.text) for tweet in tweets])
		df['date'] = np.array([tweet.created_at for tweet in tweets])
		df['source'] = np.array([tweet.source for tweet in tweets])
		df['likes'] = np.array([tweet.favorite_count for tweet in tweets])
		df['retweets'] = np.array([tweet.retweet_count for tweet in tweets])

		return df
		

if __name__ == '__main__':
	hashTagList = ["car","supercar"]

	#twitterStreamer = TwitterStreamer()
	#twitterStreamer.stream_tweets('result.json',hashTagList)

	#client = TwitterCLient('TheTweetOfGod')
	#print(client.getFriendList(5))
	client = TwitterCLient()
	api = client.getTwitterClientApi()

	tweets = api.twitterCLient.user_timeline(screen_name="realDonaldTrump",count=5)
	
	tweetAnalyzer = TweetAnalyzer()
	df = tweetAnalyzer.tweetsToDataFrame(tweets)

	# Get average length over all tweets
	print(np.mean(df['len']))

	# Get The number of most likes tweet
	print(np.max(df['likes']))

	# Get the number of most retweets
	print(np.max(df['retweets']))

	# Time series plot
	#timeLikes = pd.Series(data=df['likes'].values,index=df['date'])
	#timeLikes.plot(figsize=(16,4),color='r')
	#plt.show()

	# Merge plot
	#timeLikes = pd.Series(data=df['likes'].values,index=df['date'])
	#timeLikes.plot(figsize=(16,4),label='likes',legend=True)
	#timeLikes = pd.Series(data=df['retweets'].values,index=df['date'])
	#timeLikes.plot(figsize=(16,4),label='retweets',legend=True)

	#plt.show()

	df['sentiment'] = np.array([tweetAnalyzer.analyzeSentiment(tweet) for tweet in df['Tweets']])

	print(df.head(10))

