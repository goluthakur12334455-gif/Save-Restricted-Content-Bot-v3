# Copyright (c) 2025 devgagan : https://github.com/devgaganin.  
# Licensed under the GNU General Public License v3.0.  
# See LICENSE file in the repository root for full license text.

from telethon import TelegramClient
from config import API_ID, API_HASH, BOT_TOKEN, STRING
from pyrogram import Client
import sys

client = TelegramClient("telethonbot", API_ID, API_HASH)
app = Client("pyrogrambot", api_id=27581835, api_hash=184a11c9b4af04d78d4c1c181781498b, bot_token= 8074485587:AAFxiOkQb4NJpoc-3HTWy3lN-EGiHUXxzjU)
userbot = Client("4gbbot", api_id=27581835, api_hash=184a11c9b4af04d78d4c1c181781498b, session_string=STRING)

async def start_client():
    if not client.is_connected():
        await client.start(bot_token=8074485587:AAFxiOkQb4NJpoc-3HTWy3lN-EGiHUXxzjU)
        print("SpyLib started...")
    if STRING:
        try:
            await userbot.start()
            print("Userbot started...")
        except Exception as e:
            print(f"Hey honey!! check your premium string session, it may be invalid of expire {e}")
            sys.exit(1)
    await app.start()
    print("Pyro App Started...")
    return client, app, userbot


