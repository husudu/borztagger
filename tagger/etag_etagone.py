from bot import bot
from random import choice
from asyncio import sleep
from telethon.events import NewMessage
from config import muveqqeti_isleyen
from telethon.tl.types import ChannelParticipantsAdmins

emoji = "😀 😃 😄 😁 😆 😅 😂 🤣 😭 😗 😙 😚 😘 🥰 😍 🤩 🥳 🤗 🙃 🙂 ☺️ 😊 😏 😌 😉 🤭 😶 😐 😑 😔 😋 😛 😝 😜 🤪 🤔 🤨 🧐 🙄 😒 😤 😠 🤬 ☹️ 🙁 😕 😟 🥺 😳 😬 🤐 🤫 😰 😨 😧 😦 😮 😯 😲 😱 🤯 😢 😥 😓 😞 😖 😣 😩 😫 🤤 🥱 😴 😪 🌛 🌜 🌚 🌝 🎲 🧩 ♟ 🎯 🎳 🎭💕 💞 💓 💗 💖 ❤️‍🔥 💔 🤎 🤍 🖤 ❤️ 🧡 💛 💚 💙 💜 💘 💝 🐵 🦁 🐯 🐱 🐶 🐺 🐻 🐨 🐼 🐹 🐭 🐰 🦊 🦝 🐮 🐷 🐽 🐗 🦓 🦄 🐴 🐸 🐲 🦎 🐉 🦖 🦕 🐢 🐊 🐍 🐁 🐀 🐇 🐈 🐩 🐕 🦮 🐕‍🦺 🐅 🐆 🐎 🐖 🐄 🐂 🐃 🐏 🐑 🐐 🦌 🦙 🦥 🦘 🐘 🦏 🦛 🦒 🐒 🦍 🦧 🐪 🐫 🐿️ 🦨 🦡 🦔 🦦 🦇 🐓 🐔 🐣 🐤 🐥 🐦 🦉 🦅 🦜 🕊️ 🦢 🦩 🦚 🦃 🦆 🐧 🦈 🐬 🐋 🐳 🐟 🐠 🐡 🦐 🦞 🦀 🦑 🐙 🦪 🦂 🕷️ 🦋 🐞 🐝 🦟 🦗 🐜 🐌 🐚 🕸️ 🐛 🐾 🌞 🤢 🤮 🤧 🤒 🍓 🍒 🍎 🍉 🍑 🍊 🥭 🍍 🍌 🌶 🍇 🥝 🍐 🍏 🍈 🍋 🍄 🥕 🍠 🧅 🌽 🥦 🥒 🥬 🥑 🥯 🥖 🥐 🍞 🥜 🌰 🥔 🧄 🍆 🧇 🥞 🥚 🧀 🥓 🥩 🍗 🍖 🥙 🌯 🌮 🍕 🍟 🥨 🥪 🌭 🍔 🧆 🥘 🍝 🥫 🥣 🥗 🍲 🍛 🍜 🍢 🥟 🍱 🍚 🥡 🍤 🍣 🦞 🦪 🍘 🍡 🥠 🥮 🍧 🍨".split(" ")

@bot.on(NewMessage(pattern="^/etag@BORZTagger_bot"))
@bot.on(NewMessage(pattern="^/etag ?(.*)"))
async def etag(event):
  global muveqqeti_isleyen
  if event.is_private:
    return
  admins = []
  say = 0
  e_ad = choice(emoji)
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
      say += 1
      usrnum += 1
      usrtxt += f"[{e_ad}](tg://user?id={usr.id})"
      if event.chat_id not in muveqqeti_isleyen:
        await event.respond(f"**🆘 Emojilərlə Dəvət Prosesi sonlandırıldı\n{say} İstifadəçi qrupa çağırıldı**")
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
    async for usr in bot.iter_participants(event.chat_id):
      say += 1
      usrnum += 1
      usrtxt += f"[{e_ad}](tg://user?id={usr.id})"
      if event.chat_id not in muveqqeti_isleyen:
        await event.respond(f"🆘 Emojillərlə Dəvət Prosesi Sonlandırıldı\n{say} İstifadəçi qrupa çağırıldı")
        say = 0
        return
      if usrnum == 5:
        await bot.send_message(event.chat_id, usrtxt)
        await sleep(2)
        usrnum = 0
        usrtxt = ""

@bot.on(NewMessage(pattern="^/etagone@BORZTagger_bot"))
@bot.on(NewMessage(pattern="^/etagone ?(.*)"))
async def etagone(event):
  global muveqqeti_isleyen
  if event.is_private:
    return
  admins = []
  say = 0
  e_ad = choice(emoji)
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
      say += 1
      usrnum += 1
      usrtxt += f"[{e_ad}](tg://user?id={usr.id})"
      if event.chat_id not in muveqqeti_isleyen:
        await event.respond(f"**🆘 Emojilərlə Dəvət Prosesi sonlandırıldı\n{say} İstifadəçi Qrupa çağırıldı**")
        say = 0
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
      usrtxt += f"[{e_ad}](tg://user?id={usr.id})"
      if event.chat_id not in muveqqeti_isleyen:
        await event.respond(f"🆘 Emojilərlə Dəvət Prosesi Sonlandırıldı\n{say} İstifadəçi qrupa çağırıldı")
        say = 0
        return
      if usrnum == 1:
        await bot.send_message(event.chat_id, usrtxt)
        await sleep(2)
        usrnum = 0
        usrtxt = ""
