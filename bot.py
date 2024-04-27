import asyncio
import logging
import colorama
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from datetime import datetime
from config_reader import config


logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()

dp["started_at"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

async def on_startup(dp: Dispatcher):
    await dp.start_polling(bot, mylist=[1, 2, 3])


#handler command start
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Hello!!!HI!!!! my sweat Stepovyata")


@dp.message(Command("help"))
async def cmd_reply(message: types.Message):
    await message.reply("What do u need?")

@dp.message(Command("dice"))
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🎲")


@dp.message(Command("info"))
async def cmd_info(message: types.Message, started_at: str):
    await message.answer(f"Бот запущений {started_at}")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())




