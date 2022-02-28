import discord
import time
from random import randint
from keep_alive import keep_alive

TOKEN = input('Please enter your Discord token (without quotes) ')
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!!init'):
        print('Starting Farm...')
        while True:
            await message.channel.send('pls beg')
            time.sleep(randint(17,22))
            await message.channel.send('pls fish')
            time.sleep(randint(3,5))
            await message.channel.send("pls sell fish all")
            time.sleep(randint(1,2))
            await message.channel.send("pls sell rarefish all")
            time.sleep(randint(1,2))
            await message.channel.send("pls sell jellyfish all")
            time.sleep(randint(2,4))
            await message.channel.send("pls sell seaweed all")
            time.sleep(randint(1,2))
            await message.channel.send("pls sell junk all")
            time.sleep(randint(1,2))
            await message.channel.send("pls sell trash all")
            time.sleep(randint(1,2))
            await message.channel.send("pls sell garbage all")
            time.sleep(randint(1,2))
            await message.channel.send("pls hunt")
            time.sleep(randint(3,5))
            await message.channel.send("pls sell skunk all")
            time.sleep(randint(1,2))
            await message.channel.send("pls sell rabbit all")
            time.sleep(randint(1,2))
            await message.channel.send("pls sell duck all")
            time.sleep(randint(1,2))
            await message.channel.send("pls sell deer all")
            time.sleep(randint(1,2))
            await message.channel.send("pls sell boar all")
            time.sleep(randint(3,5))
            await message.channel.send("pls dig")
            time.sleep(randint(3,5))
            await message.channel.send("pls sell junk all")
            time.sleep(randint(1,2))
            await message.channel.send("pls sell worm all")
            time.sleep(randint(1,2))
            await message.channel.send("pls sell ant all")
            time.sleep(randint(1,2))
            await message.channel.send("pls sell ladybug all")
            time.sleep(randint(3,5))
            await message.channel.send("pls sell stickbug all")
            time.sleep(randint(3,5))
            await message.channel.send("pls daily")
            time.sleep(randint(3,5))

    elif message.content.startswith('Catch'):
        time.sleep(6)
        await message.channel.send('pls buy fishingpole')
    elif message.content.startswith('Dodge'):
        time.sleep(6)
        await message.channel.send('pls buy huntingrifle')
        time.sleep(6)
        await message.channel.send('pls buy life')
    elif message.content.startswith('Look'):
        time.sleep(6)
        await message.channel.send('pls buy shovel')
    elif message.content.startswith('Dunk'):
        time.sleep(6)
        await message.channel.send('pls buy shovel')
    elif message.content.startswith('Hit'):
        time.sleep(6)
        await message.channel.send('pls buy shovel')

keep_alive()
client.run(TOKEN)
