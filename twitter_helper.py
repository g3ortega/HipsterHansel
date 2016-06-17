from os import environ
from ConfigParser import SafeConfigParser
from tweepy import OAuthHandler
from tweepy import API

parser = SafeConfigParser(environ)
parser.read('config.ini')

consumer_key = parser.get('Consumer', 'key')
consumer_secret = parser.get('Consumer', 'secret')
access_token = parser.get('Access', 'token')
access_token_secret = parser.get('Access', 'secret')
username = parser.get('Account', 'username')
account_screen_name = parser.get('Account', 'screen_name')
account_user_id = parser.get('Account', 'user_id')

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitterApi = API(auth)