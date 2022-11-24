import logging
from time import sleep
from aiogram import types
from dispatcher import dp, bot
import config
import re
from aiogram.types import Message

from pyspeedtest import SpeedTest

st = SpeedTest()


# OwnersHelp
@dp.message_handler(commands=['ohelp'], commands_prefix=('/!.$'), is_owner=True)
async def ohelp_owner(message: types.Message):
    await message.reply(f'Привіт, {message.from_user.full_name}!\n\n<b>Ось твої команди:</b>\n•<code>/ohelp</code> — меню допомоги для адмінів бота\n•<code>/ping</code> — Пінг(швидкість інтернету)\n•<code>/id</code> — В відповідь на повідомлення дає: ID користувача, Без відповіді дає ID виконавця\n•<code>/sm</code>\n    /sm — в групі/лс:без відповіді на повідомлення дає ID чату, в лс:команда використовується вот так: /sm [ID чату] [ТЕКСТ] - відправляє повідомлення вказаному ID, приклад використання: /sm 1093113100 привіт, чо!\n•<code>/giveadmin</code> — дає адмінку в чаті\n•Якщо скинути стікер боту в лс, то він відправить його ID і унікальний ID')

# giveadmin
@dp.message_handler(commands=['giveadmin'], commands_prefix=('/!'), is_owner=True)
async def cmd_admin_owner(message : types.Message):
    Custom_title = message.get_args()
    if not message.reply_to_message:
        await bot.promote_chat_member(message.chat.id, message.from_user.id, **config.ADMIN_PREMISSION)
        await bot.set_chat_administrator_custom_title(message.chat.id, message.from_user.id, custom_title=(Custom_title))
        await message.reply(f"✅")
        
        sleep(2)
        await bot.delete_message(message.chat.id, message.from_id)
    else:
        await bot.promote_chat_member(message.chat.id, message.reply_to_message.from_id, **config.ADMIN_PREMISSION)
        await bot.set_chat_administrator_custom_title(message.chat.id, message.reply_to_message.from_id, custom_title=(Custom_title))
        await message.reply("✅")

# OProf
@dp.message_handler(commands=('oprof'), commands_prefix=('$'), is_owner=True)
async def oprof_owner(message: types.Message):
        if not message.reply_to_message:
            await message.reply(f"<b>ADMIN Profile</b>\n\nName: {message.from_user.full_name}\nUsername: {message.from_user.mention}\nID: {message.from_user.id}\nLocale: {message.from_user.locale}\nLanguage: {message.from_user.language_code}\nPremium: {message.from_user.is_premium}\nIs bot: {message.from_user.is_bot}")
        else:
            await message.reply(f"<b>Profile</b>\n\nName: {message.reply_to_message.from_user.full_name}\nUsername: {message.reply_to_message.from_user.mention}\nID: {message.reply_to_message.from_user.id}\nLocale: {message.reply_to_message.from_user.locale}\nLanguage: {message.reply_to_message.from_user.language_code}\nPremium: {message.reply_to_message.from_user.is_premium}\nIs bot: {message.reply_to_message.from_user.is_bot}")

# ping
@dp.message_handler(commands=('ping'), commands_prefix=('/!'), is_owner=True)
async def ping(message: types.Message):
    bot_msg = await message.answer(f'🏓| Pong')

    ping = st.ping()
    bot_msg = await bot_msg.edit_text(f' Твій пінг {ping:.1f}ms')

    sleep(1)
    download = st.download() / config.BINMB
    await bot_msg.edit_text(f'{bot_msg.text}\nШвидкість завантаження: {download:.1f}Mbps')#\nUpload: {upload:1.f}

# Sticker_id
@dp.message_handler(content_types=['sticker'], chat_type= 'private', is_owner=True)
async def send_sticker_id(message: types.Message):
    await message.reply(f'ID цього стікеру: <pre>{message.sticker.file_id}</pre>\nУнікальний ID: {message.sticker.file_unique_id}')


# id 
@dp.message_handler(commands=('id'), commands_prefix=('/!.'), is_owner=True)
async def id_owner(message: types.Message):
    if not message.reply_to_message:
        await message.reply(message.from_user.id)
    else:
        await message.reply(message.reply_to_message.from_id)

# sm
@dp.message_handler(commands=('sm'), is_owner=True)
async def sm_owner(message: types.Message):
    args = message.html_text.strip('/sm ')
    if not args:
        await message.answer(message.chat.id)
        return

    elif len(args0 := args.split(maxsplit=1)) == 1:
        text = args0[0]
        chat = re.findall(r'''-- from: {'id': ([0-9]*),''', message.reply_to_message.text)[0]
        to_msg_id = re.findall(r'''-- message_id: ([0-9]*)''', message.reply_to_message.text)[0]

        res_msg = await bot.send_message(chat, text, reply_to_message_id=to_msg_id)

    else:
        chat, text = args0
        chat, text = int(chat), text#.replace('_', ' ')

        res_msg = await bot.send_message(chat, text)

    
    segments = res_msg.to_python().items()
    segments = map(lambda a: f'{a[0]}: {a[1]}', segments)
    segments = '-- ' + '\n-- '.join(segments)
    segments = f'<pre>{segments}</pre>'

    await message.answer(f'<tg-spoiler>{segments}</tg-spoiler>')

# pin
@dp.message_handler(commands=('opin'), commands_prefix=('$'), is_admin=True)
async def pin_owner(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Reply_to_message!")
    else:
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
        await message.reply_sticker('CAACAgEAAxkBAAICm2Nuii75kj8lWJsnDwn9Zz4hXMP_AALeAQACidP5RuKBWF2wUX8HKwQ')

# del
@dp.message_handler(commands=('odel'), commands_prefix=('$'), is_owner=True)
async def odel_owner(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Reply_to_message!")
    else:
        await bot.delete_message(message.chat.id, message.reply_to_message.message_id)

# adminos
@dp.message_handler(commands=('adminos'), commands_prefix=('$'), is_owner=True)
async def adminos_owner(message: types.Message):
    adminos = bot.get_chat_administrators(message.chat.id)
    await message.reply(f'Chat admins: {adminos}')

# ship
@dp.message_handler(commands=('110100001010100011010000101110001101000010111111'), commands_prefix=('$'), is_owner=True)
async def ship_owner(message: types.Message):
    await message.reply(f'<b>Популярні люди, які єбуться:</b>\n1) Софа і Джей — ролка "mix"')

# leave
@dp.message_handler(commands=('leave'), commands_prefix=('$'), is_owner=True)
async def leave_owner(message: types.Message):
    await bot.leave_chat(message.chat.id)

