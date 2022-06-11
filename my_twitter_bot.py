import tweepy
import time
from keys import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

print('this is my twitter bot')

#creating auth object
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
#creating API object to talk to twitter, reads and sends data to twitter
api = tweepy.API(auth, wait_on_rate_limit=True)

#file name for last seen id txt
FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
	f_read = open(file_name, 'r')
	last_seen_id = int(f_read.read().strip())
	f_read.close()
	return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
	f_write = open(file_name, 'w')
	f_write.write(str(last_seen_id))
	f_write.close()
	return

#prints out mentions in a list

def reply_to_tweets():
	print('retrieving and replying to tweets...')
	last_seen_id = retrieve_last_seen_id(FILE_NAME)
	mentions = api.mentions_timeline(last_seen_id , tweet_mode = 'extended')

	#iterating through mentions list
	for mention in reversed(mentions):
		print(str(mention.id) + ' - ' + mention.full_text)
		last_seen_id = mention.id
		store_last_seen_id(last_seen_id, FILE_NAME)
		if '#stayinyourlane' in mention.full_text.lower():
			print('found stay in lane')
			print('responding back')
			api.update_status('@' + mention.user.screen_name +
				' I will beat MJ in a 1v1', mention.id)

while True:
	reply_to_tweets()
	time.sleep(5)