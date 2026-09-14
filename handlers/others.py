from aiogram import Dispatcher, F
from aiogram.types import Message

def register_others_handlers(dp: Dispatcher):

    @dp.message(F.text)
    async def handle_other_button(message: Message):

        if "тест" in message.text.lower():
            await message.answer("ну вроде работаю")
        else:
            await message.answer("Используйте меню!")
