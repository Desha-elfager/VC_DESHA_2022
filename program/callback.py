

from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **مرحبا [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) يسمح لك بتشغيل الموسيقى والفيديو في مجموعات من خلال محادثات الفيديو الجديدة في Telegram!**

💡 **اكتشف جميع أوامر الروبوت وكيفية عملها من خلال النقر فوق » 📚 زر الأوامر!**

🔖 **لمعرفة كيفية استخدام هذا الروبوت, الرجاء الضغط على » ❓ زر الدليل الأساسي!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اضغط لـ اضافتي لمجموعتك ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("❓ طريقة التفعيل", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("📚 الاوامر", callback_data="cbcmds"),
                    InlineKeyboardButton("❤ المطور", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "👥 جروب الدعم", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 قناة السورس", url=f"https://t.me/music_Desha1"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "مساعده", url="https://t.me/music_Desha"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **الدليل الأساسي لاستخدام هذا الروبوت:**

1.) **اولا, أضفني إلى مجموعتك.**
2.) **ثانيا, قم بترقيتي كمسؤول ومنح جميع الأذونات باستثناء المسؤول المجهول.**
3.) **بعد ترقيتي, نوع /reload في مجموعة لتحديث بيانات المسؤول.**
3.) **يضيف @{ASSISTANT_NAME} لمجموعتك أو اكتب /userbotjoin لدعوتها.**
4.) **قم بتشغيل محادثة الفيديو أولاً قبل البدء في تشغيل الفيديو/موسيقي.**
5.) **أحيانا, إعادة تحميل الروبوت باستخدام /reload يمكن أن يساعدك الأمر في حل بعض المشكلات.**

📌 **إذا لم ينضم المستخدم الروبوت إلى دردشة الفيديو, تأكد من تشغيل دردشة الفيديو بالفعل, أو اكتب /userbotleave ثم اكتب /userbotjoin تكرارا.**

💡 **Iإذا كان لديك متابعة-فوق أسئلة حول هذا الروبوت, يمكنك معرفة ذلك في دردشة الدعم الخاصة بي هنا: @{GROUP_SUPPORT}**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 الرجوع", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **مرحبا [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» **اضغط على الزر أدناه لقراءة الشرح ومشاهدة قائمة الأوامر المتاحة !**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👷🏻 اوامر الادمن", callback_data="cbadmin"),
                    InlineKeyboardButton("🧙🏻 اوامر متقدمه", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("📚 اوامر التشغيل", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("🔙 الرجوع", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 هنا الأوامر الأساسية:

» /mplay (song name/link) - play music on video chat
» /stream (query/link) - stream the yt live/radio live music
» /vplay (video name/link) - play video on video chat
» /vstream - play live video from yt live/m3u8
» /playlist - show you the playlist
» /video (query) - download video from youtube
» /song (query) - download song from youtube
» /lyric (query) - scrap the song lyric
» /search (query) - search a youtube video link

» /ping - show the bot ping status
» /uptime - show the bot uptime status
» /alive - show the bot alive info (in group)

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 الرجوع", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 هنا أوامر المسؤول:

» /pause - pause the stream
» /resume - resume the stream
» /skip - switch to next stream
» /stop - stop the streaming
» /vmute - mute the userbot on voice chat
» /vunmute - unmute the userbot on voice chat
» /volume `1-200` - adjust the volume of music (userbot must be admin)
» /reload - reload bot and refresh the admin data
» /userbotjoin - invite the userbot to join group
» /userbotleave - order userbot to leave from group

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 الرجوع", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 هنا اوامر متقدمه:

» /rmw - clean all raw files
» /rmd - clean all downloaded files
» /sysinfo - show the system information
» /update - update your bot to latest version
» /restart - restart your bot
» /leaveall - order userbot to leave from all group

⚡ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 الرجوع", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 المسؤول الوحيد الذي لديه إذن إدارة الدردشات الصوتية يمكنه النقر على هذا الزر !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **settings of** {query.message.chat.title}\n\n⏸ : pause stream\n▶️ : resume stream\n🔇 : mute userbot\n🔊 : unmute userbot\n⏹ : stop stream",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("⏹", callback_data="cbstop"),
                      InlineKeyboardButton("⏸", callback_data="cbpause"),
                      InlineKeyboardButton("▶️", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("🗑 حذف", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("❌ لا شيء يتدفق حاليا", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 المسؤول الوحيد الذي لديه إذن إدارة الدردشات الصوتية يمكنه النقر على هذا الزر !", show_alert=True)
    await query.message.delete()