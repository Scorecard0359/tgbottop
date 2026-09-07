from aiogram import Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.reply import ReplyKeyboards

def register_start_handlers(dp: Dispatcher):

    @dp.message(Command("start"))
    async def cmd_start(message: Message):

        keyboard = ReplyKeyboards.main_menu()

        await message.answer("⭐️", reply_markup=keyboard)

    @dp.message(F.text == "Старт")
    async def handle_start_button(message: Message):

        keyboard = ReplyKeyboards.main_menu()

        await message.answer("⭐️", reply_markup=keyboard)

    @dp.message(F.text == "Помощь")
    async def handle_help_button(message: Message):

        await message.answer("❓")

    @dp.message(F.text == "Помощь")
    async def handle_other_button(message: Message):

        if "тест" in message.text.lower():
            await message.answer("ну вроде работаю")
        else:
            await message.answer("⭐️")

def register_beer_handlers(dp: Dispatcher):

    @dp.message(Command("beer"))
    async def cmd_beer(message: Message):

        keyboard = ReplyKeyboards.beer_menu()

        photo_path = "core/img/beer.png"

        photo = FSInputFile(photo_path)

        await message.answer_photo(
            photo=photo,
            reply_markup=keyboard
        )

    @dp.message(F.text == "Пиво")
    async def handle_beer_button(message: Message):

        keyboard = ReplyKeyboards.beer_menu()

        photo_path = "core/img/beer.png"

        photo = FSInputFile(photo_path)

        await message.answer_photo(
            photo=photo,
            reply_markup=keyboard
        )
