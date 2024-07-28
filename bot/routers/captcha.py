from aiogram import types, Router, F
from aiogram.types import ChatPermissions

from bot.service.redis_serv.user import get_answer, get_tries, inсr_tries

from asyncio import sleep


router = Router()


@router.callback_query(F.data.startswith("fruit_"))
async def check_captcha(callback: types.CallbackQuery):

    right_answer = await get_answer(user_id=callback.from_user.id)

    user_answer = callback.data

    if right_answer == user_answer:

        await callback.message.delete()

        # text = f"""<a href='https://t.me/{callback.from_user.username}'>{callback.from_user.first_name}</a>, напишите администраторам для доступа к отправке сообщений."""
        #
        # mes = await callback.message.answer(
        #     text=text
        # )
        await callback.bot.restrict_chat_member(
            chat_id=callback.message.chat.id,
            user_id=callback.from_user.id,
            permissions=ChatPermissions(can_send_messages=True,
                                        can_send_voice_notes=True),
        )
        # await sleep(60)
        # try:
        #     await mes.delete()
        # except:
        #     pass
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
