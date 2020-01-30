from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import  credential

class StdOutListener(StreamListener):
    
    def on_data(self,data):
        print(data)
        return True

    def on_error(self,data):
        print(status)

if __name__ == '__main__':

	listener = StdOutListener()
	auth = OAuthHandler(credential.API_KEY,credential.API_SECRET_KEY)	
	auth.set_access_token(credential.ACCESS_TOKEN,credential.ACCESS_TOKEN_SECRET)
	
	stream = Stream(auth,listener)

	stream.filter(track=['donald trump'])
