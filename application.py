import tweetbot
import twitter_helper
import multiprocessing
from tweepy import Stream
from flask import Flask


def start_bot():
    streamListener = tweetbot.ReplyToTweet()
    twitterStream = Stream(twitter_helper.auth, streamListener)
    twitterStream.userstream(_with='user')

def start_server():
    application.debug = True
    application.run()

header_text = '''
    <html>\n<head> <title>Hipster Hansel</title> </head>\n<body>'''

instructions = '''
    <p><em>About</em>: A hipster twitter bot in training.</p>\n'''

footer_text = '</body>\n</html>'

application = Flask(__name__)

application.add_url_rule('/', 'index', (lambda: header_text +
    instructions + footer_text))


if __name__ == "__main__":
    # TODO: Try threads instead of process, or Celery background tasks
    bot = multiprocessing.Process(name='start_bot', target=start_bot)
    server = multiprocessing.Process(name='start_server', target=start_server)
    bot.start()
    # server.start()



