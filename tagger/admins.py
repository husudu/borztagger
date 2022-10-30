from bot import bot
from telethon.events import NewMessage
from telethon.tl.types import ChannelParticipantsAdmins as cp
from config import muveqqeti_isleyen

@bot.on(NewMessage(pattern="^[@/]admins ?(.*)"))
@bot.on(NewMessage(pattern="^/admins@BORZTagger_bot"))
async def mentionall(event):
  global muveqqeti_isleyen
  say = 0
  if event.is_private:
    return
  if event.pattern_match.group(1):
    msg = event.pattern_match.group(1)
    muveqqeti_isleyen.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in bot.iter_participants(event.chat_id, filter=cp):
      say += 1
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id})"
      if event.chat_id not in muveqqeti_isleyen:
        await event.respond(f"**🆘 Adminləri çağırmaq Prosesi sonlandırıldı\n{say} Adminstrator qrupa çağırıldı**")
        say = 0
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
    async for usr in bot.iter_participants(event.chat_id, filter=cp):
      say += 1
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id})"
      if event.chat_id not in muveqqeti_isleyen:
        await event.respond(f"**🆘 Adminləri çağırmaq Prosesi Sonlandırıldı\n{say} Adminstrator qrupa çağırıldı**")
        say = 0
        return
      if usrnum == 5:
        await bot.send_message(event.chat_id, usrtxt)
        await sleep(2)
        usrnum = 0
        usrtxt = ""
