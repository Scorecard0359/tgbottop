import logging
import time
from typing import Callable, Dict, Any, Awaitable

from aiogram.types import Message, CallbackQuery, TelegramObject
from aiogram import BaseMiddleware

logger = logging.getLogger(__name__)

class LoggingMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable([TelegramObject, Dict[str, Any], Awaitable[Any]]),
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:

        user = event.message.from_user

        user_info = f"{user.id} (@{user.username})" if user else "Неизвестный пользователь"
        logger.info(f"Входящее событие от {user_info}")

        start = time.time()

        result = await handler(event, data)

        time_result = time.time() - start
        logger.info(f"Обработано за {time_result:.2f} сек")

        return result
