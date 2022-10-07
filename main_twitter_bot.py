import tweepy
import discord_bot
import time
import asyncio
import platform
import twitter_key_retriever

if platform.system() == 'Windows':
	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

#This code will post a picture named cat.jpg in the folder cat_storage onto your twitter page

# Authenticate to Twitter
auth = tweepy.OAuthHandler(twitter_key_retriever.get_key_1(), 
    twitter_key_retriever.get_key_2())
auth.set_access_token(twitter_key_retriever.get_key_3(), 
    twitter_key_retriever.get_key_4())

api = tweepy.API(auth)



try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

#timeline = api.home_timeline()
#api.update_status("")

#





def send_new_cat():
    media = api.media_upload(filename="cat_storage/cat.jpg") #File specification
    #print("MEDIA: ", media)

    tweet = api.update_status(status="", media_ids=[media.media_id_string]) #the part that tweets out the picture
    #print("TWEET: ", tweet)
    print("here tbot (cat sent)")
    print("---")

    discord_bot.main() #increment and get next cat

while True:
   # this will remain true forever
   send_new_cat()
   time.sleep(43200) #tweets a cat every 12 hours
