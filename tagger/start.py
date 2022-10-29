from bot import bot
from telethon import Button
from telethon.events import NewMessage
from config import muveqqeti_isleyen

buttons = ([Button.url('➕ Məni Qrupa əlavə et', 'https://t.me/BORZTagger_bot?startgroup=a')], [Button.url('👨🏻‍🔧 Dəstək', 'https://t.me/BorzSohbet'), Button.url('Rəsmi Kanal📣', 'https://t.me/BORZBots')])
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
    await bot.send_photo(event.chat.id, photo=photo, text=text, buttons)

@bot.on(NewMessage(pattern="^/help$|help@BORZTagger_bot"))
async def help(event):
    await bot.send_message(event.chat.id, helptext)

@bot.on(NewMessage(pattern='^/stop$|stop@BORZTagger_bot'))
async def stop(event):
  global muveqqeti_isleyen
  muveqqeti_isleyen.remove(event.chat_id)
