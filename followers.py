import numpy as np
import pandas as pd
from tweepy import API
from tweepy import OAuthHandler
import twitter_credentials


class TwitterAuthenticator():
    def authenticate_twitter_app(self):
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        return auth


class TwitterClient():
    def __init__(self, twitter_user=None):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)
        self.twitter_user = twitter_user

    def get_twitter_client_api(self):
        return self.twitter_client


class FollowerAnalyzer():
    def tweets_to_data_frame(self, followers):
        df = pd.DataFrame(data=[follower.name for follower in followers], columns=['Followers'])
        '''df['id'] = np.array([tweet.id for tweet in tweets])
        df['len'] = np.array([len(tweet.text) for tweet in tweets])
        df['date'] = np.array([tweet.created_at for tweet in tweets])
        df['source'] = np.array([tweet.source for tweet in tweets])
        df['likes'] = np.array([tweet.favorite_count for tweet in tweets])
        df['retweets'] = np.array([tweet.retweet_count for tweet in tweets])
'''
        return df


if __name__ == '__main__':

    # creating 2 objects of class Twitterclient and tweetAnalyzer
    twitter_client = TwitterClient()
    follower_analyzer = FollowerAnalyzer()

    api = twitter_client.get_twitter_client_api()

    followers = api.followers(screen_name="muoki_caleb")
    df = follower_analyzer.tweets_to_data_frame(followers)
    print(df.head(10))
    # print(friends)