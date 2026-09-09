import os

from aiogram import Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile

from keyboards.reply import ReplyKeyboards

def register_photo_handlers(dp: Dispatcher):

    @dp.message(Command("photo"))
    async def cmd_photo(message: Message):

        keyboard = ReplyKeyboards.photo_menu()

        photo_path = os.path.join("core/img", "beer.png")

        if not os.path.exists(photo_path):
            await message.answer("👻")

            return

        photo = FSInputFile(photo_path)

        await message.answer_photo(
            photo=photo,
            reply_markup=keyboard
        )

    @dp.message(F.text == "Фото")
    async def handle_photo_button(message: Message):

        keyboard = ReplyKeyboards.photo_menu()

        photo_path = os.path.join("core/img", "beer.png")

        if not os.path.exists(photo_path):
            await message.answer("👻")

            return

        photo = FSInputFile(photo_path)

        await message.answer_photo(
            photo=photo,
            reply_markup=keyboard
        )
