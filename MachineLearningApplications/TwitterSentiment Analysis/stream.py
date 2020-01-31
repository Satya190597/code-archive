import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import Client
import Analyzer

if __name__ == '__main__':
	hashTagList = ["car","supercar"]

	#twitterStreamer = TwitterStreamer()
	#twitterStreamer.stream_tweets('result.json',hashTagList)

	#client = TwitterCLient('TheTweetOfGod')
	#print(client.getFriendList(5))
	client = Client.Client()
	api = client.getTwitterClientApi()

	tweets = api.twitterClient.user_timeline(screen_name="realDonaldTrump",count=5)
	
	tweetAnalyzer = Analyzer.TweetAnalyzer()
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
	timeLikes = pd.Series(data=df['likes'].values,index=df['date'])
	timeLikes.plot(figsize=(16,4),label='likes',legend=True)
	timeLikes = pd.Series(data=df['retweets'].values,index=df['date'])
	timeLikes.plot(figsize=(16,4),label='retweets',legend=True)

	plt.show()

	#df['sentiment'] = np.array([tweetAnalyzer.analyzeSentimentByTextBlobModel(tweet) for tweet in df['Tweets']])

	#print(df.head(10))

