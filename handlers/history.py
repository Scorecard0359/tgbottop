from aiogram import Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from database.db import Database

def register_history_handlers(dp: Dispatcher):

    @dp.message(Command("history"))
    async def cmd_history(message: Message):

        user_id = message.from_user.id
        surveys = await Database.get_user_surveys(user_id)

        if not surveys:
            await message.answer(
                "У вас нет опросов\n"
                "Введи /history, чтобы1 начать опрос."
            )
            return

        text = f"Твоя история опросов (всего опросов: {len(surveys)})\n\n"

        for i, survey in enumerate(surveys, start=1):
            name, age, city, language, created_at = survey
            text += (
                f"{i}, {created_at}\n"
                f"{name}, {age} лет, {city}\n"
                f"Любимый язык: {language}"
            )
            await message.answer(text)

    @dp.message(Command("stats"))
    async def cmd_stats(message: Message):

        stats = await Database.get_stats()

        if not stats:
            await message.answer(
                "Никто не отправлял опросы.\n"
                "Введи /history, чтобы1 начать опрос."
            )
            return

        user_count, survey_count, survey_age = stats
        await message.answer(f"Статистика бота: пользователей — {user_count}, опросов — {survey_count}, средний возраст — {survey_age}")
