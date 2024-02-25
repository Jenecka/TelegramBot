import os
import asyncio
from aiogram import Bot, Dispatcher

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

from handlers.user_private import user_private_router
from docx_work.hndl_tit_list import hndl_tit_list_router

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

dp.include_router(user_private_router)
dp.include_router(hndl_tit_list_router)

async def main():
    await dp.start_polling(bot)
asyncio.run(main())