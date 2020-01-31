from tweepy import OAuthHandler

import credential

"""
    Responsible to authenticate twitter api by using tweepy OAuthHandler
"""


class TwitterAuthenticator:

    @staticmethod
    def authenticateTwitterApi():
        auth = OAuthHandler(credential.API_KEY, credential.API_SECRET_KEY)
        auth.set_access_token(credential.ACCESS_TOKEN, credential.ACCESS_TOKEN_SECRET)
        return auth
