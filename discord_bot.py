"""
===========================================
Author: Codiacs
Github: github.com/MicroOptimization
===========================================
"""
import discord
import generic_key_retriever
import current_index
import asyncio
import io
import os
import platform
import cat_channel_retriever

#a guild is a discord server
def main():
    if platform.system() == 'Windows':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    class MyClient(discord.Client):

        async def download_image(self, msg, name): #downloads images locally
            the_attachment = msg.attachments[0]
            
            await the_attachment.save("cat_storage/" + str(name) + ".jpg")
        
        
        async def on_ready(self):
            #print("heeeere")
            print('Logged on as {0}!'.format(self.user))
            
            self.text_channel_names = []
            self.text_channels = []
            
            for i in client.get_all_channels():
                self.text_channel_names.append(str(i))
                self.text_channels.append(i)
                
            await client.change_presence(activity=discord.Game(name="with fire")) #sets bot activity status, prefaces with "playing"
            #cur_server = await self.fetch_guild("750636708462198854") #This is the ID of the coffeeshop ("750636708462198854")
            cat_channel = await self.fetch_channel(cat_channel_retriever.get_cat_channel()) #ig you don't need to get a guild to get a channel
            print("Channel name: " + cat_channel.name)
            
            messages = [message async for message in cat_channel.history(limit=123)]
            count = 0
            for i in messages:
                #print("i" , i)
                #print("--")
                #await self.download_image(i, count)
                count += 1 #use this to name the cat.
            cur_index = current_index.get_cur_index() #You put this function in another file for some reason. It reads out the current index from a text file

            cur_msg = messages[len(messages) - cur_index - 1]
            await self.download_image(cur_msg, "cat") #DOWNLOADS THE IMAGE
            print("here dbot (index advanced) | Total Number of Cat Pictures: " + str(len(messages)))
            
            await self.close()
                
        async def on_message(self, message):    
            print('Message from {0.author} from {0.channel}: {0.content}'.format(message))
            text = message.content
            words = text.split(" ")
            print(words)
            print(message.attachments[0]) #works on copy image
            #await download_attachment_from_message(message)

            
            #await self.download_image(message)
            
            id = 0 #Insert an ID int here
            
            
            #User_id comes from when you @ a user in a message that the bot detects.
            #user = client.get_user(int(user_id[2][3:-1]))
            #Allows you to DM another user if you use:
            #await user.send("Your Message")
    intents = discord.Intents.default()
    intents.members = True
    #print("here here here here here")
    client = MyClient(intents=intents) #problem line
    #print("here here here here")
    key = generic_key_retriever.get_key() #Insert your key here

    #print("here here here")
    client.run(key)
    


    
'''
counter = 0
async for message in channel.history(limit=200):
    if message.author == client.user:
        counter += 1
'''
#messages = [message async for message in channel.history(limit=123)]

