from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

class ReplyKeyboards:

    @staticmethod
    def main_menu():

        btn_start = KeyboardButton(text="Старт")
        btn_beer = KeyboardButton(text="Пиво")
        btn_help = KeyboardButton(text="Помощь")

        keyboard = ReplyKeyboardMarkup(
            keyboard=([btn_start, btn_beer], [btn_help]),
            resize_keyboard=True,
            one_time_keyboard=False
        )

        return keyboard

    @staticmethod
    def beer_menu():

        btn_beer = KeyboardButton(text="Пиво")
        btn_back = KeyboardButton(text="Назад")

        keyboard = ReplyKeyboardMarkup(
            keyboard=([btn_beer], [btn_back]),
            resize_keyboard=True,
            one_time_keyboard=False
        )

        return keyboard

    @staticmethod
    def remove():
        return ReplyKeyboardRemove()
