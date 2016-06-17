import json
import twitter_helper
from tweepy.streaming import StreamListener
from nltk.chat import eliza

chatbot = eliza.Chat(eliza.pairs)

class ReplyToTweet(StreamListener):

    def on_data(self, data):
        print data
        tweet = json.loads(data.strip())

        retweeted = tweet.get('retweeted')
        from_self = tweet.get('user', {}).get('id_str', '') == twitter_helper.account_user_id

        if retweeted is not None and not retweeted and not from_self:

            tweetId = tweet.get('id_str')
            screenName = tweet.get('user', {}).get('screen_name')
            tweetText = tweet.get('text')

            chatResponse = chatbot.respond(tweetText)

            replyText = '@' + screenName + ' ' + chatResponse

            if len(replyText) > 140:
                replyText = replyText[0:139] + '...'

            print('Tweet ID: ' + tweetId)
            print('From: ' + screenName)
            print('Tweet Text: ' + tweetText)
            print('Reply Text: ' + replyText)

            twitter_helper.twitterApi.update_status(status=replyText, in_reply_to_status_id=tweetId)

    def on_error(self, status):
        print status
