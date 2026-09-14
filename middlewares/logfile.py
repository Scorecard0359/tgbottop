import logging
import time
from typing import Callable, Dict, Any, Awaitable

from aiogram.types import Message, CallbackQuery, TelegramObject
from aiogram import BaseMiddleware

logger = logging.getLogger(__name__)
file = logging.FileHandler(filename="bot.log")
logger.addHandler(file)

class LogFileMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable([TelegramObject, Dict[str, Any], Awaitable[Any]]),
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:

        user = event.message.from_user

        user_id = user.id if user else "unknown"

        date_time = time.strftime("%d %b %Y %H:%M:%S", time.gmtime())

        logger.info(f"{date_time}, ID {user_id}: {event.message.text}")

        return await handler(event, data)
