from aiogram import Bot,Dispatcher
from dotenv import load_dotenv
from os import getenv
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from db import get_from_table
from fastapi import FastAPI
from aiogram.types import Update

load_dotenv()
token = getenv('token')
app = FastAPI()
bot = Bot(token,default=DefaultBotProperties(parse_mode=ParseMode.HTML))


dp = Dispatcher()
channel_id = getenv("CHANNEL_ID")



async def run_bot_task():
    await get_from_table(bot,parse=ParseMode.HTML,channel_id=channel_id)
    await bot.session.close()

@app.get("/")
def home():
    return {"status":"Сервер работает успешно"}


@app.get("/run-task")
async def run_task():
    # try:
        await run_bot_task()
        return {"status":"Task executed"}
    # except Exception as e:
    #     return {"status":e}





