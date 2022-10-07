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
    if platform.system() == 'Windows': #I also have no idea what this does, fixes a few bugs though
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    class MyClient(discord.Client):
        async def download_image(self, msg, name): #downloads images locally
            the_attachment = msg.attachments[0]
            
            await the_attachment.save("cat_storage/" + str(name) + ".jpg")
        
        
        async def on_ready(self):
            print('Logged on as {0}!'.format(self.user))
            
            self.text_channel_names = []
            self.text_channels = []
            
            for i in client.get_all_channels():
                self.text_channel_names.append(str(i))
                self.text_channels.append(i)
                
            await client.change_presence(activity=discord.Game(name="with fire")) #sets bot activity status, prefaces with "playing" #Optional
            cat_channel = await self.fetch_channel(cat_channel_retriever.get_cat_channel()) #ig you don't need to get a guild to get a channel
            #print("Channel name: " + cat_channel.name)
            
            messages = [message async for message in cat_channel.history(limit=123)]
            count = 0
            for i in messages:
                count += 1 #use this to name the cat. #You don't use this for anything anymore.
            cur_index = current_index.get_cur_index() #You put this function in another file for some reason. It reads out the current index from a text file

            cur_msg = messages[len(messages) - cur_index - 1]
            await self.download_image(cur_msg, "cat") #DOWNLOADS THE IMAGE from the discord channel
            #print("here dbot (index advanced) | Total Number of Cat Pictures: " + str(len(messages))) #useful for debugging
            
            await self.close()
            
    intents = discord.Intents.default()
    intents.members = True
    client = MyClient(intents=intents) 
    key = generic_key_retriever.get_key() #Insert your key here

    client.run(key)

