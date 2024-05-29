from aiogram import Dispatcher

from bot.routers import captcha
from bot.routers import join_group


def register_all_routers(dp: Dispatcher):

    dp.include_router(join_group.router)
    dp.include_router(captcha.router)