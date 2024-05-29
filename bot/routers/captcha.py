from aiogram import types, Router, F
from aiogram.types import ChatPermissions

from bot.service.redis_serv.user import get_answer, get_tries, inсr_tries


router = Router()


@router.callback_query(F.data.startswith("fruit_"))
async def check_captha(callback: types.CallbackQuery):

    right_answer = await get_answer(user_id=callback.from_user.id)

    user_answer = callback.data

    if right_answer == user_answer:

        await callback.message.delete()
        await callback.bot.restrict_chat_member(
            chat_id=callback.message.chat.id,
            user_id=callback.from_user.id,
            permissions=ChatPermissions(can_send_messages=True)
        )
        await callback.message.answer(
            text=f"<a href='https://t.me/{callback.from_user.username}'>{callback.from_user.first_name}</a>, "
                 f"добро пожаловать."
        )
    else:

        await inсr_tries(user_id=callback.from_user.id)
        tries = int(await get_tries(user_id=callback.from_user.id))
        if tries > 2:
            await callback.bot.ban_chat_member(
                chat_id=callback.message.chat.id,
                user_id=callback.from_user.id
            )
        else:
            await callback.answer("Неправильный ответ", show_alert=True)