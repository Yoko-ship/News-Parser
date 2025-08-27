import logging
from aiogram import Bot,Dispatcher,html
from dotenv import load_dotenv
from os import getenv
import asyncio
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from db import get_from_table

load_dotenv()
token = getenv('token')
print(token)
dp = Dispatcher()

@dp.message(CommandStart())
async def send_welcome(message:Message):
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@dp.message()
async def get_data_from_table(message:Message):
    data = get_from_table()
    title = data[0]['title']
    description = data[0]["description"]
    image = data[0]['image']
    caption = f"<b>{title}</b>\n\n{description}"
    await message.answer_photo(
        photo=image,caption=caption,parse_mode="HTML"
    )
    

async def main():
    bot = Bot(token,default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

# @dp.message_handler()
# async def echo(message: Message):
#     await message.answer(message.text)


asyncio.run(main())