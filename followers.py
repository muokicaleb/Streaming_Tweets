import numpy as np
import pandas as pd
from tweepy import API
from tweepy import OAuthHandler
import twitter_credentials


# twitter credentials are in twitter_credentials.
# a better way is setting them as environment variables then import OS


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
        df['ScreenName'] = np.array([follower.screen_name for follower in followers])
        df['NumberFollowers'] = np.array([follower.followers_count for follower in followers])
        df['id'] = np.array([follower.id for follower in followers])
        df['statusesCount'] = np.array([follower.statuses_count for follower in followers])
        df['profileImageURL'] = np.array([follower.profile_image_url for follower in followers])
        return df


if __name__ == '__main__':
    twitter_client = TwitterClient()
    follower_analyzer = FollowerAnalyzer()
    api = twitter_client.get_twitter_client_api()
    followers = api.followers(screen_name="muoki_caleb", count=200)
    df = follower_analyzer.tweets_to_data_frame(followers)
    df.to_csv('FollowerOutput.csv', sep='\t', encoding='utf-8')
    print("done")
