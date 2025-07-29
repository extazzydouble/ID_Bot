from aiogram import Dispatcher
from handlers.common.common_router import common_router

def setup_routers(dp: Dispatcher):
    dp.include_router(common_router)