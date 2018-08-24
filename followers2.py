import csv
from tweepy import API
from tweepy import Cursor
from tweepy import OAuthHandler
import time
from tweepy import TweepError
import twitter_credentials


class TwitterAuthenticator():
    def authenticate_twitter_app(self):
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        return auth


class TwitterClient():
    def __init__(self, twitter_user=None):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth, wait_on_rate_limit=True)
        self.twitter_user = twitter_user

    def get_twitter_client_api(self):
        return self.twitter_client


if __name__ == '__main__':
    twitter_client = TwitterClient()

    api = twitter_client.get_twitter_client_api()

    Output_file = csv.writer(open('followers_python.csv', 'w'))
    Output_file.writerow(['Name', 'ScreenName', "NumberFollowers", "id", "statusesCount", "profileImageURL"])

    followers = Cursor(api.followers, screen_name="muoki_caleb", count=200).items()

    while True:
        try:
            follower = next(followers)
        except TweepError:
            time.sleep(60 * 15)
            follower = next(followers)
        except StopIteration:
            break

        Output_file.writerow([follower.name, follower.screen_name,
                              follower.followers_count, follower.id,
                              follower.statuses_count, follower.profile_image_url])

    print("done")
