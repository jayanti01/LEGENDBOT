"""Fun pligon...for HardcoreUserbot
\nCode by @MYSTERIOUS_PLUGINS
type .sona and .bcha to see the fun.
"""
import random, re
from userbot.utils import admin_cmd
import asyncio
from telethon import events

@borg.on(admin_cmd(pattern="son ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("MELI")
        await asyncio.sleep(0.7)
        await event.edit("SONA")
        await asyncio.sleep(1)
        await event.edit("🥺")
        await asyncio.sleep(0.8)
        await event.edit("TU")
        await asyncio.sleep(0.9)
        await event.edit("ITI")
        await asyncio.sleep(1)
        await event.edit("CUTE")
        await asyncio.sleep(0.8)
        await event.edit("KYUN")
        await asyncio.sleep(0.7)
        await event.edit("H ALE ALE MELA BCHA ")
        await asyncio.sleep(1)
        await event.edit("I LOVE U MELI SONA 🙊 CHALI AB TUM VI BOLO🥺 LOVE YOU TOO")

@borg.on(events.NewMessage(pattern=r"\.nehi", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("AB DRAME NA KAR BOL DAL🙊")
    await asyncio.sleep(999)