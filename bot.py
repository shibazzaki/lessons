import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command



logging.basicConfig(level=logging.INFO)
bot = Bot(token="7037127414:AAFPTG7YZjquoYiqY6gTv1Ez2krZquEjelU") #token would be here

dp = Dispatcher()


#handler command start
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Hello!!!HI!!!! my sweat Stepovyata")


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())


