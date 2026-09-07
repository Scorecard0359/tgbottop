import os
from dotenv import load_dotenv

class BotConfig:

    _token = None

    @classmethod
    def load(cls):

        load_dotenv()

        cls._token = os.getenv("BOT_TOKEN")

        if not cls._token:
            raise ValueError(
                "Токен бота не найден!"
            )

    @classmethod
    def get_token(cls):
        return cls._token


BotConfig.load()