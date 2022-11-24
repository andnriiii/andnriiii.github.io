import logging
from logging.handlers import TimedRotatingFileHandler
from aiogram import executor
from dispatcher import dp
import handlers
import config

async def on_startup(_):
    print('Бот запущений успішно✅')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)