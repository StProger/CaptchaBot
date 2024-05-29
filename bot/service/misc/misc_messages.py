from aiogram import types

import random

from aiogram.types import ChatPermissions

from bot.settings import settings

from bot.service.redis_serv.user import set_tries, set_answer
from bot.keyboards.inline import captcha_key


async def event_join_group(event: types.ChatMemberUpdated):

    fruits = list(settings.FRUITS.copy().keys())
    random.shuffle(fruits)

    fruit = random.choice(fruits)

    answer = settings.FRUITS[fruit]

    await set_tries(user_id=event.from_user.id)
    await set_answer(user_id=event.from_user.id, answer=answer)
    await event.bot.restrict_chat_member(chat_id=event.chat.id,
                                         user_id=event.from_user.id,
                                         permissions=ChatPermissions())

    text = f"""<a href='https://t.me/{event.from_user.username}'>{event.from_user.first_name}</a>, нажми на {fruit}."""

    await event.answer(
        text=text,
        reply_markup=captcha_key(fruits=fruits)
    )


