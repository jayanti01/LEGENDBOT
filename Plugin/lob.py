import asyncio

from userbot.utils import admin_cmd

 #credit - @villagerboy1

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
        "😘",
        "🤩",
        "🤗",
        "ale mela bachcha mele sona mele mona 😘😘😘😘",
        "i lobe uhh meri jaan🤩",
        "lao ab kissi do😅",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 12])