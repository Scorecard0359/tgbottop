import asyncio, logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile

from config import BotConfig
from handlers import register_all_handlers
from middlewares.logging import LoggingMiddleware
from middlewares.auth import AdminMiddleware
from middlewares.logfile import LogFileMiddleware
from middlewares.counter import UserCounterMiddleware
from database.db import Database

class TelegramBot:

    def __init__(self):

        logging.basicConfig(level=logging.INFO)

        self.token = BotConfig.get_token()

        self.bot = Bot(token=self.token)

        self.dp = Dispatcher()

        # self._setup_middlewares()

        register_all_handlers(self.dp)

        logging.info("Бот инициализирован.")

    def _setup_middlewares(self):
        pass

        # self.dp.update.outer_middleware(LoggingMiddleware())

        # self.dp.update.outer_middleware(LogFileMiddleware())

        # self.dp.update.outer_middleware(UserCounterMiddleware())

        # * self.dp.update.outer_middleware(AdminMiddleware())

    async def start(self):

        await Database.init()

        bot_info = await self.bot.me()

        print("Бот запущен.", bot_info.first_name, bot_info.username, bot_info.id)

        await self.dp.start_polling(self.bot, skip_updates=True)

async def main():

    bot = TelegramBot()

    await bot.start()

if __name__ == "__main__":
    asyncio.run(main())
