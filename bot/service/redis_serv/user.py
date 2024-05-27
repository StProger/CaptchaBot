from bot.service.redis_serv.base import redis_pool


async def set_msg_to_delete(user_id: int, message_id: int) -> None:
    """ Установка сообщения на удаление (пользователю) """
    await redis_pool.set(f"{user_id}:msg:id", message_id)


async def get_msg_to_delete(user_id: int) -> int:
    """ Получение сообщения, которое надо удалить у пользователя """
    return await redis_pool.get(f"{user_id}:msg:id")


async def inсr_tries(user_id: int) -> None:

    await redis_pool.incr(f"{user_id}:tries")


async def get_tries(user_id: int) -> int:

    return await redis_pool.get(f"{user_id}:tries")