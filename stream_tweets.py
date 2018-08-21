from tweepy import API
from tweepy import Cursor
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import StreamListener
import twitter_credentials


class TwitterAuthenticator():
    def authenticate_twitter_app(self):
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        return auth


class TwitterStreamer():
    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator()

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        listener = TwitterListener(fetched_tweets_filename)
        auth = self.twitter_authenticator.authenticate_twitter_app()
        stream = Stream(auth, listener)
        stream.filter(track=hash_tag_list)


class TwitterListener(StreamListener):
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    '''
       This method shows the data that has been streamed
       In our case it prints the data on the screen and also
       writes  it in a file
    '''

    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True

        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True

    '''
        In the event of an error it prints the error
    '''

    def on_error(self, status):
        if status == 420:
            return False
        print(status)


if __name__ == '__main__':

    hash_tag_list = ['KenyanTraffic', 'Nairobi', 'Thika']
    fetched_tweets_filename = 'tweets.txt'

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)
