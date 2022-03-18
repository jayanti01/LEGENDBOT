# shayri plugin By @MYSTERIOUS_PLUGINS
"""garmi
Available Commands:
.garmi"""


import asyncio

from userbot.utils import admin_cmd


@borg.on(admin_cmd("garmi"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(0, 36)
    # input_str = event.pattern_match.group(1)
    # if input_str == "garmi":
    await event.edit("CHALI")
    animation_chars = [
        "GAYI",
        "GARMI",
        "��",
        "ANE WALI",
        "HAI THND",
        "�之",
        "AISI",
        "LDKI",
        "PATUNGA",
        "JO",
        "LAPK",
        "KE",
        "LEWE",
        "LUND",
        "�不",
        "��",
        "YEAHHHH",
        "CHALI GAYI GARMI ANE WALI H THND AISI LDKI PATUNGA JO �之LAPK KE LEWE LUND�不",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])