import logging
import time
from typing import Callable, Dict, Any, Awaitable

from aiogram.types import Message, CallbackQuery, TelegramObject
from aiogram import BaseMiddleware

LOG_FORMATTER = "%(asctime)s | %(name)s | %(levelname)s | %(message)s"

logger = logging.getLogger(__name__)

logger_con = logging.StreamHandler()
logger_fil = logging.FileHandler(f"bot.log", encoding="UTF-8")
logger_con.setFormatter(logging.Formatter(LOG_FORMATTER))
logger_fil.setFormatter(logging.Formatter(LOG_FORMATTER))

logger.addHandler(logger_con)
logger.addHandler(logger_fil)

class LoggingMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable([TelegramObject, Dict[str, Any], Awaitable[Any]]),
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:

        user = data.get("event_from_user")
        user_info = f"{user.id} @{user.username}"   

        if isinstance(event, Message):
            event_type = "Сообщения"
            content = event.text or "<без текста>"
        elif isinstance(event, CallbackQuery):
            event_type = "callback"
            content = event.data
        else:
            event_type = "Другое"
            content = "-"

        logger.info(f"[{event_type}] {user_info}: {content}")

        start = time.time()

        try:
            result = await handler(event, data)
            el = time.time() - start

            logger.info(f"Обработано за {el:.3f} сек")

            return result
        except Exception:
            el = time.time() - start
            logger.error(f"Ошибка за {el:.3f} сек: {er}")
            raise
