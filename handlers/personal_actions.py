from time import sleep
from aiogram import types
from dispatcher import bot, dp
import config
from aiogram.dispatcher.filters import Text
import html
import random


# start
@dp.message_handler(commands=('start'), commands_prefix=('/!'))
async def start(message: types.Message):
    await message.answer("Хай, я Квард! Я допоможу тобі вбивати русню, робити біолабораторії, або просто банити і мутити людей\n\nДля того щоб взнати, що я вмію, напиши /help", parse_mode='HTML')
    print(f'{message.from_user.full_name}, {message.from_user.username},{message.from_user.id} Ha scritto Start')


# help
@dp.message_handler(commands=('help'), commands_prefix=('/!'))
async def help(message: types.Message):
    await message.answer("<b>Меню допомоги:</b>\n\nЦе бот модератор для чатів! Я вмію банити, мутити людей, а також вбивати русню, ставити міни, користуватись байрактаром, і інші дрібниці\n\n\n<b>Основні команди:</b>\n•<code>/start</code> - стартує цю штуку\n•<code>/help</code> - меню допомоги\n•<code>/info</code> - інформація\n\n<b>Команди адміністрування:</b>\n•<code>/mute</code> - забороняє людині писати на годину\n•<code>/unmute</code> - розмучує людину раніше години\n•<code>/ban</code> - блокує людину в чаті\n•<code>/unban</code> - розблоковує людину в чаті\n•<code>+санкции</code> - накладає санкції на людину\n\n---BETA---", parse_mode='HTML')

# info
@dp.message_handler(commands=('info'), commands_prefix=('/!'))
async def info(message: types.Message):
    await message.answer(f"<b>Інформація:</b>Це бот Квард, створенний одним українським нн-ом, якому стало скучно, і він вирішив без знань нічого написати свого бота в телеграмі. Бот перший раз запущений в якісь групі 31.10.2022. Також (надіюсь) він буде оновлюватись і далі, тому чекайте нових оновлень. А я йду попью чаю!😉\n\n<b>Сімейство Noki Family:</b>\n•Quard(@QuardNoki_bot) — Бот-модератор Квард, може помогти вам вбивати русню\n•Tech(@Tech_nokibot) — Технічна підтримка\n•StickerID(@asasda_bot) — Допоможе вам взнати ID стікеру\n•ToHTML(@ToHTML_nokibot) — Конвертує текст з телеграмного форматування, на HTML\n\n<b>Технічна інформація:</b>\nМова програмування:Python, Aiogram 2\nВерсія боту:0.09\n\n<b>Контакти і т.д.</b>\n•Наш канал: @NokiFamily\n•Посиділки з квардом: @quard_nokifamily\n•Тех. підтримка:@Tech_nokibot\n\n<b>Адміни і розробники:</b>\n•Головний розробник: @nnokito\n•Головний адмін: @jenniemie\n\n<i>Модераторів і адмінів поки немає, але в майбутньому <u>можливо</u> будуть</i>", parse_mode='HTML')

# Quard
@dp.message_handler(commands=('Квард', 'Quard', 'квард', 'quard'), commands_prefix=('/!'))
async def quard(message: types.Message):
    await message.answer(f"шо хоч?", parse_mode='HTML')

# QuardNoki_bot
@dp.message_handler(commands=('QuardNoki_bot'), commands_prefix=('/!.@'))
async def mention_quard(message: types.Message):
    await message.reply(f"шо?")

# Password Generator
@dp.message_handler(commands=('password'), commands_prefix=('/!.'))
async def pass_generator(message: types.Message):
    lenght = int(message.get_args())
    lower_case = "abcdefghijklmnopqrstuwxy"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUWXY"
    numbers = "0123456789"
    
    Use_for = lower_case + upper_case + numbers
    lenght_for_pass = lenght

    password = "".join(random.sample(Use_for, lenght_for_pass))
    await message.reply(f"Квард вибирає: {password}")

# Telegram to HTML
@dp.message_handler(commands=('html'))
async def to_html(message: types.Message):
    to_html = message.get_args()
    to_html = str(message.html_text)

    await message.answer(to_html, parse_mode='')
    
    await message.answer(f"<b>Ваш текст</b>:\n\n{message.html_text}", parse_mode="HTML")

# Database
#@dp.message_handler()
#async def mess_handler(message: types.Message):
#    if not db.user_exists(message.from_user.id):
#        db.add_user(message.from_user.id)
