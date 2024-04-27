import asyncio
import logging
import colorama
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from datetime import datetime
from config_reader import config
from aiogram import F
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram import html
from aiogram.utils.formatting import Text, Bold, Italic, Underline
logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.bot_token.get_secret_value(), parse_mode="HTML")
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

@dp.message(F.text)
async def echo_with_time(message: types.Message):
    time_now = datetime.now().strftime("%H:%M:%S")
    added_text = html.underline(f"Created in {time_now}")
    await message.answer(f"{message.html_text}\n{added_text}", parse_mode="HTML")



@dp.message(F.text, Command("test"))
async def any_message(message: Message):
    await message.answer(
        "Це повідомлення з <u>ХТМЛ розміткою</u>"
    )
    await message.answer(
        "Hello, *world*\!",
        parse_mode=ParseMode.MARKDOWN_V2
    )


@dp.message(Command("hello"))
async def cmd_hello(message: types.Message):
    content = Text(
        "Hello, ",
        Bold(message.from_user.full_name)
    )
    await message.answer(
        **content.as_kwargs()

    )

@dp.message(Command("info"))
async def cmd_info(message: types.Message, started_at: str):
    await message.answer(f"Бот запущений {started_at}")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())




