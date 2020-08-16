# Coded by @AbirHasan2005
# Telegram Group: http://t.me/linux_repo


from telethon import events

import asyncio

from userbot.utils import admin_cmd

@borg.on(admin_cmd("hacking"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(0,11)
    #input_str = event.pattern_match.group(1)
    #if input_str == "Read This Telegraph Whole info here":
    await event.edit("`Starting ...`")
    animation_chars = [
            "`root@anon:~# `",
            "`root@anon:~# ls`",
            "`root@anon:~# ls`\n\n**  usr  ghost  codes  **\n\n`root@aono:~#`",
            "`root@anon:~# ls`\n\n**  usr  ghost  codes  **\n\n`root@aono:~# # So Let's Hack it ...`",
            "`root@anon:~# ls`\n\n**  usr  ghost  codes  **\n\n`root@aono:~# # So Let's Hack it ...`\n`root@anon:~# `",
            "`root@anon:~# ls`\n\n**  usr  ghost  codes  **\n\n`root@aono:~# # So Let's Hack it ...`\n`root@anon:~# touch setup.py`",
            "`root@anon:~# ls`\n\n**  usr  ghost  codes  **\n\n`root@aono:~# # So Let's Hack it ...`\n`root@anon:~# touch setup.py`\n\n**setup.py deployed ...**",
            "`root@anon:~# ls`\n\n**  usr  ghost  codes  **\n\n`root@aono:~# # So Let's Hack it ...`\n`root@anon:~# touch setup.py`\n\n**setup.py deployed ...**\n**Auto CMD deployed ...**",
            "`root@anon:~# ls`\n\n**  usr  ghost  codes  **\n\n`root@aono:~# # So Let's Hack it ...`\n`root@anon:~# touch setup.py`\n\n**setup.py deployed ...**\n**Auto CMD deployed ...**\n\n`root@anon:~# trap whoami`",
            "`root@anon:~# ls`\n\n**  usr  ghost  codes  **\n\n`root@aono:~# # So Let's Hack it ...`\n`root@anon:~# touch setup.py`\n\n**setup.py deployed ...**\n**Auto CMD deployed ...**\n\n`root@anon:~# trap whoami`\n\n**whoami=**`admin`",
            "`root@anon:~# ls`\n\n**  usr  ghost  codes  **\n\n`root@aono:~# # So Let's Hack it ...`\n`root@anon:~# touch setup.py`\n\n**setup.py deployed ...**\n**Auto CMD deployed ...**\n\n`root@anon:~# trap whoami`\n\n**whoami=**`admin`\n`boost_trap on force ...`",
            "`root@anon:~# ls`\n\n**  usr  ghost  codes  **\n\n`root@aono:~# # So Let's Hack it ...`\n`root@anon:~# touch setup.py`\n\n**setup.py deployed ...**\n**Auto CMD deployed ...**\n\n`root@anon:~# trap whoami`\n\n**whoami=**`admin`\n`boost_trap on force ...`\n`victim detected as `**NOOB**` in ghost ...`",
            "`root@anon:~# ls`\n\n**  usr  ghost  codes  **\n\n`root@aono:~# # So Let's Hack it ...`\n`root@anon:~# touch setup.py`\n\n**setup.py deployed ...**\n**Auto CMD deployed ...**\n\n`root@anon:~# trap whoami`\n\n**whoami=**`admin`\n`boost_trap on force ...`\n`victim detected as `**NOOB**` in ghost ...`\n\n**All Done!**",
            "`root@anon:~# ls`\n\n**  usr  ghost  codes  **\n\n`root@aono:~# # So Let's Hack it ...`\n`root@anon:~# touch setup.py`\n\n**setup.py deployed ...**\n**Auto CMD deployed ...**\n\n`root@anon:~# trap whoami`\n\n**whoami=**`admin`\n`boost_trap on force ...`\n`victim detected as `**NOOB**` in ghost ...`\n\n**All Done!**\n**Hacked!**\n**Token=**`DJ65gulO90P90nlkm65dRfc8I`",
         ]
            

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])