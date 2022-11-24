import logging
from time import sleep
from aiogram import types
from dispatcher import dp, bot
import config
import re
import time

# pin
@dp.message_handler(commands=('pin', 'пін', 'пин'), commands_prefix=('/!.+'), is_admin=True)
async def cmd_pin(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Команду в відповідь на повідомлення використовуй")
    else:
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
        await message.reply_sticker('CAACAgEAAxkBAAICm2Nuii75kj8lWJsnDwn9Zz4hXMP_AALeAQACidP5RuKBWF2wUX8HKwQ')


# unpin
@dp.message_handler(commands=('unpin', 'унпін', 'унпин', 'пін', 'пин'), commands_prefix=('/!.-'), is_admin=True)
async def cmd_unpin(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Команду в відповідь на повідомлення використовуй")
    else:
        await bot.unpin_chat_message(message.chat.id, message.reply_to_message.message_id)
        await message.reply_sticker('CAACAgEAAxkBAAICm2Nuii75kj8lWJsnDwn9Zz4hXMP_AALeAQACidP5RuKBWF2wUX8HKwQ')

# mute
@dp.message_handler(commands=('mute', 'заткнуть', 'мут', 'мовчи', 'молчи'), commands_prefix=('/!.'), is_admin=True)
async def cmd_mute(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Команда використовується тільки в відповіді на повідомлення")
        return
    else:
        to_mute_time = int(message.get_args())
        to_mute_time = int(time.mktime(message.date.timetuple())) + to_mute_time
        await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_id, until_date=to_mute_time, **config.MUTE_PREMISSION)
        await message.reply(f"тіпєрь малчі {to_mute_time} сікунд, квасік підарасік! ")
    return

# sanctions
@dp.message_handler(commands=('Санкции', 'санкции'), commands_prefix=('/!.+'), is_admin=True)
async def cmd_sanctions(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Команда використовується тільки в відповіді на повідомлення")
        return
    else:
        to_mute_time = int(time.mktime(message.date.timetuple())) + 1
        await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_id, until_date=to_mute_time, **config.SANCTION_PREMISSION)
        await message.reply("Санкції наложені, для зняття санкцій напишіть /unmute")
    return

# unmute
@dp.message_handler(commands=('unmute', 'parla'), commands_prefix=('/!.'), is_admin=True)
async def cmd_unmute(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Команда використовується тільки в відповіді на повідомлення")
        return
    else:
        await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_id, **config.UNMUTE_PREMISSION)
        await message.reply("Ви витянули кляп з рота користувача!")
    return

# ban
@dp.message_handler(commands=('ban'), commands_prefix=('/!.'), is_admin=True)
async def cmd_ban(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Команда використовується тільки в відповіді на повідомлення")
        return
    else:
        await bot.ban_chat_member(message.chat.id, message.reply_to_message.from_id)
        await message.reply("Урааа, ми ізбавились від цієї повії🥳")
    return

# unban
@dp.message_handler(commands=('unban'), commands_prefix=('/!.'), is_admin=True)
async def cmd_unban(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Команда використовується тільки в відповіді на повідомлення")
        return
    else:
        await bot.unban_chat_member(message.chat.id, message.reply_to_message.from_id)
        await message.reply("Воно повертається, вітаємо лєгєнду!(або ні)")
    return

@dp.message_handler(commands=('mute', 'заткнуть', 'мут', 'мовчи', 'молчи', 'unmute', 'parla', 'ban', 'unban'), commands_prefix=('/!'), chat_type=('supergroup', 'group')) #, is_admin=True
async def cmd_unban(message: types.Message):
    await message.reply("Ноу ноу ноу, ти не адмін!")

