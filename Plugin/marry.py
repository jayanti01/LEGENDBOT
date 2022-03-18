"""Fun pligon...for HardcoreUserbot
\nCode by @villagerboy1
type .marry and .jaan to see the fun.
"""
import random, re
from userbot.utils import admin_cmd
import asyncio
from telethon import events

@borg.on(admin_cmd(pattern="marry ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("I")
        await asyncio.sleep(0.7)
        await event.edit("LOVE")
        await asyncio.sleep(1)
        await event.edit("YOU")
        await asyncio.sleep(0.8)
        await event.edit("MY ")
        await asyncio.sleep(0.9)
        await event.edit("JAAN")
        await asyncio.sleep(1)
        await event.edit("WILL")
        await asyncio.sleep(0.8)
        await event.edit("YOU")
        await asyncio.sleep(0.7)
        await event.edit("MAARY ME IN FUTURE")
        await asyncio.sleep(0.9)
        await event.edit("I CAN DO ANYTHING FOR YOU")
        await asyncio.sleep(0.9)
        await event.edit("CREDIT @villagerboy1 ")
        await asyncio.sleep(0.8)
        await event.edit("MARRY ME I WILL FILL YOUR EVERYDAY WITH HAPPYNESS")
        await event.edit("I LOVE YOU MY JAAN WILL U MARRY ME IN FUTURE I CAN DO ANYTHING FOR YOU MARRY ME I WILL FILL YOUR EVERYDAY WITH HAPPYNESS 😍💍")

@borg.on(events.NewMessage(pattern=r"\.nehi", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("AB DRAME NA KAR I LOVE YOU TOO BOL DAL❤️")
    await asyncio.sleep(999)