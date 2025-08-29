from aiogram import Bot,Dispatcher
from dotenv import load_dotenv
from os import getenv
import asyncio
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from db import get_from_table

load_dotenv()
token = getenv('token')
dp = Dispatcher()

channel_id = getenv("CHANNEL_ID")


async def main():
    bot = Bot(token,default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await get_from_table(bot,parse=ParseMode.HTML,channel_id=channel_id)
    await bot.session.close()


asyncio.run(main())
