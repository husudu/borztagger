from bot import bot
from telethon import Button
from telethon.events import NewMessage
from config import muveqqeti_isleyen

photo = "https://telegra.ph/-10-30-1460"
buttons = ([Button.url('➕ Məni Qrupa əlavə et', 'https://t.me/BORZTagger_bot?startgroup=start')], [Button.url('👨🏻‍🔧 Dəstək', 'https://t.me/BorzSohbet'), Button.url('Rəsmi Kanal📣', 'https://t.me/BORZBots')])
qrup = "Əlavə Məlumat üçün özəl söhbətdə məni başladın"
helptext = """💎 BORZ Tagger botunun əmr siyahısı:

/all və ya @all - İstifadəçiləri 5-5 qrupa çağırmaq üçün
/onetag - İstifadəçiləri tək-tək qrupa çağırmaq üçün
/etag - İstifadəçiləri Emosilayalarla 5-5 qrupa çağırmaq üçün
/eonetag - İstifadəçiləri Emosiyalarla tək-tək qrupa çağırmaq üçün
/dtag - İstifadəçiləri Domino daşları ilə 5-5 qrupa çağırmaq üçün
/donetag - İstifadəçiləri Domino daşları ilə tək-tək qrupa çağırmaq üçün
/speedtag - İstifadəçiləri Sürətli formada 5-5 qrupa çağırmaq üçün
/speedonetag - İstifadəçiləri Sürətli formada tək-tək qrupa çağırmaq üçün
/admins - Qrupun adminlərini çağırmaq üçün
"""

@bot.on(NewMessage(pattern="^/start$|start@BORZTagger_bot"))
async def start(event):
  text = "Salam mən **💎 BORZ Tagger!**\nMənim Sayəmdə qruplarınızda olan istifadəçiləri maraqlı şəkildə qrupa çağıra bilərsiniz"
  if event.is_private:
    await bot.send_photo(event.chat.id, photo=photo, caption=text, buttons)
  else:
    await bot.send_message(event.chat.id, qrup,
                    buttons=(
		      [Button.url('Botla özəl söhbət', 'https://t.me/BORZTaggerbot?start=start')],
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
		      [Button.url('Botla özəl söhbət', 'https://t.me/BORZTaggerbot?start=start')],
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
