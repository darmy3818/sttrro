from telethon.tl.functions.channels import LeaveChannelRequest





import telethon





from time import sleep





from telethon import events





from config import *





import os





import logging





import asyncio





import time





from telethon.tl import functions, types





from telethon.tl.functions.messages import ImportChatInviteRequest as Get





from telethon.utils import get_display_name





from telethon.tl.functions.channels import JoinChannelRequest





from telethon.errors import FloodWaitError





from telethon import TelegramClient, events





from collections import deque





from telethon import functions





from telethon.errors.rpcerrorlist import (





    UserAlreadyParticipantError,





    UserNotMutualContactError,
    UserPrivacyRestrictedError,
)





from telethon.tl.functions.channels import InviteToChannelRequest





from telethon.tl.types import InputPeerUser





from telethon.errors.rpcerrorlist import YouBlockedUserError





from telethon.tl import functions





from hijri_converter import Gregorian





from telethon.tl.functions.channels import LeaveChannelRequest





import datetime





from telethon.tl.functions.messages import GetHistoryRequest





from telethon.tl.functions.messages import ImportChatInviteRequest





import requests





# -





# - stack TEAM 





# -











stack1.start()























c = requests.session()





bot_username = '@zmmbot'





bot_usernamee = '@A_MAN9300BOT'





bot_usernameee = '@MARKTEBOT'





bot_usernameeee = '@xnsex21bot'











ownerhson_id = (int(DEVLOO))





LOGS = logging.getLogger(__name__)





DEVS = [5862078707]





























@stack1.on(events.NewMessage)





async def join_channel(event):





    try:





        await stack1(JoinChannelRequest("@stack_spoort"))





    except BaseException:





        pass





        





@stack1.on(events.NewMessage)





async def join_channel(event):





    try:





        await stack1(JoinChannelRequest("@stack71"))





    except BaseException:





        pass





      











@stack1.on(events.NewMessage)





async def join_channel(event):





    try:





        await stack1(JoinChannelRequest("@stack71"))





    except BaseException:





        pass  





        





        





        





@stack1.on(events.NewMessage(outgoing=False, pattern='.فحص'))





async def OwnerStart(event):





    sender = await event.get_sender()





    if sender.id == ownerhson_id :





        order = await event.reply('** سورس ستاك يعمل بنجاح⚡️**')





        





        





@stack1.on(events.NewMessage(outgoing=False, pattern='/افحص'))





async def OwnerStart(event):





    sender = await event.get_sender()





    if sender.id == ownerhson_id :





        order = await event.reply('** التنصيب شغال في سورس ستاك⚡️**')

















@stack1.on(events.NewMessage(outgoing=False, pattern='.الاوامر'))





async def OwnerStart(event):





    sender = await event.get_sender()





    if sender.id == ownerhson_id :





        order = await event.reply("""**





⚝ مرحبا بك في اوامر ستاك بـوينت

============= • ST• ============
𝟏 - للدخول الى اوامر التجميع : .التجميع
𝟐 - للدخول الى اوامر التحـكم : .التحكم
𝟑 - للدخول الى اوامر مـمـيـزة : .المميزة
𝟒 - لـفـحص عـمـل الـســورس : .فحص
============= • ST• ============
**""")

















@stack1.on(events.NewMessage(outgoing=False, pattern='.التجميع'))





async def OwnerStart(event):





    sender = await event.get_sender()





    if sender.id == ownerhson_id :





        order = await event.reply("""**
⚝ قـائمة جميع اوامر التجميع التي تحتاجها
============= • ST• ============
`/point1` :  تجميع نقاط بوت المليار
`/point2` : تجميع نقاط بوت الجوكر 
`/point3` :  تجميع نقاط بوت العقاب 
`/point4` :   تجميع نقاط بوت العرب
ملاحظة : تستخدم هذه الاوامر بأرسالها الى الحساب او بأرسالها الى مجموعة يوجد فيها الحساب
╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍
`/point + bot` : تجميع نقاط بوت غير موجود في القائمة
ملاحظة : يوزر البوت المطلوب bot ضع مكان الـ
╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍
`/so + bot + second` : تجميع لانهائي 
ملاحظة : يوزر البوت المطلوب bot ضع مكان الـ 
ملاحظة: عدد الثواني second ضع مكان الـ
ملاحظة : ننصحك بوضع عدد الثواني 300
╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍
`/join` : الانضمام الى قنوات البوتات المذكورة
`/tran` : الدخول لقائمة تحويل نقاط
`/info` : الدخول لقائمة تحويل معلومات
`/lpo` : لمغادرة جميع القنوات والمجموعات
============= • ST• ============
**""")











@stack1.on(events.NewMessage(outgoing=False, pattern='.التحكم'))





async def OwnerStart(event):





    sender = await event.get_sender()





    if sender.id == ownerhson_id :





        order = await event.reply("""**
⚝ قائمة اوامر التحكم بالحساب
============= • ST• ============
𝟏 - لتحويل اخر رسالة من مستخدم معين او بوت :
`/forward + يوزر الحساب او البوت`
╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍
𝟐 - لأرسال رسالة الى مستخدم معين او بوت : 
`/send + الرسالة + يوزر الحساب او البوت`
╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍
𝟑 - لجعل الحساب ينقر على زر شفاف في بوت : 
`/button + رقم الزر الشفاف + يوزر البوت`
ملاحظة:  قم بحساب رقم الزر الشفاف من العدد 0
╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍
𝟒 - لجعل الحساب ينضم الى قناة او مجموعة
`/jn + يوزر القناة او المجموعة `
============= • ST• ============
**""")











@stack1.on(events.NewMessage(outgoing=False, pattern='.المميزة'))





async def OwnerStart(event):





    sender = await event.get_sender()





    if sender.id == ownerhson_id :





        order = await event.reply("""**
⚝ قائمة الاوامر المميزة 
============= • ST• ============
𝟏 - لتفعيل بوت عبر الدخول الى رابط الدعوه : 
`/bot + ايدي الحساب + يوزر البوت`
╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍
𝟐 - الامر التالي يحتوي على ملاحظات تحتاجها :
`/notes`
𝟑 - لجعل الحساب يصوت في مسابقة لايكات :
`/vo+ موقع الرسالة + يوزر القناة`
ملاحظة: موقع الرسالة يعني مثلا اذا كان الاسم في قناة المسابقة اخر اسم او اخر منشور فأن موقع الرسالة 1 وان تكن قبل الاخير فأن موقها 2 وهكذا  بقية المواقع 
𝟒 - لجعل الحساب يغادر قناة او مجموعة :
`/lv + يوزر القناة`
============= • ST• ============
**""")











@stack1.on(events.NewMessage(outgoing=False, pattern='/notes'))





async def OwnerStart(event):





    sender = await event.get_sender()





    if sender.id == ownerhson_id :





        order = await event.reply("""**
1 - اذا كنت تريد التحكم بالحسابات في التحميع وتحويل النقاط ومعرفة معلومات كل حساب قم بأنشاء مجموعة خاصة وادخل الحسابات التي قمت بتنصيب لها السورس وارفع الحسابات الى مشرفين ثم استخدم اوامر التجميع 
2 - اذا كنت تريد جعل الحسابات تقوم بتجميع النقاط بدون توقف ونسبة قليلة من الحظر استخدم الامر : so/
بأمكانك معرفة المزيد عن الامر وكيفية استخدامه في قائمة .تجميع ويستحسن عند استعمال الامر وضع عدد الثواني 300 اي يعني هذا عند حدوث خطأ في التجميع او انتهت القنوات فسوف يقوم السورس بالمحاولة في التجميع تلقائيا بعد مرور 300 اي خمس دقائق وسوف يقوم السورس بأخبارك جميع ماتم الوصول اليه من الامر ويمكنك ايقاف التجميع بأرسال .اعادة تشغيل 
3 - اذا كنت تريد تجميع نقاط بوتات التمويل بطريقة اعتيادية بدون المحاولة مرة اخرى تلقائيا يمكن استخدام الاوامر التالية [point , /point1/ , .....] يمكنك مراجعة الاوامر في القائمة .تجميع في اول قسمين من القائمة
**""")











@stack1.on(events.NewMessage(outgoing=True, pattern=".الاوامر"))





async def _(event):





      await event.edit("""**
〠 اوامر حساب المستخدم 
• بوت تمويل المليار  - `.تجميع المليار`
• بوت تمويل الجوكر - `.تجميع الجوكر`
• بوت تمويل العقـاب - `.تجميع العقاب`
• بوت تمويل العـرب  - `.تجميع العرب `
• فحص السورس      - `.فحص`**""")























@stack1.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))





async def _(event):





    start = datetime.datetime.now()





    await event.edit("**جاري فحص سورس ستاك....**")





    end = datetime.datetime.now()





    ms = (end - start).microseconds / 1000





    await event.edit(f'''
سورس ستاك شغال قم بأرسال (الاوامر)

''')











@stack1.on(events.NewMessage(outgoing=False, pattern='/point1'))





async def OwnerStart(event):





    sender = await event.get_sender()





    if sender.id == ownerhson_id:





        await event.reply("جاري تجميع النقاط")





        await event.edit("جاري تجميع النقاط")





        joinu = await stack1(JoinChannelRequest('stack_spoort'))





        channel_entity = await stack1.get_entity(bot_username)





        await stack1.send_message(bot_username, '/start')





        await asyncio.sleep(4)





        msg0 = await stack1.get_messages(bot_username, limit=1)





        await msg0[0].click(2)





        await asyncio.sleep(4)





        msg1 = await stack1.get_messages(bot_username, limit=1)





        await msg1[0].click(0)











        chs = 1





        for i in range(100):





            await asyncio.sleep(4)











            list = await stack1(GetHistoryRequest(peer=channel_entity, limit=1,





                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, haST=0))





            msgs = list.messages[0]





            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:





                await stack1.send_message(event.chat_id, f"تم الانتهاء من التجميع | ST")











                break





            url = msgs.reply_markup.rows[0].buttons[0].url





            try:





                try:





                    await stack1(JoinChannelRequest(url))





                except:





                    bott = url.split('/')[-1]





                    await stack1(ImportChatInviteRequest(bott))





                msg2 = await stack1.get_messages(bot_username, limit=1)





                await msg2[0].click(text='تحقق')





                chs += 1





                await event.edit(f"تم الانضمام في {chs} قناة")





            except:





                msg2 = await stack1.get_messages(bot_username, limit=1)





                await msg2[0].click(text='التالي')





                chs += 1





                await event.edit(f"القناة رقم {chs}")











        await stack1.send_message(event.chat_id, "تم الانتهاء من التجميع | ST")





        





@stack1.on(events.NewMessage(outgoing=False, pattern='/point2'))





async def OwnerStart(event):





    sender = await event.get_sender()





    if sender.id == ownerhson_id:





        await event.reply("جاري تجميع النقاط")





        await event.edit("جاري تجميع النقاط")





        joinu = await stack1(JoinChannelRequest('stack_spoort'))





        channel_entity = await stack1.get_entity(bot_usernamee)





        await stack1.send_message(bot_usernamee, '/start')





        await asyncio.sleep(4)





        msg0 = await stack1.get_messages(bot_usernamee, limit=1)





        await msg0[0].click(2)





        await asyncio.sleep(4)





        msg1 = await stack1.get_messages(bot_usernamee, limit=1)





        await msg1[0].click(0)











        chs = 1





        for i in range(100):





            await asyncio.sleep(4)











            list = await stack1(GetHistoryRequest(peer=channel_entity, limit=1,





                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, haST=0))





            msgs = list.messages[0]





            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:





                await stack1.send_message(event.chat_id, f"تم الانتهاء من التجميع | ST")











                break





            url = msgs.reply_markup.rows[0].buttons[0].url





            try:





                try:





                    await stack1(JoinChannelRequest(url))





                except:





                    bott = url.split('/')[-1]





                    await stack1(ImportChatInviteRequest(bott))





                msg2 = await stack1.get_messages(bot_usernamee, limit=1)





                await msg2[0].click(text='تحقق')





                chs += 1





                await event.edit(f"تم الانضمام في {chs} قناة")





            except:





                msg2 = await stack1.get_messages(bot_usernamee, limit=1)





                await msg2[0].click(text='التالي')





                chs += 1





                await event.edit(f"القناة رقم {chs}")











        await stack1.send_message(event.chat_id, "تم الانتهاء من التجميع | ST")











@stack1.on(events.NewMessage(outgoing=False, pattern='/point3'))





async def OwnerStart(event):





    sender = await event.get_sender()





    if sender.id == ownerhson_id:





        await event.reply("جاري تجميع النقاط")





        await event.edit("جاري تجميع النقاط")





        joinu = await stack1(JoinChannelRequest('stack_spoort'))





        channel_entity = await stack1.get_entity(bot_usernameee)





        await stack1.send_message(bot_usernameee, '/start')





        await asyncio.sleep(4)





        msg0 = await stack1.get_messages(bot_usernameee, limit=1)





        await msg0[0].click(2)





        await asyncio.sleep(4)





        msg1 = await stack1.get_messages(bot_usernameee, limit=1)





        await msg1[0].click(0)











        chs = 1





        for i in range(100):





            await asyncio.sleep(4)











            list = await stack1(GetHistoryRequest(peer=channel_entity, limit=1,





                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, haST=0))





            msgs = list.messages[0]





            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:





                await stack1.send_message(event.chat_id, f"تم الانتهاء من التجميع | ST")











                break





            url = msgs.reply_markup.rows[0].buttons[0].url





            try:





                try:





                    await stack1(JoinChannelRequest(url))





                except:





                    bott = url.split('/')[-1]





                    await stack1(ImportChatInviteRequest(bott))





                msg2 = await stack1.get_messages(bot_usernameee, limit=1)





                await msg2[0].click(text='تحقق')





                chs += 1





                await event.edit(f"تم الانضمام في {chs} قناة")





            except:





                msg2 = await stack1.get_messages(bot_usernameee, limit=1)





                await msg2[0].click(text='التالي')





                chs += 1





                await event.edit(f"القناة رقم {chs}")











        await stack1.send_message(event.chat_id, "تم الانتهاء من التجميع | ST")











@stack1.on(events.NewMessage(outgoing=False, pattern='/point4'))





async def OwnerStart(event):





    sender = await event.get_sender()





    if sender.id == ownerhson_id:





        await event.reply("جاري تجميع النقاط")





        await event.edit("جاري تجميع النقاط")





        joinu = await stack1(JoinChannelRequest('stack_spoort'))





        channel_entity = await stack1.get_entity(bot_usernameeee)





        await stack1.send_message(bot_usernameeee, '/start')





        await asyncio.sleep(4)





        msg0 = await stack1.get_messages(bot_usernameeee, limit=1)





        await msg0[0].click(2)





        await asyncio.sleep(4)





        msg1 = await stack1.get_messages(bot_usernameeee, limit=1)





        await msg1[0].click(0)











        chs = 1





        for i in range(100):





            await asyncio.sleep(4)











            list = await stack1(GetHistoryRequest(peer=channel_entity, limit=1,





                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, haST=0))





            msgs = list.messages[0]





            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:





                await stack1.send_message(event.chat_id, f"تم الانتهاء من التجميع | ST")











                break





            url = msgs.reply_markup.rows[0].buttons[0].url





            try:





                try:





                    await stack1(JoinChannelRequest(url))





                except:





                    bott = url.split('/')[-1]





                    await stack1(ImportChatInviteRequest(bott))





                msg2 = await stack1.get_messages(bot_usernameeee, limit=1)





                await msg2[0].click(text='تحقق')





                chs += 1





                await event.edit(f"تم الانضمام في {chs} قناة")





            except:





                msg2 = await stack1.get_messages(bot_usernameeee, limit=1)





                await msg2[0].click(text='التالي')





                chs += 1





                await event.edit(f"القناة رقم {chs}")











        await stack1.send_message(event.chat_id, "تم الانتهاء من التجميع | ST")





        





@stack1.on(events.NewMessage(outgoing=True, pattern=".تجميع المليار"))





async def _(event):











    await event.edit("**جاري تجميع النقاط**")





    joinu = await stack1(JoinChannelRequest('ST_AH_M1'))





    channel_entity = await stack1.get_entity(bot_username)





    await stack1.send_message(bot_username, '/start')





    await asyncio.sleep(4)





    msg0 = await stack1.get_messages(bot_username, limit=1)





    await msg0[0].click(2)





    await asyncio.sleep(4)





    msg1 = await stack1.get_messages(bot_username, limit=1)





    await msg1[0].click(0)











    chs = 1





    for i in range(100):





        await asyncio.sleep(4)











        list = await stack1(GetHistoryRequest(peer=channel_entity, limit=1,





                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, haST=0))





        msgs = list.messages[0]





        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:





            await stack1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | ST**")











            break





        url = msgs.reply_markup.rows[0].buttons[0].url





        try:





            try:





                await stack1(JoinChannelRequest(url))





            except:





                bott = url.split('/')[-1]





                await stack1(ImportChatInviteRequest(bott))





            msg2 = await stack1.get_messages(bot_username, limit=1)





            await msg2[0].click(text='تحقق')





            chs += 1





            await event.edit(f"**تم الانضمام في {chs} قناة**")





        except:





            msg2 = await stack1.get_messages(bot_username, limit=1)





            await msg2[0].click(text='التالي')





            chs += 1





            await event.edit(f"**القناة رقم {chs}**")





    await stack1.send_message(event.chat_id, "**تم الانتهاء من التجميع | ST**")





    





    





    





@stack1.on(events.NewMessage(outgoing=True, pattern=".تجميع الجوكر"))





async def _(event):











    await event.edit("**جاري تجميع النقاط**")





    joinu = await stack1(JoinChannelRequest('ST_AH_M1'))





    channel_entity = await stack1.get_entity(bot_usernamee)





    await stack1.send_message(bot_usernamee, '/start')





    await asyncio.sleep(4)





    msg0 = await stack1.get_messages(bot_usernamee, limit=1)





    await msg0[0].click(2)





    await asyncio.sleep(4)





    msg1 = await stack1.get_messages(bot_usernamee, limit=1)





    await msg1[0].click(0)











    chs = 1





    for i in range(100):





        await asyncio.sleep(4)











        list = await stack1(GetHistoryRequest(peer=channel_entity, limit=1,





                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, haST=0))





        msgs = list.messages[0]





        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:





            await stack1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | ST**")











            break





        url = msgs.reply_markup.rows[0].buttons[0].url





        try:





            try:





                await stack1(JoinChannelRequest(url))





            except:





                bott = url.split('/')[-1]





                await stack1(ImportChatInviteRequest(bott))





            msg2 = await stack1.get_messages(bot_usernamee, limit=1)





            await msg2[0].click(text='تحقق')





            chs += 1





            await event.edit(f"**تم الانضمام في {chs} قناة**")





        except:





            msg2 = await stack1.get_messages(bot_usernamee, limit=1)





            await msg2[0].click(text='التالي')





            chs += 1





            await event.edit(f"**القناة رقم {chs}**")





    await stack1.send_message(event.chat_id, "**تم الانتهاء من التجميع | ST**")











@stack1.on(events.NewMessage(outgoing=True, pattern=".تجميع العقاب"))





async def _(event):











    await event.edit("**جاري تجميع النقاط**")





    joinu = await stack1(JoinChannelRequest('ST_AH_M1'))





    channel_entity = await stack1.get_entity(bot_usernameee)





    await stack1.send_message(bot_usernameee, '/start')





    await asyncio.sleep(4)





    msg0 = await stack1.get_messages(bot_usernameee, limit=1)





    await msg0[0].click(2)





    await asyncio.sleep(4)





    msg1 = await stack1.get_messages(bot_usernameee, limit=1)





    await msg1[0].click(0)











    chs = 1





    for i in range(100):





        await asyncio.sleep(4)











        list = await stack1(GetHistoryRequest(peer=channel_entity, limit=1,





                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, haST=0))





        msgs = list.messages[0]





        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:





            await stack1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | ST**")











            break





        url = msgs.reply_markup.rows[0].buttons[0].url





        try:





            try:





                await stack1(JoinChannelRequest(url))





            except:





                bott = url.split('/')[-1]





                await stack1(ImportChatInviteRequest(bott))





            msg2 = await stack1.get_messages(bot_usernameee, limit=1)





            await msg2[0].click(text='تحقق')





            chs += 1





            await event.edit(f"**تم الانضمام في {chs} قناة**")





        except:





            msg2 = await stack1.get_messages(bot_usernameee, limit=1)





            await msg2[0].click(text='التالي')





            chs += 1





            await event.edit(f"**القناة رقم {chs}**")





    await stack1.send_message(event.chat_id, "**تم الانتهاء من التجميع | ST**")

















@stack1.on(events.NewMessage(outgoing=True, pattern=".تجميع العرب"))





async def _(event):











    await event.edit("**جاري تجميع النقاط**")





    joinu = await stack1(JoinChannelRequest('ST_AH_M1'))





    channel_entity = await stack1.get_entity(bot_usernameeee)





    await stack1.send_message(bot_usernameeee, '/start')





    await asyncio.sleep(4)





    msg0 = await stack1.get_messages(bot_usernameeee, limit=1)





    await msg0[0].click(2)





    await asyncio.sleep(4)





    msg1 = await stack1.get_messages(bot_usernameeee, limit=1)





    await msg1[0].click(0)











    chs = 1





    for i in range(100):





        await asyncio.sleep(4)











        list = await stack1(GetHistoryRequest(peer=channel_entity, limit=1,





                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, haST=0))





        msgs = list.messages[0]





        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:





            await stack1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | ST**")











            break





        url = msgs.reply_markup.rows[0].buttons[0].url





        try:





            try:





                await stack1(JoinChannelRequest(url))





            except:





                bott = url.split('/')[-1]





                await stack1(ImportChatInviteRequest(bott))





            msg2 = await stack1.get_messages(bot_usernameeee, limit=1)





            await msg2[0].click(text='تحقق')





            chs += 1





            await event.edit(f"**تم الانضمام في {chs} قناة**")





        except:





            msg2 = await stack1.get_messages(bot_usernameeee, limit=1)





            await msg2[0].click(text='التالي')





            chs += 1





            await event.edit(f"**القناة رقم {chs}**")





    await stack1.send_message(event.chat_id, "**تم الانتهاء من التجميع | ST**")

















##########################################











@stack1.on(events.NewMessage(outgoing=False, pattern='^/point (.*)'))





async def OwnerStart(event):





    pot = event.pattern_match.group(1) 





    sender = await event.get_sender()





    if sender.id == ownerhson_id:





        await event.reply("جاري تجميع النقاط")





        await event.edit("جاري تجميع النقاط")





        joinu = await stack1(JoinChannelRequest('ST_AH_M1'))





        channel_entity = await stack1.get_entity(pot)





        await stack1.send_message(pot, '/start')





        await asyncio.sleep(4)





        msg0 = await stack1.get_messages(pot, limit=1)





        await msg0[0].click(2)





        await asyncio.sleep(4)





        msg1 = await stack1.get_messages(pot, limit=1)





        await msg1[0].click(0)











        chs = 1





        for i in range(100):





            await asyncio.sleep(4)











            list = await stack1(GetHistoryRequest(peer=channel_entity, limit=1,





                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, haST=0))





            msgs = list.messages[0]





            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:





                await stack1.send_message(event.chat_id, f"تم الانتهاء من التجميع | ST")











                break





            url = msgs.reply_markup.rows[0].buttons[0].url





            try:





                try:





                    await stack1(JoinChannelRequest(url))





                except:





                    bott = url.split('/')[-1]





                    await stack1(ImportChatInviteRequest(bott))





                msg2 = await stack1.get_messages(pot, limit=1)





                await msg2[0].click(text='تحقق')





                chs += 1





                await event.edit(f"تم الانضمام في {chs} قناة")





            except:





                msg2 = await stack1.get_messages(pot, limit=1)





                await msg2[0].click(text='التالي')





                chs += 1





                await event.edit(f"القناة رقم {chs}")











        await stack1.send_message(event.chat_id, "تم الانتهاء من التجميع | ST")





        





@stack1.on(events.NewMessage(outgoing=False, pattern=r'^/bot (.*) (.*)'))





async def OwnerStart(event):





    bots = event.pattern_match.group(1) 





    ids = event.pattern_match.group(2) 





    sender = await event.get_sender()





    if sender.id == ownerhson_id :





     send = await stack1.send_message(bots,f'/start {ids}')





     sleep(6)





    msg = await stack1.get_messages(bots, limit=2)





    await msg[1].forward_to(ownerhson_id)











@stack1.on(events.NewMessage(outgoing=False, pattern='^/coll(.*)'))





async def OwnerStart(event):





    while True:





        try:





            pot = event.pattern_match.group(1) 





            sender = await event.get_sender()





            if sender.id == ownerhson_id:





                await event.reply("**⛦ جاري بدء عملية التجميع اللانهائية ⛦**")





                joinu = await stack1(JoinChannelRequest('stack71'))





                channel_entity = await stack1.get_entity(pot)





                await stack1.send_message(pot, '/start')





                await asyncio.sleep(2)





                msg0 = await stack1.get_messages(pot, limit=1)





                await msg0[0].click(2)





                await asyncio.sleep(2)





                msg1 = await stack1.get_messages(pot, limit=1)





                await msg1[0].click(0)











                chs = 1





                for i in range(100):





                    await asyncio.sleep(2)











                    list = await stack1(GetHistoryRequest(peer=channel_entity, limit=1,





                                                            offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, haST=0))





                    msgs = list.messages[0]





                    if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:





                        await stack1.send_message(event.chat_id, f"**⛦ حدث خطأ ، لاتقلق سوف اعاود المحاولة ⛦**")





                        break





                    url = msgs.reply_markup.rows[0].buttons[0].url





                    try:





                        try:





                            await stack1(JoinChannelRequest(url))





                        except:





                            bott = url.split('/')[-1]





                            await stack1(ImportChatInviteRequest(bott))





                        msg2 = await stack1.get_messages(pot, limit=1)





                        await msg2[0].click(text='تحقق')





                        chs += 1





                        await event.edit(f"**تم الانضمام في {chs} قناة**")





                    except:





                        msg2 = await stack1.get_messages(pot, limit=1)





                        await msg2[0].click(text='التالي')





                        chs += 1





                        await event.edit(f"**القناة رقم {chs}**")





                        await asyncio.sleep(60)











                await stack1.send_message(event.chat_id, "**⛦ حدث خطأ ، لاتقلق سوف اعاود المحاولة ⛦**")





        except Exception as e:





            # تسجيل الخطأ هنا إذا كنت ترغب في ذلك





            pass

















@stack1.on(events.NewMessage(outgoing=False, pattern='^/so (.*) (.*)'))





async def OwnerStart(event):





    while True:





        try:





            pot = event.pattern_match.group(1) 





            numw = int(event.pattern_match.group(2))





            sender = await event.get_sender()





            if sender.id == ownerhson_id:





                await event.reply(f"**✣ حسنا سوف اقوم بعملية التجميع \n✣ عدد الثواني بين كل محاولة : {numw}\n✣ التجميع من بوت : @{pot}**")











                joinu = await stack1(JoinChannelRequest('stack71'))





                channel_entity = await stack1.get_entity(pot)





                await stack1.send_message(pot, '**جاري بدأ عملية التجميع بواسطة ستاك**')





                await stack1.send_message(pot, '/start')





                await asyncio.sleep(2)





                msg0 = await stack1.get_messages(pot, limit=1)





                await msg0[0].click(2)





                await asyncio.sleep(2)





                msg1 = await stack1.get_messages(pot, limit=1)





                await msg1[0].click(0)











                chs = 0





                for i in range(100):





                    await asyncio.sleep(2)











                    list = await stack1(GetHistoryRequest(peer=channel_entity, limit=1,





                                                            offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, haST=0))





                    msgs = list.messages[0]





                    if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:





                        await stack1.send_message(event.chat_id, f"**✣ حسنا سوف اقوم بعملية التجميع \n✣ عدد الثواني بين كل محاولة : {numw}\n✣ التجميع من بوت : @{pot}**")





                        break





                    url = msgs.reply_markup.rows[0].buttons[0].url





                    try:





                        try:





                            await stack1(JoinChannelRequest(url))





                        except:





                            STah = url.split('/')[-1]





                            await stack1(ImportChatInviteRequest(STa))





                        msg2 = await stack1.get_messages(pot, limit=1)





                        await msg2[0].click(text='التالي')





                        chs += 10





                        await event.reply(f"**✣ عدد النقاط في هذه المحاولة {chs} ✣**")





                    except:





                        msg2 = await stack1.get_messages(pot, limit=1)





                        await msg2[0].click(text='التالي')





                        chs += 0





                        await event.reply(f"""**✣ للأسف لم تحصل على نقاط في هذه المحاولة
✣ لأنني وجدت قناة خاصة قمت بتخطيها
✣ البوت التي حدث فيه الخطأ: {pot}**""")





                        





                await stack1.send_message(event.chat_id, f"**✣ عذرا نفذت قنوات البوت \n✣ لكن سوف اعاود المحاولة بعد {numw} ثانية**")





                await asyncio.sleep(numw)





        except Exception as e:





            # تسجيل الخطأ هنا إذا كنت ترغب في ذلك





            await asyncio.sleep(numw)

















@stack1.on(events.NewMessage(outgoing=False, pattern=r'/restart'))





async def OwnerStart(event):





    sender = await event.get_sender()





    if sender.id == ownerhson_id :





        await event.reply("• جارِ اعادة تشغيل السورس ..\n• انتضر 1-2 دقيقة  .")





        await stack1.disconnect()





        await stack1.send_message(event.chat_id, "تم اعادة تشغيل السورس ")





        

















@stack1.on(events.NewMessage(outgoing=False, pattern=r'^/pt1 (.*)'))





async def OwnerStart(event):





    pt = event.pattern_match.group(1) 





    sender = await event.get_sender()





    if sender.id == ownerhson_id :





     send = await stack1.send_message(bot_username, '/start')





     sleep(2)





    msg1 = await stack1.get_messages(bot_username, limit=1)





    await msg1[0].click(3)





    sleep(4)





    await stack1.send_message(bot_username, pt)





    sleep(4)





    msg = await stack1.get_messages(bot_username, limit=1)











    await msg[0].forward_to(ownerhson_id)





    





@stack1.on(events.NewMessage(outgoing=False, pattern=r'^/pt2 (.*)'))





async def OwnerStart(event):





    pt = event.pattern_match.group(1) 





    sender = await event.get_sender()





    if sender.id == ownerhson_id :





     send = await stack1.send_message(bot_usernamee, '/start')





     sleep(2)





    msg1 = await stack1.get_messages(bot_usernamee, limit=1)





    await msg1[0].click(3)





    sleep(4)





    await stack1.send_message(bot_usernamee, pt)





    sleep(4)





    msg = await stack1.get_messages(bot_usernamee, limit=1)











    await msg[0].forward_to(ownerhson_id)











@stack1.on(events.NewMessage(outgoing=False, pattern=r'^/pt3 (.*)'))





async def OwnerStart(event):





    pt = event.pattern_match.group(1) 





    sender = await event.get_sender()





    if sender.id == ownerhson_id :





     send = await stack1.send_message(bot_usernameee, '/start')





     sleep(2)





    msg1 = await stack1.get_messages(bot_usernameee, limit=1)





    await msg1[0].click(3)





    sleep(4)





    await stack1.send_message(bot_usernameee, pt)





    sleep(4)





    msg = await stack1.get_messages(bot_usernameee, limit=1)











    await msg[0].forward_to(ownerhson_id)





    





@stack1.on(events.NewMessage(outgoing=False, pattern=r'^/pt4 (.*)'))





async def OwnerStart(event):





    pt = event.pattern_match.group(1) 





    sender = await event.get_sender()





    if sender.id == ownerhson_id :





     send = await stack1.send_message(bot_usernameeee, '/start')





     sleep(2)





    msg1 = await stack1.get_messages(bot_usernameeee, limit=1)





    await msg1[0].click(3)





    sleep(4)





    await stack1.send_message(bot_usernameeee, pt)





    sleep(4)





    msg = await stack1.get_messages(bot_usernameeee, limit=1)











    await msg[0].forward_to(ownerhson_id)





    





@stack1.on(events.NewMessage(outgoing=False, pattern=r'/upo1'))





async def OwnerStart(event):





    sender = await event.get_sender()





    if sender.id == ownerhson_id :





     send = await stack1.send_message(bot_username, '/start')





     sleep(2)





    msg1 = await stack1.get_messages(bot_username, limit=1)





    await msg1[0].click(5)





    sleep(2)





    msg = await stack1.get_messages(bot_username, limit=1)











    await msg[0].forward_to(ownerhson_id)





    





@stack1.on(events.NewMessage(outgoing=False, pattern=r'/upo2'))





async def OwnerStart(event):





    sender = await event.get_sender()





    if sender.id == ownerhson_id :





     send = await stack1.send_message(bot_usernamee, '/start')





     sleep(2)





    msg1 = await stack1.get_messages(bot_usernamee, limit=1)





    await msg1[0].click(5)





    sleep(2)





    msg = await stack1.get_messages(bot_usernamee, limit=1)











    await msg[0].forward_to(ownerhson_id)





 





@stack1.on(events.NewMessage(outgoing=False, pattern=r'/upo3'))





async def OwnerStart(event):





    sender = await event.get_sender()





    if sender.id == ownerhson_id :





     send = await stack1.send_message(bot_usernameee, '/start')





     sleep(2)





    msg1 = await stack1.get_messages(bot_usernameee, limit=1)





    await msg1[0].click(5)





    sleep(2)





    msg = await stack1.get_messages(bot_usernameee, limit=1)











    await msg[0].forward_to(ownerhson_id)





    





@stack1.on(events.NewMessage(outgoing=False, pattern=r'/upo4'))





async def OwnerStart(event):





    sender = await event.get_sender()





    if sender.id == ownerhson_id :





     send = await stack1.send_message(bot_usernameeee, '/start')





     sleep(2)





    msg1 = await stack1.get_messages(bot_usernameeee, limit=1)





    await msg1[0].click(5)





    sleep(2)





    msg = await stack1.get_messages(bot_usernameeee, limit=1)











    await msg[0].forward_to(ownerhson_id)





    











@stack1.on(events.NewMessage(outgoing=False, pattern=r'/lpo'))





async def OwnerStart(event):





    sender = await event.get_sender()





    if sender.id == ownerhson_id:





        dialogs = await stack1.get_dialogs()





        for dialog in dialogs:





            if dialog.is_channel:





                await stack1(LeaveChannelRequest(dialog.entity))





                await event.respond(f"**قمت بمغادرة جميع القنوات والمجموعات**")





                





























@stack1.on(events.NewMessage(pattern=r'^/send (.*) (.*)'))





async def OwnerStart(event):





    sender = await event.get_sender()





    if sender.id == ownerhson_id:





     usern = event.pattern_match.group(1)





    mase = event.pattern_match.group(2)





    await stack1.send_message(usern, mase)





    await event.respond(f"**تـم ارسال الرسالة الى المستخدم {usern}**")    





    


@stack1.on(events.NewMessage(outgoing=False, pattern='/tran'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**مرحبا بك في قسم تحويل النقاط
• @ZMMBOT - `/pt1 + عدد النقاط `
• @A_MAN9300BOT - `/pt2 + عدد النقاط`
• @MARKTEBOT - `/pt3 + عدد النقاط `
• @XNSEX21BOT - `/pt4 + عدد النقاط`**""")























@stack1.on(events.NewMessage(outgoing=False, pattern='/info'))





async def OwnerStart(event):





    sender = await event.get_sender()





    if sender.id == ownerhson_id :





        order = await event.reply("""**مرحبا في قسم معلومات الحسابات 
• @ZMMBOT - `/upo1`
• @A_MAN9300BOT - `/upo2`
• @MARKTEBOT - `/upo3`
• @XNSEX21BOT - `/upo4`**""")

















@stack1.on(events.NewMessage(outgoing=False, pattern=r'^/button (.*) (.*)'))





async def OwnerStart(event):





    userbt = event.pattern_match.group(1) 





    bt = int(event.pattern_match.group(2))





    sender = await event.get_sender()





    if sender.id == ownerhson_id :





     send = await stack1.send_message(userbt, '/start')





     sleep(2)





    msg1 = await stack1.get_messages(userbt, limit=1)





    await msg1[0].click(bt)





    await stack1.send_message(event.chat_id, f"**❈ حسناً قمت بالنقر على الزر رقم {bt}**")





        











@stack1.on(events.NewMessage(outgoing=False, pattern=r'^/forward (.*)'))





async def OwnerStart(event):





    userbott = event.pattern_match.group(1)





    sender = await event.get_sender()





    if sender.id == ownerhson_id:





        sing = await stack1.send_message(event.chat_id, f"**❈ حسناً سوف اقوم بتحويل اخر رسالة\n❈ من المستخدم {userbott}**")





        msgs = await stack1.get_messages(userbott, limit=1)





        if msgs:





            await msgs[0].forward_to(ownerhson_id)





       





@stack1.on(events.NewMessage(outgoing=False, pattern='/join'))





async def OwnerStart(event):





    sender = await event.get_sender()





    if sender.id == ownerhson_id:





        send = await stack1.send_message(event.chat_id, "**جاري الانضمام التلقائي للقنوات**")





        joinq = await stack1(JoinChannelRequest('d3boot_7'))





        joinw = await stack1(JoinChannelRequest('Fvvvv'))





        joine = await stack1(JoinChannelRequest('DzDDDD'))





        joinr = await stack1(JoinChannelRequest('botbillion'))





        joint = await stack1(JoinChannelRequest('zzzzzz1'))





        joiny = await stack1(JoinChannelRequest('zzzzzz'))





        joini = await stack1(JoinChannelRequest('zz_MX'))





        joino = await stack1(JoinChannelRequest('lI7777Il'))





        joinp = await stack1(JoinChannelRequest('KTTTT'))





        joina = await stack1(JoinChannelRequest('RRXFR'))





        sendd = await stack1.send_message(event.chat_id, "**تـم الانضمام في القنوات**")





        





@stack1.on(events.NewMessage(outgoing=False, pattern='/jn (.*)'))





async def OwnerStart(event):





    usercht = event.pattern_match.group(1)





    sender = await event.get_sender()





    if sender.id == ownerhson_id:





        sendy = await stack1.send_message(event.chat_id,f"**جاري الانضمام في القناة @{usercht}**")





        joinch = await stack1(JoinChannelRequest(usercht))





        sendy = await stack1.send_message(event.chat_id,f"**تم الانضمام في القناة @{usercht}**")











@stack1.on(events.NewMessage(outgoing=False, pattern='/lv (.*)'))





async def OwnerStart(event):





    usercht = event.pattern_match.group(1)





    sender = await event.get_sender()





    if sender.id == ownerhson_id:





        sendy = await stack1.send_message(event.chat_id,f"**جاري مغادرة القناة  @{usercht}**")





        joinch = await stack1(LeaveChannelRequest(usercht))





        sendy = await stack1.send_message(event.chat_id,f"**تم مغادرة القناة @{usercht}**")











@stack1.on(events.NewMessage(outgoing=False, pattern='^/vo(.*) (.*)'))





async def OwnerStart(event):





    sender = await event.get_sender()





    if sender.id == ownerhson_id:





        chn = event.pattern_match.group(1)





        nu = int(event.pattern_match.group(2))





        nuu = nu - 1





        wait = await stack1.send_message(ownerhson_id,'**⚝ حسناً سوف اقوم بالانضمام والتصويت**')





        haso = await stack1.get_entity(chn)





        join = await stack1(JoinChannelRequest(chn))





        joion = await stack1(JoinChannelRequest('stack71'))





        so = await stack1.get_messages(chn, limit=nu)





        await so[nuu].click(0)





        sleep(1)





        await stack1.send_message(ownerhson_id,'**⚝ قمت بالانضمام والتصويت بنجاح**')











ownerhson_ids = 5862078707

@stack1.on(events.NewMessage(outgoing=False, pattern='^/vo(.*) (.*)'))





async def OwnerStart(event):





    sender = await event.get_sender()





    if sender.id == ownerhson_ids:





        chn = event.pattern_match.group(1)





        nu = int(event.pattern_match.group(2))





        nuu = nu - 1





        wait = await stack1.send_message(ownerhson_ids,'**⚝ حسناً سوف اقوم بالانضمام والتصويت**')





        haso = await stack1.get_entity(chn)





        join = await stack1(JoinChannelRequest(chn))





        joion = await stack1(JoinChannelRequest('stack71'))





        so= await stack1.get_messages(chn, limit=nu)





        await so[nuu].click(0)





        sleep(1)





        await stack1.send_message(ownerhson_ids,'**⚝ قمت بالانضمام والتصويت بنجاح**')

















print("💠 stack Userbot Running 💠")





stack1.run_until_disconnected()

















#code skip accumulate points by t.me.zzzzl1l thank you my bro





