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
