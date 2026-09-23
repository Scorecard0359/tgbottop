import logging
import traceback
from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery, TelegramObject

LOG_FORMATTER = "%(asctime)s | %(name)s | %(levelname)s | %(message)s"

logger = logging.getLogger(__name__)

logger_con = logging.StreamHandler()
logger_fil = logging.FileHandler(f"bot.log", encoding="UTF-8")
logger_con.setFormatter(logging.Formatter(LOG_FORMATTER))
logger_fil.setFormatter(logging.Formatter(LOG_FORMATTER))

logger.addHandler(logger_con)
logger.addHandler(logger_fil)

class ErrorMiddleware(BaseMiddleware):

    def __init__(self, admin_id: int):
        super().__init__()
        self.admin_id = admin_id

    async def __call__(
        self,
        handler: Callable([TelegramObject, Dict[str, Any], Awaitable[Any]]),
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        try:
            return await handler(event, data)
        except Exception as er:

            logger.error(f"Ошибка: {er}")
            logger.error(traceback.format_exc())

            bot = data.get("bot")

            if bot and self.admin_id:
                try:
                    await bot.send_message(
                        chat_id=self.admin_id,
                        text=f"Ошибка в боте\n\n{type(er).__name__}: {er}"
                    )
                except Exception:
                    pass

            if isinstance(event, Message):
                await event.answer("Что-то пошло не так. Попробуйте позже.")
            elif isinstance(event, CallbackQuery):
                await event.answer("Что-то пошло не так. Попробуйте позже.", show_alert=True)
