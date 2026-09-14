from typing import Callable, Dict, Any, Awaitable

from aiogram.types import Message, CallbackQuery, TelegramObject
from aiogram import BaseMiddleware

class UserCounterMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable([TelegramObject, Dict[str, Any], Awaitable[Any]]),
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:

        user = event.message.from_user

        if user is None:
            return await handler(event, data)

        # ...

        return await handler(event, data)
