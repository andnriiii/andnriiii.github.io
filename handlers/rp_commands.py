from time import sleep
from aiogram import types
from dispatcher import bot, dp
import config
from aiogram.dispatcher.filters import Text
import html
import emoji
import random
import time



# Trah
@dp.message_handler(text=['трахнути', 'Трахнути'])
async def trah_rp(message: types.Message):
    if not message.reply_to_message:    
        await message.answer(f'{message.from_user.full_name} трахнув сам себе')
    else:
        await message.answer(f'{message.from_user.full_name} жоска відтрахав {message.reply_to_message.from_user.full_name} в попачкю')

# Samogubstvo
@dp.message_handler(text=['самогубство', 'Самогубство'])
async def samogubstvo_rp(message: types.Message):
    await message.answer(f'{message.from_user.full_name} наклав собі в руки')

# Srobyt vystril
@dp.message_handler(text=['вистрілити', 'Вистрілити'])
async def vystril_rp(message: types.Message):
    if not message.reply_to_message:
        await message.answer(f'{message.from_user.full_name} вистрілив в повітря')
    else:
        list_vystril = [f'{message.from_user.full_name} стріляє в {message.reply_to_message.from_user.full_name}, але не попадає', f'{message.from_user.full_name} стріляє в {message.reply_to_message.from_user.full_name} і попадає! Юхууу']
        await message.answer(random.choice(list_vystril))

# baccino
@dp.message_handler(text=['поцілувати', 'Поцілувати', 'поцілувать', 'Поцілувать'])
async def baccino_rp(message: types.Message):
    if not message.reply_to_message:
        await message.reply(f'ти хочеш поцілувати сам себе?')
    else:
        list_baccino = ['щічку', 'губи', 'ніс', 'лоб']
        await message.answer(f'{message.from_user.full_name} поцілував в {random.choice(list_baccino)} {message.reply_to_message.from_user.full_name}')

# udar
@dp.message_handler(text=['Уєбати', 'уєбати'])
async def udar_rp(message: types.Message):
    if not message.reply_to_message:
        await message.answer(f'{message.from_user.full_name} уєбав сам себе')
    else:
        if message.reply_to_message.from_user.id == 1093113100:
            await message.reply(f'мого создатєля нізя бить, йди нахуй!')
        else:
            await message.answer(f'{message.from_user.full_name} уєбав нахуй {message.reply_to_message.from_user.full_name}')


# дії 1, 3 лице
@dp.message_handler(commands=['me'], commands_prefix=('/'))
async def me_rp(message: types.Message):
    me = message.get_args()
    await message.delete()
    await message.answer(f'<i>{message.from_user.full_name} {me}</i>')