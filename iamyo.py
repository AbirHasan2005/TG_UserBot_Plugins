# Coded by @AbirHasan2005
# Telegram Group: http://t.me/linux_repo


from telethon import events

import asyncio

from userbot.utils import admin_cmd

@borg.on(admin_cmd("iamyo"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0,36)
    await event.edit("Hello")
    animation_chars = [
            "Bro",
            "I",
            "am",
            "a",
            "coder",
            "hacker",
            "skills"
            "git",
            "python",
            "ruby",
            "bash",
            "shell",
            "HTML",
            "PHP",
            "Nothing",
            "Much",
            "I",
            "am",
            "Abir",
            "Hasan",
            "Abir Hasan\n\n❤ @AbirHasan2005 ❤"
         ]
            

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])