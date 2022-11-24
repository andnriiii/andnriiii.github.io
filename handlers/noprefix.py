from time import sleep
from aiogram import types
from dispatcher import bot, dp
import config
from aiogram.dispatcher.filters import Text
import html
import emoji
import random
import time

my_list = ['пр пупсік', 'привіт', 'прпр', 'пр', 'прив', 'хай', 'хеллоу!']

# Hello
@dp.message_handler(text=['пр пупсік', 'пр', 'привіт', 'привет пупсик', 'привіт пупсік', 'пр пупсик', 'пр квард', 'Пр'])
async def hello_command(message: types.Message):
    await message.reply(f'{random.choice(my_list)} {message.from_user.full_name}')

# testtests
@dp.message_handler(text=['хто це'])
async def chie_command(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Пиши в відповідь на повідомлення(тільки не своє, надіюсь ти не єблан)")
    else:
        await message.reply(f'Це {message.reply_to_message.from_user.full_name}')


# Pupsik
@dp.message_handler(text=['пупс', 'Пупс', 'Пупсик', 'пупсик', 'пупсік', 'Пупсік'])
async def pupsik_command(message: types.Message):
    await message.reply("Го в попочкю?🥵😘")
    await message.chat.do('choose_sticker')

    sleep(2)
    await message.answer_sticker(f'CAACAgIAAx0CY9d2ngABAojtY2qLJpqp-kmMIUGJ3orfhKsJJy4AAhgeAAJe_RhJz_tWnfMlfS8rBA')

# Quard
@dp.message_handler(text=['квард', 'Квард', 'Квардик'])
async def quard_command(message: types.Message):
    await message.reply("я тут. шо хоч?")

# Tipok
@dp.message_handler(text=['тіпок', 'Тіпок', 'типок', 'тіпок'])
async def tipok(message: types.Message):
    await message.reply(".")

# kapsho
@dp.message_handler(text=['капшо'])
async def kapsho_command(message: types.Message):
    await message.reply("йди нахуй зі своїм капшо")
    await message.chat.do('choose_sticker')

    sleep(1)
    await bot.send_sticker('CAACAgEAAxkBAAMEY2bqjosZYfZ1JkMbc8TuQPlVR1oAAnUBAAJ0wPFGOl5jUSP9GyErBA')

# Посилання, типу нахуй в сраку і т.д.

# Nahui ua
@dp.message_handler(text=['йди нахуй', 'иди нахуй'])
async def nahui_command(message: types.Message):
    if message.from_user.id == 1093113100:
        if message.reply_to_message:
            await message.reply_to_message.reply(f'повністю згідний, {message.reply_to_message.from_user.full_name} пішов нахуй!')
        else:
            await message.reply(f'я згідний з чо, йди нахуй!')
    else:
        await message.reply("сам(а) йди😉")

# v sraku
@dp.message_handler(text=['йди в сраку'])
async def vsraku_command(message: types.Message):
    await message.reply("Ротік будіш у стаматолага актрівать, заюшь🙄")

# 🙋
@dp.message_handler(text=['🙋'])
async def shos_command(message: types.Message):
    await message.reply_sticker('CAACAgIAAxkBAAICf2Nr7YBBXK5GTTjb0CLmrBTNtXHMAAJnCQACHxFhSlhrS2D5ieFkKwQ')

# 💔
@dp.message_handler(text=['💔'])
async def shos2_command(message: types.Message):
    await message.reply('Мой сладкій перчік діма діма євтушенка(ділдашенка)')

# dani
@dp.message_handler(text=['дані', 'Дані', 'ДаНі', '.дані', '!дані'])
async def dani_command(message: types.Message):
    dani_random = ['да', 'ні']
    await message.reply(f'я вибираю: {random.choice(dani_random)}')

# test
#@dp.message_handler(lambda text: text in ['пр', 'привіт', 'хеллоу', 'хай'])
#async def test_commands(message: types.Message):
#    await message.reply("прп")


# MUTE
@dp.message_handler(text=['заткнуть', 'мут', 'мовчи', 'молчи'], is_admin=True)
async def mute_command(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Команда використовується тільки в відповіді на повідомлення")
        return
    else:
        to_mute_time = int(time.mktime(message.date.timetuple())) + 900
        await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_id, until_date=to_mute_time, **config.MUTE_PREMISSION)
        await message.reply("Всьо, тепер мовчи 15 хвилин, подумай над своєю поведінкою")
    return

# gpdjj
@dp.message_handler(text=['Чо вернись\nдивись не споткнись\nв нас біда\nне вернешся — пізда'])
async def gpdjj(message: types.Message):
    await message.reply(f'Призиваю Чо!!')

    sleep(1)
    await bot.send_message(1093113100, f'{message.from_user.mention} ТЕБЕ ВИКЛИКАЄ В ФНР, Хватай монатки і піздуй туди! @FNRslava')