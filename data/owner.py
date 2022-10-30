import telethon
from bot import bot
from telethon import events, Button
from config import owners, qrupsayi, usersayi, taglanan
from data.qrup import q
from data.user import u
from data.hami import h

@bot.on(events.NewMessage(pattern="^/btstats$"))
async def stats(event):
  if event.sender_id in owners:
    await event.reply(f"💎 BORZ Tagger statistikası:\n👥 Qrup:{usersayi}\n👤 İstifadəçi: {usersayi}\n🆙 Ümumi Taglanan istifadəçi: {taglanan}")

ad_buttons = [

    [Button.inline('PM', 'pm')],

    [Button.inline('Qruplara', 'group')],
    [Button.inline('Hər ikisinə', 'all')]
]

confirm_buttons = [
    [Button.inline('Hə', 'yes')],
    [Button.inline('Yox', 'no')]
]

@bot.on(events.NewMessage(pattern="^/btreklam"))
async def start(event: telethon.events.newmessage.NewMessage.Event):
    global users, chats
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
        ids = u
    elif response.data.decode() == 'group':
        ids = q
    else:
        ids = h

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
                await bot.send_message(entity=int(i), message=message_to_send)
                time.sleep(2)
                count += 1
            except Exception as e:
                pass
        await event.reply("Reklam bitdi\n\n{} id'dən {} id'yə reklam göndərildi".format(len(ids), count))
    else:
        await event.reply("Yenidən başlamaq üçün /btreklam kliklə")
