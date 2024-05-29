from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

from bot.settings import settings

def captcha_key(fruits):

    builder = InlineKeyboardBuilder()
    for index, fruit in enumerate(fruits):

        if index % 3 == 0:

            builder.row(
                InlineKeyboardButton(
                    text=fruit, callback_data=settings.FRUITS[fruit]
                )
            )

        else:

            builder.button(text=fruit, callback_data=settings.FRUITS[fruit])

    return builder.as_markup()