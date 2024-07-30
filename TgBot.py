import os
import asyncio
from aiogram import Bot, Dispatcher

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

ALLOWED_UPDATES = ['message, edited_message']
from handlers.user_private import user_private_router
from docx_work.hndl_tit_list import hndl_tit_list_router
from docx_work.spis_litrature import hndl_spis_literature_router

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

dp.include_router(user_private_router)
dp.include_router(hndl_tit_list_router)
dp.include_router(hndl_spis_literature_router)


async def main():
    await dp.start_polling(bot, allowed_updates=[])


asyncio.run(main())
