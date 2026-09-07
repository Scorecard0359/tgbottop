import asyncio, logging, os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("⭐️")

@dp.message(Command("beer"))
async def cmd_beer(message: Message):
    # await message.answer("придётся подождать")

    photo_path = "img/beer.png"

    photo = FSInputFile(photo_path)

    await message.answer_photo(
        photo=photo
    )

async def main():
    await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__":
    asyncio.run(main())
