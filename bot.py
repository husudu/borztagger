from config import API_ID, API_HASH, BOT_TOKEN, owners
from telethon import TelegramClient, Button, events
from telethon.events import NewMessage
from telethon.tl.types import ChannelParticipantsAdmins as cp
import telethon, time
from random import choice
from asyncio import sleep
from data.db import add_served_chat, add_served_user, set_cagirma, get_served_chats, get_served_users, get_cagirma

bot = TelegramClient("borztagger", api_id=API_ID, api_hash=API_HASH).start(bot_token=BOT_TOKEN)

muveqqeti_isleyen = []
photo = "data/IMG_20221031_014515_509.jpg"
buttons = ([Button.url('➕ Məni Qrupa əlavə et', 'https://t.me/BORZTagger_bot?startgroup=start')], [Button.url('👨🏻‍🔧 Dəstək', 'https://t.me/BorzSohbet'), Button.url('Rəsmi Kanal📣', 'https://t.me/BORZBots')])
qrup = "Əlavə Məlumat üçün özəl söhbətdə məni başladın"
tag = "@BORZTagger_bot"
helptext = """💎 BORZ Tagger botunun əmr siyahısı:
/all və ya @all - İstifadəçiləri 5-5 qrupa çağırmaq üçün
/onetag - İstifadəçiləri tək-tək qrupa çağırmaq üçün
/etag - İstifadəçiləri Emosilayalarla 5-5 qrupa çağırmaq üçün
/eonetag - İstifadəçiləri Emosiyalarla tək-tək qrupa çağırmaq üçün
/speedtag - İstifadəçiləri Sürətli formada 5-5 qrupa çağırmaq üçün
/speedonetag - İstifadəçiləri Sürətli formada tək-tək qrupa çağırmaq üçün
/admins - Qrupun adminlərini çağırmaq üçün
/stop - Tag prosesini sonlandırar
"""

@bot.on(NewMessage(pattern="^/start$|start@BORZTagger_bot"))
async def start(event):
  text = "Salam mən **💎 BORZ Tagger!**\nMənim Sayəmdə qruplarınızda olan istifadəçiləri maraqlı şəkildə qrupa çağıra bilərsiniz"
  if event.is_private:
    await bot.send_file(event.chat.id, file=photo, caption=text, buttons=buttons)
  else:
    await bot.send_message(event.chat.id, qrup,
                    buttons=(
		      [Button.url('Botla özəl söhbət', 'https://t.me/BORZTagger_bot?start=start')],
                    ),
                    link_preview=False
                   )


@bot.on(NewMessage(pattern="^/help$|help@BORZTagger_bot"))
async def help(event):
  if event.is_private:
    await bot.send_message(event.chat.id, helptext)
  else:
    await bot.send_message(event.chat.id, qrup,
                    buttons=(
		      [Button.url('Botla özəl söhbət', 'https://t.me/BORZTagger_bot?start=start')],
                    ),
                    link_preview=False
                   )


@bot.on(NewMessage(pattern='^/stop$|stop@BORZTagger_bot'))
async def stop(event):
  global muveqqeti_isleyen
  if event.is_private:
    return
  else:
    muveqqeti_isleyen.remove(event.chat_id)


@bot.on(NewMessage(pattern="^[@/]admins ?(.*)"))
async def mentionall(event):
  global muveqqeti_isleyen
  say = 0
  if event.is_private:
    return
  if event.pattern_match.group(1) == tag:
    muveqqeti_isleyen.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in bot.iter_participants(event.chat_id, filter=cp):
      set_cagirma(1)
      say += 1
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}), "
      if event.chat_id not in muveqqeti_isleyen:
        say -= 1
        await event.respond(f"**🆘 Adminləri çağırmaq Prosesi Sonlandırıldı\n{say} Adminstrator qrupa çağırıldı**")
        say = 0
        return
      if usrnum == 5:
        await bot.send_message(event.chat_id, usrtxt)
        await sleep(2)
        usrnum = 0
        usrtxt = ""
  elif event.pattern_match.group(1):
    msg = event.pattern_match.group(1)
    muveqqeti_isleyen.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in bot.iter_participants(event.chat_id, filter=cp):
      set_cagirma(1)
      say += 1
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}), "
      if event.chat_id not in muveqqeti_isleyen:
        say -= 1
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
      set_cagirma(1)
      say += 1
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}), "
      if event.chat_id not in muveqqeti_isleyen:
        say -= 1
        await event.respond(f"**🆘 Adminləri çağırmaq Prosesi Sonlandırıldı\n{say} Adminstrator qrupa çağırıldı**")
        say = 0
        return
      if usrnum == 5:
        await bot.send_message(event.chat_id, usrtxt)
        await sleep(2)
        usrnum = 0
        usrtxt = ""


@bot.on(NewMessage(pattern="^[@/]all ?(.*)"))
async def mentionall(event):
  global muveqqeti_isleyen
  if event.is_private:
    return
  say = 0
  admins = []
  async for admin in bot.iter_participants(event.chat_id, filter=cp):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**👨🏻‍🔧 Bu əmri sadəcə adminlər işlədə bilər**")
  if event.pattern_match.group(1) == tag:
    muveqqeti_isleyen.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in bot.iter_participants(event.chat_id):
      set_cagirma(1)
      say += 1
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}), "
      if event.chat_id not in muveqqeti_isleyen:
        say -= 1
        await event.respond(f"🆘 5-5 Dəvət Prosesi Sonlandırıldı\n{say} İstifadəçi qrupa çağırıldı")
        say = 0
        return
      if usrnum == 5:
        await bot.send_message(event.chat_id, usrtxt)
        await sleep(2)
        usrnum = 0
        usrtxt = ""
  elif event.pattern_match.group(1):
    msg = event.pattern_match.group(1)
    muveqqeti_isleyen.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in bot.iter_participants(event.chat_id):
      set_cagirma(1)
      say += 1
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}), "
      if event.chat_id not in muveqqeti_isleyen:
        say -= 1
        await event.respond(f"**🆘 5-5 Dəvət Prosesi sonlandırıldı\n{say} İstifadəçi qrupa çağırıldı**")
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
      set_cagirma(1)
      say += 1
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}), "
      if event.chat_id not in muveqqeti_isleyen:
        say -= 1
        await event.respond(f"🆘 5-5 Dəvət Prosesi Sonlandırıldı\n{say} İstifadəçi qrupa çağırıldı")
        say = 0
        return
      if usrnum == 5:
        await bot.send_message(event.chat_id, usrtxt)
        await sleep(2)
        usrnum = 0
        usrtxt = ""


@bot.on(NewMessage(pattern="^/tagone ?(.*)"))
async def tagone(event):
  global muveqqeti_isleyen
  if event.is_private:
    return
  say = 0
  admins = []
  async for admin in bot.iter_participants(event.chat_id, filter=cp):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**👨🏻‍🔧 Bu əmri sadəcə adminlər işlədə bilər**")
  if event.pattern_match.group(1) == tag:
    muveqqeti_isleyen.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in bot.iter_participants(event.chat_id):
      set_cagirma(1)
      say += 1
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}), "
      if event.chat_id not in muveqqeti_isleyen:
        say -= 1
        await event.respond(f"🆘 Tək-Tək Dəvət Prosesi Sonlandırıldı\n{say} İstifadəçi qrupa çağırıldı")
        say = 0
        return
      if usrnum == 1:
        await bot.send_message(event.chat_id, usrtxt)
        await sleep(2)
        usrnum = 0
        usrtxt = ""
  elif event.pattern_match.group(1):
    msg = event.pattern_match.group(1)
    msg = event.reply_to_msg_id
    muveqqeti_isleyen.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in bot.iter_participants(event.chat_id):
      set_cagirma(1)
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}), "
      if event.chat_id not in muveqqeti_isleyen:
        say -= 1
        await event.respond(f"**🆘 Tək-Tək Dəvət Prosesi sonlandırıldı\n{say} İstifadəçi qrupa çağırıldı**")
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
      set_cagirma(1)
      say += 1
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}), "
      if event.chat_id not in muveqqeti_isleyen:
        say -= 1
        await event.respond(f"🆘 Tək-Tək Dəvət Prosesi Sonlandırıldı\n{say} İstifadəçi qrupa çağırıldı")
        say = 0
        return
      if usrnum == 1:
        await bot.send_message(event.chat_id, usrtxt)
        await sleep(2)
        usrnum = 0
        usrtxt = ""


emoji = "😀 😃 😄 😁 😆 😅 😂 🤣 😭 😗 😙 😚 😘 🥰 😍 🤩 🥳 🤗 🙃 🙂 ☺️ 😊 😏 😌 😉 🤭 😶 😐 😑 😔 😋 😛 😝 😜 🤪 🤔 🤨 🧐 🙄 😒 😤 😠 🤬 ☹️ 🙁 😕 😟 🥺 😳 😬 🤐 🤫 😰 😨 😧 😦 😮 😯 😲 😱 🤯 😢 😥 😓 😞 😖 😣 😩 😫 🤤 🥱 😴 😪 🌛 🌜 🌚 🌝 🎲 🧩 ♟ 🎯 🎳 🎭💕 💞 💓 💗 💖 ❤️‍🔥 💔 🤎 🤍 🖤 ❤️ 🧡 💛 💚 💙 💜 💘 💝 🐵 🦁 🐯 🐱 🐶 🐺 🐻 🐨 🐼 🐹 🐭 🐰 🦊 🦝 🐮 🐷 🐽 🐗 🦓 🦄 🐴 🐸 🐲 🦎 🐉 🦖 🦕 🐢 🐊 🐍 🐁 🐀 🐇 🐈 🐩 🐕 🦮 🐕‍🦺 🐅 🐆 🐎 🐖 🐄 🐂 🐃 🐏 🐑 🐐 🦌 🦙 🦥 🦘 🐘 🦏 🦛 🦒 🐒 🦍 🦧 🐪 🐫 🐿️ 🦨 🦡 🦔 🦦 🦇 🐓 🐔 🐣 🐤 🐥 🐦 🦉 🦅 🦜 🕊️ 🦢 🦩 🦚 🦃 🦆 🐧 🦈 🐬 🐋 🐳 🐟 🐠 🐡 🦐 🦞 🦀 🦑 🐙 🦪 🦂 🕷️ 🦋 🐞 🐝 🦟 🦗 🐜 🐌 🐚 🕸️ 🐛 🐾 🌞 🤢 🤮 🤧 🤒 🍓 🍒 🍎 🍉 🍑 🍊 🥭 🍍 🍌 🌶 🍇 🥝 🍐 🍏 🍈 🍋 🍄 🥕 🍠 🧅 🌽 🥦 🥒 🥬 🥑 🥯 🥖 🥐 🍞 🥜 🌰 🥔 🧄 🍆 🧇 🥞 🥚 🧀 🥓 🥩 🍗 🍖 🥙 🌯 🌮 🍕 🍟 🥨 🥪 🌭 🍔 🧆 🥘 🍝 🥫 🥣 🥗 🍲 🍛 🍜 🍢 🥟 🍱 🍚 🥡 🍤 🍣 🦞 🦪 🍘 🍡 🥠 🥮 🍧 🍨".split(" ")

@bot.on(NewMessage(pattern=f"^/etag ?(.*)|etag{tag}$"))
async def etag(event):
  global muveqqeti_isleyen
  if event.is_private:
    return
  admins = []
  say = 0
  async for admin in bot.iter_participants(event.chat_id, filter=cp):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**👨🏻‍🔧 Bu əmri sadəcə adminlər işlədə bilər**")  
  if event.pattern_match.group(1) == tag:
    muveqqeti_isleyen.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in bot.iter_participants(event.chat_id):
      set_cagirma(1)
      say += 1
      usrnum += 1
      usrtxt += f"[{choice(emoji)}](tg://user?id={usr.id}), "
      if event.chat_id not in muveqqeti_isleyen:
        say -= 1
        await event.respond(f"🆘 Emojillərlə Dəvət Prosesi Sonlandırıldı\n{say} İstifadəçi qrupa çağırıldı")
        say = 0
        return
      if usrnum == 5:
        await bot.send_message(event.chat_id, usrtxt)
        await sleep(2)
        usrnum = 0
        usrtxt = ""
  elif event.pattern_match.group(1):
    msg = event.pattern_match.group(1)
    muveqqeti_isleyen.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in bot.iter_participants(event.chat_id):
      set_cagirma(1)
      say += 1
      usrnum += 1
      usrtxt += f"[{choice(emoji)}](tg://user?id={usr.id}), "
      if event.chat_id not in muveqqeti_isleyen:
        say -= 1
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
      set_cagirma(1)
      say += 1
      usrnum += 1
      usrtxt += f"[{choice(emoji)}](tg://user?id={usr.id}), "
      if event.chat_id not in muveqqeti_isleyen:
        say -= 1
        await event.respond(f"🆘 Emojillərlə Dəvət Prosesi Sonlandırıldı\n{say} İstifadəçi qrupa çağırıldı")
        say = 0
        return
      if usrnum == 5:
        await bot.send_message(event.chat_id, usrtxt)
        await sleep(2)
        usrnum = 0
        usrtxt = ""

@bot.on(NewMessage(pattern="^/etagone ?(.*)"))
async def etagone(event):
  global muveqqeti_isleyen
  if event.is_private:
    return
  admins = []
  say = 0
  e_ad = choice(emoji)
  async for admin in bot.iter_participants(event.chat_id, filter=cp):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**👨🏻‍🔧 Bu əmri sadəcə adminlər işlədə bilər**")  
  if event.pattern_match.group(1) == tag:
    muveqqeti_isleyen.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in bot.iter_participants(event.chat_id):
      set_cagirma(1)
      usrnum += 1
      usrtxt += f"[{choice(emoji)}](tg://user?id={usr.id}), "
      if event.chat_id not in muveqqeti_isleyen:
        say -= 1
        await event.respond(f"🆘 Emojilərlə Dəvət Prosesi Sonlandırıldı\n{say} İstifadəçi qrupa çağırıldı")
        say = 0
        return
      if usrnum == 1:
        await bot.send_message(event.chat_id, usrtxt)
        await sleep(2)
        usrnum = 0
        usrtxt = ""
  elif event.pattern_match.group(1):
    msg = event.pattern_match.group(1)
    muveqqeti_isleyen.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in bot.iter_participants(event.chat_id):
      set_cagirma(1)
      say += 1
      usrnum += 1
      usrtxt += f"[{choice(emoji)}](tg://user?id={usr.id}), "
      if event.chat_id not in muveqqeti_isleyen:
        say -= 1
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
      set_cagirma(1)
      usrnum += 1
      usrtxt += f"[{choice(emoji)}](tg://user?id={usr.id}), "
      if event.chat_id not in muveqqeti_isleyen:
        say -= 1
        await event.respond(f"🆘 Emojilərlə Dəvət Prosesi Sonlandırıldı\n{say} İstifadəçi qrupa çağırıldı")
        say = 0
        return
      if usrnum == 1:
        await bot.send_message(event.chat_id, usrtxt)
        await sleep(2)
        usrnum = 0
        usrtxt = ""


@bot.on(NewMessage(pattern="^/speedonetag ?(.*)"))
async def speedtag(event):
  global muveqqeti_isleyen
  if event.is_private:
    return
  say = 0
  admins = []
  async for admin in bot.iter_participants(event.chat_id, filter=cp):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**👨🏻‍🔧 Bu əmri sadəcə adminlər işlədə bilər**")
  if event.pattern_match.group(1) == tag:
    muveqqeti_isleyen.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in bot.iter_participants(event.chat_id):
      set_cagirma(1)
      say += 1
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}), "
      if event.chat_id not in muveqqeti_isleyen:
        say -= 1
        await event.respond(f"**🆘 Sürətli Dəvət Prosesi Sonlandırıldı\n{say} İstifadəçi qrupa çağırıldı**")
        say = 0
        return
      if usrnum == 5:
        await bot.send_message(event.chat_id, usrtxt)
        await sleep(0.5)
        usrnum = 0
        usrtxt = ""
  elif event.pattern_match.group(1):
    msg = event.pattern_match.group(1)
    muveqqeti_isleyen.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in bot.iter_participants(event.chat_id):
      set_cagirma(1)
      say += 1
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}), "
      if event.chat_id not in muveqqeti_isleyen:
        say -= 1
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
      set_cagirma(1)
      say += 1
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}), "
      if event.chat_id not in muveqqeti_isleyen:
        say -= 1
        await event.respond(f"**🆘 Sürətli Dəvət Prosesi Sonlandırıldı\n{say} İstifadəçi qrupa çağırıldı**")
        say = 0
        return
      if usrnum == 5:
        await bot.send_message(event.chat_id, usrtxt)
        await sleep(0.5)
        usrnum = 0
        usrtxt = ""


@bot.on(NewMessage(pattern="^/speedtag ?(.*)"))
async def speedtag(event):
  global muveqqeti_isleyen
  if event.is_private:
    return
  say = 0
  admins = []
  async for admin in bot.iter_participants(event.chat_id, filter=cp):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**👨🏻‍🔧 Bu əmri sadəcə adminlər işlədə bilər**")
  if event.pattern_match.group(1) == tag:
    muveqqeti_isleyen.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in bot.iter_participants(event.chat_id):
      set_cagirma(1)
      say += 1
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}), "
      if event.chat_id not in muveqqeti_isleyen:
        say -= 1
        await event.respond(f"**🆘 Sürətli Dəvət Prosesi Sonlandırıldı\n{say} İstifadəçi qrupa çağırıldı")
        say = 0
        return
      if usrnum == 1:
        await bot.send_message(event.chat_id, usrtxt)
        await sleep(0.5)
        usrnum = 0
        usrtxt = ""
  elif event.pattern_match.group(1):
    msg = event.pattern_match.group(1)
    muveqqeti_isleyen.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in bot.iter_participants(event.chat_id):
      set_cagirma(1)
      say += 1
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}), "
      if event.chat_id not in muveqqeti_isleyen:
        say -= 1
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
      set_cagirma(1)
      say += 1
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}), "
      if event.chat_id not in muveqqeti_isleyen:
        say -= 1
        await event.respond(f"**🆘 Sürətli Dəvət Prosesi Sonlandırıldı\n{say} İstifadəçi qrupa çağırıldı")
        say = 0
        return
      if usrnum == 1:
        await bot.send_message(event.chat_id, usrtxt)
        await sleep(0.5)
        usrnum = 0
        usrtxt = ""


@bot.on(NewMessage())
async def data(event):
  if event.is_private:
    add_served_user(event.chat.id)
  else:
    add_served_chat(event.chat.id)


@bot.on(NewMessage(pattern="^/btstats$"))
async def stats(event):
    qrup = len(await get_served_chats())
    user = len(await get_served_users())
    cagirma = await get_queries()
    if event.sender_id in owners:
        await event.reply(f"💎 BORZ Tagger statistikası:\n👥 Qrup:{qrup}\n👤 İstifadəçi: {user}\n🆙 Ümumi Çağırılan istifadəçi: {cagirma}")

ad_buttons = [

    [Button.inline('PM', 'pm')],
    [Button.inline('Qruplara', 'group')],
    [Button.inline('Hər ikisinə', 'all')]
]

confirm_buttons = [
    [Button.inline('Hə', 'yes')],
    [Button.inline('Yox', 'no')]
]

@bot.on(NewMessage(pattern="^/btreklam"))
async def start(event: telethon.events.newmessage.NewMessage.Event):
    chats = len(await get_served_chats())
    users = len(await get_served_users())
    if event.sender_id not in owners:
        return


    await event.reply("Reklamı botu start etmiş userlərin PM-inə göndərmək istəyirsən, ya bot işlənən qruplara?",
                      buttons=ad_buttons)
    async with event.client.conversation(event.chat_id) as conv:
        try:
            response = await conv.wait_event(events.CallbackQuery(chats=[event.chat_id]), timeout=180)
            await response.delete()
        except:
            await event.reply("Yenidən başlamaq üçün /btreklam kliklə")
            return


    if response.data.decode() == 'pm':
        ids = users
    elif response.data.decode() == 'group':
        ids = chats
    else:
        ids = chats + users

    await event.reply("Reklam mesajını göndər")
    async with event.client.conversation(event.chat_id) as conv:
        try:
            response = await conv.wait_event(events.NewMessage(chats=[event.chat_id]), timeout=180)
        except:
            await event.reply("Yenidən başlamaq üçün {} kliklə".format(command))
            return
    message_to_send = response.message
    await bot.send_message(entity=event.chat_id,  message=message_to_send)

    await event.respond("Yuxarıdakı mesajın göndərilməsini təsdiq edirsən?",
                        buttons=confirm_buttons)
    async with event.client.conversation(event.chat_id) as conv:
        try:
            response = await conv.wait_event(events.CallbackQuery(chats=[event.chat_id]), timeout=180)
            await response.delete()
        except:
            await event.reply("Yenidən başlamaq üçün /btreklam kliklə")
            return

    if response.data.decode() == 'yes':
        count = 0
        for i in ids:
            try:
                await bot.send_message(entity=int(a["user_id"]), message=message_to_send)
                time.sleep(2)
                count += 1
            except Exception as e:
                pass
        await event.reply("Reklam bitdi\n\n{} id'dən {} id'yə reklam göndərildi".format(len(ids), count))
    else:
        await event.reply("Yenidən başlamaq üçün /btreklam kliklə")


bot.start()
bot.run_until_disconnected()
