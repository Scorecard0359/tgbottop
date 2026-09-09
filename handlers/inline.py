from aiogram import Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext

from keyboards.reply import ReplyKeyboards
from keyboards.inline import InlineKeyboards

# from .survey import cmd_survey

def register_inline_handlers(dp: Dispatcher):

    @dp.message(Command("menu"))
    async def cmd_menu(message: Message):

        keyboard = InlineKeyboards.main_menu()

        await message.answer(
            "Меню бота:\n",
            "Выберите действие.",
            reply_markup=keyboard
        )

    @dp.callback_query()
    async def handle_callback(callback: CallbackQuery, state: FSMContext):

        await callback.answer()

        data = callback.data

        if data == "info":
            await callback.message.edit_text(
                "Информация о боте:\n"
                "Первый нормальный бот"
            )
        elif data == "survey":
            await callback.message.delete()
            # await cmd_survey(callback.message, state)
            await callback.message.answer("Отправьте /survey")
        elif data == "photo":
            await callback.message.delete()
            await callback.message.answer("Фото отправляется")

            photo = FSInputFile("core/img/beer.png")
            await callback.message.answer_photo(
                photo=photo
            )
        elif data == "close":
            await callback.message.delete()
            await callback.message.answer("Меню закрыто.", reply_markup=ReplyKeyboards.main_menu())
