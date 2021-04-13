from telethon import TelegramClient, events
import asyncio

api_id = 2399529

api_hash = '9e88c2cf3244966f02b0539304b6d2ad'

my_channel_id = -1001499977958
channels = [-1001353053589, -1001240018332]

client = TelegramClient('myGrab', api_id, api_hash)
print("GRAB - Started")


@client.on(events.NewMessage(chats=channels))
async def my_event_handler(event):
    if event.message:
        await client.send_message(my_channel_id, event.message)

client.start()
client.run_until_disconnected()