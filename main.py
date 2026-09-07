import asyncio, logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile

from config import BotConfig
from handlers import register_all_handlers

class TelegramBot:

    def __init__(self):

        logging.basicConfig(level=logging.INFO)

        self.token = BotConfig.get_token()

        self.bot = Bot(token=self.token)

        self.dp = Dispatcher()

        register_all_handlers(self.dp)

        logging.info("Бот инициализирован.")

    async def start(self):

        bot_info = await self.bot.me()

        print(bot_info.first_name, bot_info.username, bot_info.id)

        await self.dp.start_polling(self.bot, skip_updates=True)

async def main():

    bot = TelegramBot()

    await bot.start()

if __name__ == "__main__":
    asyncio.run(main())
