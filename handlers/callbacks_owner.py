from time import sleep
from aiogram import types
from dispatcher import dp, bot
import config
import re

from pyspeedtest import SpeedTest

st = SpeedTest()

# OMenu
@dp.message_handler(commands=('omenu'), commands_prefix=('$'), is_owner=True)
async def omenu_owner(message: types.Message):    
    buttons = [
        types.InlineKeyboardButton(text="Допомога", callback_data="ohelp"),
        types.InlineKeyboardButton(text="Пінг", callback_data="ping"),
        types.InlineKeyboardButton(text="⚠️LEAVE⚠️", callback_data="leave")
    ]
    
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    await message.answer(f"Привіт, {message.from_user.full_name}!\nЯ бачу ти є в моєму списку адмінів!\n\nв цьому меню ти можеш:", reply_markup=keyboard)


@dp.callback_query_handler(text="ohelp", is_owner=True)
async def callback_ohelp(call: types.CallbackQuery):
    await call.message.edit_text('<b>Ось твої команди:</b>\n•<code>/ohelp</code> — меню допомоги для адмінів бота\n•<code>/ping</code> — Пінг(швидкість інтернету)\n•<code>/id</code> — В відповідь на повідомлення дає: ID користувача, Без відповіді дає ID виконавця\n•<code>/sm</code>\n    /sm — в групі/лс:без відповіді на повідомлення дає ID чату, в лс:команда використовується вот так: /sm [ID чату] [ТЕКСТ] - відправляє повідомлення вказаному ID, приклад використання: /sm 1093113100 привіт, чо!\n•<code>/giveadmin</code> — дає адмінку в чаті, також після самої команди можна вказати кличку адмінки\n•<code>$oprof</code> — інформація про користувача\n\n•Якщо скинути стікер боту в лс, то він відправить його ID і унікальний ID')
    await call.answer()


@dp.callback_query_handler(text="ping", is_owner=True)
async def callback_ping(call: types.CallbackQuery):
    bot_msg = await call.message.answer(f'🏓| Pong')

    ping = st.ping()
    bot_msg = await bot_msg.edit_text(f' Твій пінг {ping:.1f}ms')

    sleep(1)
    download = st.download() / config.BINMB
    await bot_msg.edit_text(f'{bot_msg.text}\nШвидкість завантаження: {download:.1f}Mbps')#\nUpload: {upload:1.f}
    await call.answer()

@dp.callback_query_handler(text="leave", is_owner=True)
async def callback_leave(call: types.CallbackQuery):
    await bot.leave_chat(call.message.chat.id)
    await call.answer()