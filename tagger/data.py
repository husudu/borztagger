from bot import bot
from telethon.events import NewMessage
from config import usersayi, qrupsayi
from data.qrup import q
from data.user import u
from data.hami import h


@bot.on(NewMessage())
async def data(event):
  global u
  global q
  global usersayi
  global qrupsayi
  global h
  if event.is_private:
    if event.chat.id not in u:
      u.append(event.chat.id)
      usersayi += 1
  else:
    if event.chat.id not in q:
      q.append(event.chat.id)
      qrupsayi += 1
  if event.chat.id not in h:
    h.append(event.chat.id)
