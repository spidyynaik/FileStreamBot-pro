# (c) adarsh-goel 
from Adarsh.bot import StreamBot
from Adarsh.vars import Var
import logging
logger = logging.getLogger(__name__)
#from Adarsh.bot.plugins.stream import MY_PASS
from Adarsh.utils.human_readable import humanbytes
from Adarsh.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from Adarsh.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.name)
from pyrogram.types import ReplyKeyboardMarkup

buttonz = ReplyKeyboardMarkup(
    [
        ["𝐒𝐭𝐚𝐫𝐭⚡️", "𝐇𝐞𝐥𝐩📚", "𝐒𝐭𝐚𝐭𝐮𝐬📊"],
        ["𝐂𝐡𝐚𝐧𝐧𝐞𝐥♻️", "𝐏𝐢𝐧𝐠📡","𝐂𝐫𝐞𝐚𝐭𝐨𝐫😎"]
    ],
    resize_keyboard=True
)

            
@StreamBot.on_message((filters.command("start") | filters.regex('𝐒𝐭𝐚𝐫𝐭⚡️')) & filters.private )
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"**Nᴇᴡ Usᴇʀ Jᴏɪɴᴇᴅ:** \n\n__Mʏ Nᴇᴡ Fʀɪᴇɴᴅ__ [{m.from_user.first_name}](tg://user?id={m.from_user.id}) __Sᴛᴀʀᴛᴇᴅ Yᴏᴜʀ Bᴏᴛ !!__"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == "kicked":
                await b.send_message(
                    chat_id=m.chat.id,
                    text="__𝓢𝓞𝓡𝓡𝓨, 𝓨𝓞𝓤 𝓐𝓡𝓔 𝓐𝓡𝓔 𝓑𝓐𝓝𝓝𝓔𝓓 𝓕𝓡𝓞𝓜 𝓤𝓢𝓘𝓝𝓖 𝓜𝓔. 𝓒ᴏɴᴛᴀᴄᴛ ᴛʜᴇ 𝓓ᴇᴠᴇʟᴏᴘᴇʀ__\n\n  **𝙃𝙚 𝙬𝙞𝙡𝙡 𝙝𝙚𝙡𝙥 𝙮𝙤𝙪**",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
             await StreamBot.send_photo(
                chat_id=m.chat.id,
                photo="https://telegra.ph/file/6035c9116c8e118408a35.jpg",
                caption="<i>𝙹𝙾𝙸𝙽 CHANNEL 𝚃𝙾 𝚄𝚂𝙴 𝙼𝙴🔐</i>",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Jᴏɪɴ ɴᴏᴡ 🔓", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
            )
             return
        except Exception:
            await b.send_message(
                chat_id=m.chat.id,
                text="<i>𝓢𝓸𝓶𝓮𝓽𝓱𝓲𝓷𝓰 𝔀𝓮𝓷𝓽 𝔀𝓻𝓸𝓷𝓰</i> <b> <a href='https://t.me/Mr_Spidybot'>CLICK HERE FOR SUPPORT </a></b>",
                
                disable_web_page_preview=True)
            return
    await StreamBot.send_photo(
        chat_id=m.chat.id,
        photo ="https://graph.org/file/72689fe7b446757d5b4e7.jpg",
        caption =f' Hᴇʏ, {m.from_user.mention(style="md")}\nIᴍ Tᴇʟᴇɢʀᴀᴍ Fɪʟᴇs Sᴛʀᴇᴀᴍɪɴɢ Bᴏᴛ ᴀs ᴡᴇʟʟ Dɪʀᴇᴄᴛ Lɪɴᴋs Gᴇɴᴇʀᴀᴛᴇ.\nCʟɪᴄᴋ ᴏɴ Hᴇʟᴘ ᴛᴏ ɢᴇᴛ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ\n<u>𝗪𝗔𝗥𝗡𝗜𝗡𝗚 🚸</u>\n🔞 Pᴏʀɴ ᴄᴏɴᴛᴇɴᴛꜱ ʟᴇᴀᴅꜱ ᴛᴏ ᴘᴇʀᴍᴀɴᴇɴᴛ ʙᴀɴ ʏᴏᴜ.\n<b>🥀 Bᴏᴛ Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ :@YourDemandZone</b>',
        reply_markup=buttonz)


@StreamBot.on_message((filters.command("help") | filters.regex('𝐇𝐞𝐥𝐩📚')) & filters.private )
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"**Nᴇᴡ Usᴇʀ Jᴏɪɴᴇᴅ **\n\n__Mʏ Nᴇᴡ Fʀɪᴇɴᴅ__ [{message.from_user.first_name}](tg://user?id={message.from_user.id}) __Started Your Bot !!__"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="<i>Sᴏʀʀʏ Sɪʀ, Yᴏᴜ ᴀʀᴇ Bᴀɴɴᴇᴅ FROM USING ᴍᴇ. Cᴏɴᴛᴀᴄᴛ ᴛʜᴇ Dᴇᴠᴇʟᴏᴘᴇʀ</i>",
                    
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await StreamBot.send_photo(
                chat_id=message.chat.id,
                photo="https://telegra.ph/file/ca10e459bc6f48a4ad0f7.jpg",
                Caption="**𝙹𝙾𝙸𝙽 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙶𝚁𝙾𝚄𝙿 𝚃𝙾 𝚄𝚂𝙴 ᴛʜɪs Bᴏᴛ!**\n\n__Dᴜᴇ ᴛᴏ Oᴠᴇʀʟᴏᴀᴅ, Oɴʟʏ Cʜᴀɴɴᴇʟ Sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜᴇ Bᴏᴛ!__",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🤖 Jᴏɪɴ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="__Sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ Wʀᴏɴɢ. Cᴏɴᴛᴀᴄᴛ ᴍᴇ__ [𝐌𝐫.𝐒𝐏𝐈𝐃𝐘 ×͜×](https://t.me/Mr_SpidyBot).",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text="""<b>Sᴇɴᴅ ᴍᴇ ᴀɴʏ ғɪʟᴇ ᴏʀ ᴠɪᴅᴇᴏ ɪ ᴡɪʟʟ ɢɪᴠᴇ ʏᴏᴜ sᴛʀᴇᴀᴍᴀʙʟᴇ ʟɪɴᴋ ᴀɴᴅ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ.</b>\n
<b> I ᴀʟsᴏ sᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟs, Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ sᴇɴᴅ ᴀɴʏ ᴍᴇᴅɪᴀ ғɪʟᴇs ᴀɴᴅ sᴇᴇ ᴛʜᴇ ᴍᴀɢɪᴄ✨""",
        
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("💁‍♂️ Dᴇᴠ", url="https://t.me/Mr_Spidy")],
                [InlineKeyboardButton("💥 Uᴘᴅᴀᴛᴇ", url="https://t.me/YourDemandZone")]
            ]
        )
    )
