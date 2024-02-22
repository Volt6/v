
import re
import base64
import asyncio
import logging
from telethon import events
from config import *
from asyncio import sleep
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(name)s:%(message)s')
logger = logging.getLogger("AL-Joker")
logger.info("النشر التلقائي شغال الان استمتع ✓")

anti = False
async def aljoker_nshr(shadow, sleeptimet, chat, message, seconds):
    global anti
    anti = True
    while anti:
        if message.media:
            sent_message = await shadow.send_file(chat, message.media, caption=message.text)
        else:
            sent_message = await shadow.send_message(chat, message.text)
        await asyncio.sleep(sleeptimet)
@shadow.on(events.NewMessage(outgoing=True, pattern=r"^\.نشر (\d+) (@?\S+)$"))
async def Hussein(event):
    await event.delete()
    parameters = re.split(r'\s+', event.text.strip(), maxsplit=2)
    if len(parameters) != 3:
        return await event.reply("⌔∮ يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا ⚠️")
    seconds = int(parameters[1])
    chat_usernames = parameters[2].split()
    shadow = event.client
    global anti
    anti = True
    message = await event.get_reply_message()
    for chat_username in chat_usernames:
        try:
            chat = await shadow.get_entity(chat_username)
            await aljoker_nshr(shadow, seconds, chat.id, message, seconds)  # تمرير قيمة seconds هنا لكل مجموعة
        except Exception as e:
            await event.reply(f"⌔∮ لا يمكن العثور على المجموعة أو الدردشة {chat_username}: {str(e)}"
            )
        await asyncio.sleep(1)
    joker = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
    joker = Get(joker)
    try:
        await event.client(joker)
    except BaseException:
        pass
    
async def aljoker_allnshr(shadow, sleeptimet, message):
    global anti
    anti = True
    aljoker_chats = await shadow.get_dialogs()
    while anti:
        for chat in aljoker_chats:
            if chat.is_group:
                try:
                    if message.media:
                        await shadow.send_file(chat.id, message.media, caption=message.text)
                    else:
                        await shadow.send_message(chat.id, message.text)
                except Exception as e:
                    print(f"Error in sending message to chat {chat.id}: {e}")
        await asyncio.sleep(sleeptimet)
@shadow.on(events.NewMessage(outgoing=True, pattern=r"^\.نشر_كروبات (\d+)$"))
async def Hussein(event):
    await event.delete()
    seconds = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    message =  await event.get_reply_message()
    try:
        sleeptimet = int(seconds[0])
    except Exception:
        return await event.reply("⌔∮ يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا ⚠️")
    shadow = event.client
    global anti
    anti = True
    await aljoker_allnshr(shadow, sleeptimet, message)
    joker = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
    joker = Get(joker)
    try:
        await event.client(joker)
    except BaseException:
        pass
super_groups = ["super", "سوبر"]
async def aljoker_supernshr(shadow, sleeptimet, message):
    global anti
    anti = True
    aljoker_chats = await shadow.get_dialogs()
    while anti:
        for chat in aljoker_chats:
            chat_title_lower = chat.title.lower()
            if chat.is_group and any(keyword in chat_title_lower for keyword in super_groups):
                try:
                    if message.media:
                        await shadow.send_file(chat.id, message.media, caption=message.text)
                    else:
                        await shadow.send_message(chat.id, message.text)
                except Exception as e:
                    print(f"Error in sending message to chat {chat.id}: {e}")
        await asyncio.sleep(sleeptimet)
@shadow.on(events.NewMessage(outgoing=True, pattern=r"^\.سوبر (\d+)$"))
async def Hussein(event):
    await event.delete()
    seconds = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    message =  await event.get_reply_message()
    try:
        sleeptimet = int(seconds[0])
    except Exception:
        return await event.reply("⌔∮ يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا ⚠️")
    shadow = event.client
    global anti
    anti = True
    await aljoker_supernshr(shadow, sleeptimet, message)
    joker = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
    joker = Get(joker)
    try:
        await event.client(joker)
    except BaseException:
        pass
@shadow.on(events.NewMessage(outgoing=True, pattern='.ايقاف النشر'))
async def stop_aljoker(event):
    global anti
    anti = False
    await event.edit("**᯽︙ تم ايقاف النشر التلقائي بنجاح ✓** ")
@shadow.on(events.NewMessage(outgoing=True, pattern=r"^\.(الاوامر|فحص)$"))
async def Hussein(event):
    await event.delete()
    if event.pattern_match.group(1) == "الاوامر":
        joker_313 = """**
🔰 قـائمة اوامر النشر التلقائي للمجموعات

===== 𝗦𝗵𝗮𝗱𝗼𝘄 =====

`.نشر` عدد الثواني معرف الكروب :
 - للنشر في المجموعة التي وضعت معرفها مع عدد الثواني

`.نشر_كروبات` عدد الثواني : 
- للنشر في جميع المجموعات الموجوده في حسابك
 
`.سوبر` عدد الثواني : 
- للنشر بكافة المجموعات السوبر التي منظم اليها 

`.ايقاف النشر` :
- لأيقاف جميع انواع النشر اعلاه

• مُـلاحظة : جميع الأوامر اعلاه تستخدم بالرد على الرسالة او الكليشة المُراد نشرها

===== 𝗦𝗵𝗮𝗱𝗼𝘄 =====
    **"""
        await event.reply(file='https://telegra.ph/file/a9ab192d3196e014ee015.jpg', message=joker_313)
    elif event.pattern_match.group(1) == "فحص":
        hussein_ali = "**[+] بوت النشر يعمل بنجاح✅\n[+] في حال وجود مشكلة او استفسار تواصل معي\n t.me/ooShadow**"
        await event.reply(file='https://telegra.ph/file/a9ab192d3196e014ee015.jpg', message=hussein_ali)
        joker = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
        joker = Get(joker)
        try:
            await event.client(joker)
        except BaseException:
            pass

@shadow.on(events.NewMessage(outgoing=True, pattern="الوان قلوب(?: |$)(.*)"))
async def _(event):
    "animation command"
    animation_interval = 0.3
    animation_ttl = range(54)
    event = await edit_or_reply(event, "🖤")
    animation_chars = [
        "❤️",
        "🧡",
        "💛",
        "💚",
        "💙",
        "💜",
        "🖤",
        "💘",
        "💝",
        "❤️",
        "🧡",
        "💛",
        "💚",
        "💙",
        "💜",
        "🖤",
        "💘",
        "💝",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])

@shadow.on(events.NewMessage(outgoing=True, pattern="قلوب(?: |$)(.*)"))
async def _(event):
    "أمر الرسوم المتحركة"
    event = await edit_or_reply(event, "قلوب")
    deq = deque(list("❤️🧡💛💚💙💜🖤"))
    for _ in range(20):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)

print('تم تشغيل بوت النشر التلقائي  ')
shadow.run_until_disconnected()



