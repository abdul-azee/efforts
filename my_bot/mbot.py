import tweepy
import time

def reply_tweets():
    print("replying to tweets . . .")
    CONSUMER_KEY='mo6DVSskHxJmz5zXzs3s6zTeO'
    CONSUMER_SECRET='yfqtslorGsdKtQYCG3gLCKVp5NjQOFLc0NbJoot6UHGVJ371CQ'
    ACCESS_KEY='1290205834845200386-1oNz9qFCyYgIMmCUN3ae0V7BItzA4h'
    ACCESS_SECRET='ehVT63evML3J3mowovzhbElXTt8AwgSZgsBFpe7BqzWxl'

    auth=tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api=tweepy.API(auth,wait_on_rate_limit=True)


    FILE_NAME='last_seen_id.txt'

    def retrieve_last_id(file_name):
        f_read=open(file_name,'r')
        last_seen_id=int(f_read.read())
        f_read.close()
        return last_seen_id
    def store_last_id(file_name,last_seen_id):
        f_write=open(file_name,'w')
        f_write.write(str(last_seen_id))
        f_write.close()
        return
        
    #THE LAST SEEN ID FOR THIS CASE "1290232435708313600"
    last_seen_id=retrieve_last_id(FILE_NAME)
    mentions=api.mentions_timeline(last_seen_id,tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id)+"-"+mention.full_text)
        last_seen_id=mention.id
        store_last_id(FILE_NAME,last_seen_id)
        if '#helloworld' in mention.full_text.lower():
            print("Hello there")
            print("responding back . . .\n\n")
            api.update_status('@'+mention.user.screen_name+' #smile and have a good day',mention.id)
while True:
    reply_tweets()
    time.sleep(10)
