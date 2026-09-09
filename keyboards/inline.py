from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class InlineKeyboards:

    @staticmethod
    def main_menu() -> InlineKeyboardMarkup:

        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton (
                        text="Информация",
                        callback_data="info"
                    ),
                    InlineKeyboardButton (
                        text="Фото",
                        callback_data="photo"
                    )
                ],
                [
                InlineKeyboardButton (
                        text="Опрос",
                        callback_data="survey"
                    ),
                    InlineKeyboardButton (
                        text="Закрыть",
                        callback_data="close"
                    ) 
                ]
            ]
        )

        return keyboard
