import os
import asyncio
from aiogram import Bot, Dispatcher, types

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

from handlers.user_private import user_private_router
#импортирован обьект класса роутер из файла user_private

bot = Bot(token = os.getenv('TOKEN'))
dp = Dispatcher()

dp.include_router(user_private_router)


async def main():
    await dp.start_polling(bot)
asyncio.run(main())