from bot import bot
from config import muveqqeti_isleyen, taglanan
from telethon.events import NewMessage
from telethon.tl.types import ChannelParticipantsAdmins


@bot.on(NewMessage(pattern="^/speedonetag ?(.*)"))
@bot.on(NewMessage(pattern="^/speedonetag@BORZTagger_bot"))
async def speedtag(event):
  global muveqqeti_isleyen
  global taglanan
  if event.is_private:
    return
  say = 0
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
      taglanan += 1
      say += 1
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id})"
      if event.chat_id not in muveqqeti_isleyen:
        await event.respond(f"**🆘 Sürətli Dəvət Prosesi sonlandırıldı\n{say} İstifadəçi qrupa çağırıldı**")
        say = 0
        return
      if usrnum == 5:
        await bot.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await sleep(0.5)
        usrnum = 0
        usrtxt = ""
  else:
    muveqqeti_isleyen.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in bot.iter_participants(event.chat_id):
      taglanan += 1
      say += 1
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id})"
      if event.chat_id not in muveqqeti_isleyen:
        await event.respond(f"**🆘 Sürətli Dəvət Prosesi Sonlandırıldı\n{say} İstifadəçi qrupa çağırıldı**")
        say = 0
        return
      if usrnum == 5:
        await bot.send_message(event.chat_id, usrtxt)
        await sleep(0.5)
        usrnum = 0
        usrtxt = ""


@bot.on(NewMessage(pattern="^/speedtag ?(.*)"))
@bot.on(NewMessage(pattern="^/speedtag@BORZTagger_bot"))
async def speedtag(event):
  global muveqqeti_isleyen
  global taglanan
  if event.is_private:
    return
  say = 0
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
      taglanan += 1
      say += 1
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id})"
      if event.chat_id not in muveqqeti_isleyen:
        await event.respond(f"**🆘 Sürətli Dəvət Prosesi sonlandırıldı\n{say} İstifadəçi qrupa çağırıldı**")
        say = 0
        return
      if usrnum == 1:
        await bot.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await sleep(0.5)
        usrnum = 0
        usrtxt = ""
  else:
    muveqqeti_isleyen.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in bot.iter_participants(event.chat_id):
      taglanan += 1
      say += 1
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id})"
      if event.chat_id not in muveqqeti_isleyen:
        await event.respond(f"**🆘 Sürətli Dəvət Prosesi Sonlandırıldı\n{say} İstifadəçi qrupa çağırıldı")
        say = 0
        return
      if usrnum == 1:
        await bot.send_message(event.chat_id, usrtxt)
        await sleep(0.5)
        usrnum = 0
        usrtxt = ""
