import asyncio

from uniborg.util import admin_cmd
from userbot import ALIVE_NAME

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Love U BABE"
 #credit - @MYSTERIOUS_PLUGINS

@borg.on(admin_cmd(pattern=r"lob"))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 12)

    await event.edit("lOVE YOU")

    animation_chars = [
        "❤️❤️❤️❤️⬜⬜⬜💙💙💙💙\n❤️❤️❤️⬜⬜⬜💙💙💙💙\n❤️❤️❤️⬜⬜⬜💙💙",
        "💙💙💙⬜⬜⬜❤️❤️❤️\n💙💙💙⬜⬜⬜💙💙💙\n💙💙💙⬜⬜⬜❤️❤️❤️",
        "❤️❤️❤️⬜⬜⬜💙💙💙\n❤️❤️❤️⬜⬜⬜💙💙💙💙\n❤️❤️❤️⬜⬜⬜💙💙💙",
        "💙💙💙⬜⬜⬜❤️❤️❤️\n💙💙💙⬜⬜⬜❤️❤️❤️\n💙💙💙⬜⬜⬜❤️❤️❤️",
        "❤️❤️❤️⬜⬜⬜💙💙💙\n❤️❤️❤️⬜⬜⬜💙💙💙\n❤️❤️❤️⬜⬜⬜💙💙💙",
        "💙💙💙⬜⬜⬜❤️❤️❤️\n💙💙💙⬜⬜⬜❤️❤️❤️\n💙💙💙⬜⬜⬜❤️❤️❤️",
        "💙💙💙⬜⬜⬜💙💙💙\n❤️❤️❤️⬜⬜⬜💙💙💙\n❤️❤️❤️⬜⬜⬜💙💙💙",
        "💙💙💙⬜⬜⬜❤️❤️❤️\n💙💙💙⬜⬜⬜❤️❤️❤️\n💙💙💙⬜⬜⬜❤️❤️❤️",
        "❤️❤️❤️⬜⬜⬜💙💙💙\n❤️❤️❤️⬜⬜⬜💙💙💙\n❤️❤️❤️⬜⬜⬜💙💙💙",
        "💙💙💙⬜⬜⬜❤️❤️❤️\n💙💙💙⬜⬜⬜❤️❤️❤️\n💙💙💙⬜⬜⬜❤️❤️❤️",
        "❤️❤️❤️⬜⬜⬜💙💙💙\n❤️❤️❤️⬜⬜⬜💙💙💙\n❤️❤️❤️⬜⬜⬜💙💙💙",
        "[😘LOVELY LOVE😘",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 12])