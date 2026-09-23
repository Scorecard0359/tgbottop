from aiogram import Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

def register_others_handlers(dp: Dispatcher):

    @dp.message(Command("test_error"))
    async def cmd_test_error(message: Message, command: Command.CommandObj):
        if command.args is not None:
            if command.args == "1":
                result = 1 / 0
                await message.answer(result)
            elif command.args == "2":
                sl = {}
                await message.answer(sl["starling"])
            elif command.args == "3":
                sl = []
                await message.answer(sl[1])

    @dp.message(F.text)
    async def handle_other_button(message: Message):

        if "тест" in message.text.lower():
            await message.answer("ну вроде работаю")
        else:
            await message.answer("Используйте меню!")
