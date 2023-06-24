#(c) Spidy-Naik
import os
import asyncio
from asyncio import TimeoutError
from Spidy.bot import StreamBot
from Spidy.utils.database import Database
from Spidy.utils.human_readable import humanbytes
from Spidy.vars import Var
from urllib.parse import quote_plus
from pyrogram import filters, Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from Spidy.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.name)


"""MY_PASS = os.environ.get("MY_PASS", None)
pass_dict = {}
pass_db = Database(Var.DATABASE_URL, "ag_passwords")


@StreamBot.on_message((filters.regex("ʟᴏɢɪɴ🔑") | filters.command("login")) , group=4)
async def login_handler(c: Client, m: Message):
    try:
        try:
            ag = await m.reply_text("Nᴏᴡ sᴇɴᴅ ᴍᴇ ᴘᴀssᴡᴏʀᴅ.\n\n Eɴᴛᴇʀ ᴛʜᴇ ᴘᴀssᴡᴏʀᴅ ᴀs 0000 \n\n(You can use /cancel command to cancel the process)")
            _text = await c.listen(m.chat.id, filters=filters.text, timeout=90)
            if _text.text:
                textp = _text.text
                if textp == "/cancel":
                   await ag.edit("ᴘʀᴏᴄᴇss ᴄᴀɴᴄᴇʟʟᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ")
                   return
            else:
                return
        except TimeoutError:
            await ag.edit("ɪ ᴄᴀɴ'ᴛ ᴡᴀɪᴛ ᴍᴏʀᴇ ғᴏʀ ᴘᴀssᴡᴏʀᴅ, ᴛʀʏ ᴀɢᴀɪɴ")
            return
        if textp == MY_PASS:
            await pass_db.add_user_pass(m.chat.id, textp)
            ag_text = "ʏᴇᴀʜ! ʏᴏᴜ ᴇɴᴛᴇʀᴇᴅ ᴛʜᴇ ᴘᴀssᴡᴏʀᴅ ᴄᴏʀʀᴇᴄᴛʟʏ"
        else:
            ag_text = "Wrong password, try again"
        await ag.edit(ag_text)
    except Exception as e:
        print(e) """

@StreamBot.on_message((filters.private) & (filters.document | filters.video | filters.audio | filters.photo) , group=4)
async def private_receive_handler(c: Client, m: Message):
    """if MY_PASS:
        check_pass = await pass_db.get_user_pass(m.chat.id)
        if check_pass== None:
            await m.reply_text("Login first using /login cmd \n Password is 0000")
            return
        if check_pass != MY_PASS:
            await pass_db.delete_user(m.chat.id)
            return
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await c.send_message(
            Var.BIN_CHANNEL,
            f"New User Joined! : \n\n Name : [{m.from_user.first_name}](tg://user?id={m.from_user.id}) Started Your Bot!!"
        )"""
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await c.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == "kicked":
                await c.send_message(
                    chat_id=m.chat.id,
                    text="You are banned!\n\n  **Cᴏɴᴛᴀᴄᴛ Dᴇᴠᴇʟᴏᴘᴇʀ [𝐌𝐫.𝐒𝐏𝐈𝐃𝐘 ×͜×](https://t.me/Mr_SpidyBot) ʜᴇ Wɪʟʟ Hᴇʟᴘ Yᴏᴜ**",
                    
                    disable_web_page_preview=True
                )
                return 
        except UserNotParticipant:
            await c.send_message(
                chat_id=m.chat.id,
                text="""<i>𝙹𝙾𝙸𝙽 UPDATES CHANNEL 𝚃𝙾 𝚄𝚂𝙴 𝙼𝙴 🔐</i>""",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Jᴏɪɴ ɴᴏᴡ 🔓", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
            )
            return
        except Exception as e:
            await m.reply_text(e)
            await c.send_message(
                chat_id=m.chat.id,
                text="**Sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ Wʀᴏɴɢ. Cᴏɴᴛᴀᴄᴛ ᴍʏ ʙᴏss** [𝐌𝐫.𝐒𝐏𝐈𝐃𝐘 ×͜×](https://t.me/Mr_SpidyBot)",
                
                disable_web_page_preview=True)
            return
    try:
        log_msg = await m.forward(chat_id=Var.BIN_CHANNEL)
        stream_link = f"{Var.URL}watch/{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"
        online_link = f"{Var.URL}{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"
       
        msg_text ="""<i><u>𝗬𝗼𝘂𝗿 𝗟𝗶𝗻𝗸 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 !</u></i>\n\n<b>📂 Fɪʟᴇ ɴᴀᴍᴇ :</b> <i>{}</i>\n\n<b>📦 Fɪʟᴇ ꜱɪᴢᴇ :</b> <i>{}</i>\n\n<b>🚸 Nᴏᴛᴇ : LINK WON'T EXPIRE TILL I DELETE\nMᴀɪɴᴛᴀɪɴ Bʏ @YourDemandZone♻️</b>"""

        await log_msg.reply_text(text=f"**RᴇQᴜᴇꜱᴛᴇᴅ ʙʏ :** [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n**Uꜱᴇʀ ɪᴅ :** `{m.from_user.id}`\n**Stream ʟɪɴᴋ :** {stream_link}", disable_web_page_preview=True,  quote=True)
        await m.reply_text(
            text=msg_text.format(get_name(log_msg), humanbytes(get_media_file_size(m)), online_link, stream_link),
            quote=True,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Sᴛʀᴇᴀᴍɪɴɢ 🎬", callback_data='stream'), #Call Stream
                                                InlineKeyboardButton('Dᴏᴡɴʟᴏᴀᴅ 📥', url=online_link)], #Download Link
                                                [InlineKeyboardButton("🍀 Jᴏɪɴ Mᴏᴠɪᴇ Gʀᴏᴜᴘ 🍀", url="https://t.me/+UA8rF845SWk4ZjU1")]]) 
        )
    except FloodWait as e:
        print(f"Sleeping for {str(e.x)}s")
        await asyncio.sleep(e.x)
        await c.send_message(chat_id=Var.BIN_CHANNEL, text=f"Gᴏᴛ FʟᴏᴏᴅWᴀɪᴛ ᴏғ {str(e.x)}s from [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n\n**𝚄𝚜𝚎𝚛 𝙸𝙳 :** `{str(m.from_user.id)}`", disable_web_page_preview=True)

@StreamBot.on_callback_query(filters.regex(r'stream'))
async def stream_callback_handler(c: Client, query: CallbackQuery):
    try:
        data = query.data
        if query.data == "close_data":
            await query.message.delete()
        
            # Retrieve the necessary information for streaming
            log_msg = await c.get_message(chat_id, message_id)
            stream_link = f"{Var.URL}watch/{str(log_msg.message_id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"
            online_link = f"{Var.URL}{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"
    
            # Implement your streaming logic here
            # You can use the 'stream_link' variable for the stream URL
        elif query.data == "stream":
            buttons = [[
                 InlineKeyboardButton('ʙʀᴏᴡsᴇʀ', url=stream_link),
                 InlineKeyboardButton('ᴍx ᴘʟᴀʏᴇʀ', url='intent:online_link#Intent;package=com.mxtech.videoplayer.ad;S.title=Power by @YourDemandZone ;end'),
            ],  [
                 InlineKeyboardButton('ᴠʟᴄ & ᴠᴅx', url='vlc://online_link'),
                 InlineKeyboardButton('ᴘʟᴀʏɪᴛ', url='playit://playerv2/video?url=online_link')
            ],[
                InlineKeyboardButton('ᴅᴏᴡɴʟᴏᴀᴅ', url=online_link),
                InlineKeyboardButton('ᴄᴏɴᴛᴀᴄᴛ', url='htps://t.me/Mr_SpidyBot')
            ],[
                InlineKeyboardButton('ᴊᴏɪɴ ʏᴅᴢᴏɴᴇ', url='htps://t.me/YourDemandZone')
            ]]
    except Exception as e:
        await c.answer_callback_query(
            callback_query_id=query.id,
            text="Something went wrong."
        )

@StreamBot.on_message(filters.channel & ~filters.group & (filters.document | filters.video | filters.photo)  & ~filters.forwarded, group=-1)
async def channel_receive_handler(bot, broadcast):
    if MY_PASS:
        check_pass = await pass_db.get_user_pass(broadcast.chat.id)
        if check_pass == None:
            await broadcast.reply_text("Login first using /login cmd \n Password is 0000")
            return
        if check_pass != MY_PASS:
            await broadcast.reply_text("Wrong password, login again")
            await pass_db.delete_user(broadcast.chat.id)
            
            return
    if int(broadcast.chat.id) in Var.BANNED_CHANNELS:
        await bot.leave_chat(broadcast.chat.id)
        
        return
    try:
        log_msg = await broadcast.forward(chat_id=Var.BIN_CHANNEL)
        stream_link = f"{Var.URL}watch/{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"
        online_link = f"{Var.URL}{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"
        await log_msg.reply_text(
            text=f"**Channel Name:** `{broadcast.chat.title}`\n**CHANNEL ID:** `{broadcast.chat.id}`\n**Rᴇǫᴜᴇsᴛ ᴜʀʟ:** {stream_link}",
            quote=True
        )
        await bot.edit_message_reply_markup(
            chat_id=broadcast.chat.id,
            message_id=broadcast.id,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Sᴛʀᴇᴀᴍɪɴɢ 🎬", url=stream_link),
                     InlineKeyboardButton('Dᴏᴡɴʟᴏᴀᴅ 📥', url=online_link)],
                    [InlineKeyboardButton("🍀 Jᴏɪɴ Mᴏᴠɪᴇ Gʀᴏᴜᴘ 🍀", url="https://t.me/+UA8rF845SWk4ZjU1")]
                ]
            )
        )
    except FloodWait as w:
        print(f"Sleeping for {str(w.x)}s")
        await asyncio.sleep(w.x)
        await bot.send_message(chat_id=Var.BIN_CHANNEL,
                             text=f"GOT FLOODWAIT OF {str(w.x)}s FROM {broadcast.chat.title}\n\n**CHANNEL ID:** `{str(broadcast.chat.id)}`",
                             disable_web_page_preview=True)
    except Exception as e:
        await bot.send_message(chat_id=Var.BIN_CHANNEL, text=f"**#ERROR_TRACKEBACK:** `{e}`", disable_web_page_preview=True)
        print(f"Cᴀɴ'ᴛ Eᴅɪᴛ Bʀᴏᴀᴅᴄᴀsᴛ Mᴇssᴀɢᴇ!\nEʀʀᴏʀ:  **Give me edit permission in updates and bin Channel!{e}**")
