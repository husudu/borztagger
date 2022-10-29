from bot import bot
from asyncio import sleep
from telethon.events import NewMessage
from config import muveqqeti_isleyen
from telethon.tl.types import ChannelParticipantsAdmins


@bot.on(NewMessage(pattern="@all ?(.*)"))
@bot.on(NewMessage(pattern="^/all ?(.*)"))
@bot.on(NewMessage(pattern="^/all@BORZTagger_bot"))
async def mentionall(event):
  global muveqqeti_isleyen
  if event.is_private:
    return
  admins = []
  async for admin in bot.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**👨🏻‍🔧 Bu əmri sadəcə adminlər işlədə bilər**")
  if event.pattern_match.group(1):
    msg = event.pattern_match.group(1)
    muveqqeti_isleyen.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in bot.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id})"
      if event.chat_id not in anlik_calisan:
        await event.respond("**🆘 Dəvət Prosesi sonlandırıldı**")
        return
      if usrnum == 5:
        await bot.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await sleep(2)
        usrnum = 0
        usrtxt = ""
  else:
    muveqqeti_isleyen.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in bot.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id})"
      if event.chat_id not in muveqqeti_isleyen:
        await event.respond("🆘 5-5 Dəvət Prosesi Sonlandırıldı")
        return
      if usrnum == 5:
        await bot.send_message(event.chat_id, usrtxt)
        await sleep(2)
        usrnum = 0
        usrtxt = ""

@bot.on(NewMessage(pattern="^/tagone@BORZTagger_bot"))
@bot.on(NewMessage(pattern="^/tagone ?(.*)"))
async def tagone(event):
  global muveqqeti_isleyen
  if event.is_private:
    return
  admins = []
  async for admin in bot.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**👨🏻‍🔧 Bu əmri sadəcə adminlər işlədə bilər**")
  if event.pattern_match.group(1):
    msg = event.pattern_match.group(1)
    msg = event.reply_to_msg_id
    muveqqeti_isleyen.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in bot.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id})"
      if event.chat_id not in anlik_calisan:
        await event.respond("**🆘 Tək-Tək Dəvət Prosesi sonlandırıldı**")
        return
      if usrnum == 1:
        await bot.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await sleep(2)
        usrnum = 0
        usrtxt = ""
  else:
    muveqqeti_isleyen.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in bot.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id})"
      if event.chat_id not in muveqqeti_isleyen:
        await event.respond("🆘 Tək-Tək Dəvət Prosesi Sonlandırıldı")
        return
      if usrnum == 1:
        await bot.send_message(event.chat_id, usrtxt)
        await sleep(2)
        usrnum = 0
        usrtxt = ""
