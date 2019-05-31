#Convert tweet to 3d mesh.

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import os

from dotenv import load_dotenv
load_dotenv()


print(os.getenv('CONSUMER_KEY'))