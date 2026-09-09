from aiogram import Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from keyboards.reply import ReplyKeyboards

class SurveyStates(StatesGroup):

    name = State()
    age = State()
    city = State()
    language = State()

def register_survey_handlers(dp: Dispatcher):

    @dp.message(Command("survey"))
    async def cmd_survey(message: Message, state: FSMContext):
        
        await message.answer(
            text="Как тебя зовут?\n",
            reply_markup=ReplyKeyboardRemove()
        )

        await state.set_state(SurveyStates.name)

    @dp.message(SurveyStates.name)
    async def process_name(message: Message, state: FSMContext):
        
        await state.update_data(name=message.text)

        await message.answer(text="Сколько лет?")
        await state.set_state(SurveyStates.age)

    @dp.message(SurveyStates.age)
    async def process_age(message: Message, state: FSMContext):
        
        if not message.text.isdigit():
            await message.answer(text="Введите число")
            return

        await state.update_data(age=int(message.text))

        await message.answer(text="В каком городе живёте?")
        await state.set_state(SurveyStates.city)

    @dp.message(SurveyStates.city)
    async def process_name(message: Message, state: FSMContext):
        
        await state.update_data(city=message.text)

        await message.answer(text="На каком языке говорите?")
        await state.set_state(SurveyStates.language)

    @dp.message(SurveyStates.language)
    async def process_name(message: Message, state: FSMContext):
        
        await state.update_data(language=message.text)

        data = await state.get_data()

        result_text = f"Опрос пройден.\nИмя: {data.get('name')}\nВозраст: {data.get('age')}\nГород: {data.get('city')}\nЯзык: {data.get('language')}\n"

        keyboard = ReplyKeyboards.main_menu()

        await message.answer(text=result_text, reply_markup=keyboard)

        await state.clear()

    @dp.message(Command("cancel"))
    async def cmd_cancel(message: Message, state: FSMContext):

        current_state = await state.get_state()

        if current_state is None:
            await message.answer(
                text="Отменять нечего, нет активных диалогов.",
                reply_markup=ReplyKeyboards.main_menu()
            )
            return

        await state.clear()
        await message.answer(text="Диалог отменён.", reply_markup=ReplyKeyboards.main_menu())
