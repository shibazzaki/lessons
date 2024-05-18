import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import Message

# Налаштування логування
logging.basicConfig(level=logging.INFO)

# Ініціалізація бота та диспетчера
bot = Bot(token=str('7039214828:AAFoqoPafd-4s41jpbVCcciCxkRrij8SIZw'))
dp = Dispatcher()
ADMIN_ID = 661267467

# Словник для зберігання фільмів (в реальному застосунку краще використовувати базу даних)
movies = {}

# Обробник команди /start
@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "Вітаю! Я бот для пошуку фільмів.\n"
        "Адміністратор може додати фільми за допомогою команди /add.\n"
        "Щоб знайти фільм, введіть його код."
    )

# Обробник команди /add (тільки для адміністратора)
@dp.message(Command("add"), F.from_user.id == ADMIN_ID)
async def cmd_add(message: Message, command: CommandObject):
    global movies
    args = command.args.split()  # Отримуємо аргументи з CommandObject
    if len(args) != 2:
        await message.answer("Неправильний формат. Використовуйте: /add <код> <назва фільму>")
        return

    code, movie_name = args
    movies[code] = movie_name
    await message.answer(f"Фільм '{movie_name}' додано з кодом '{code}'.")


# Обробник пошуку фільму за кодом
@dp.message()
async def get_movie(message: Message):
    code = message.text
    if code in movies:
        await message.answer(f"Назва фільму: {movies[code]}")
    else:
        await message.answer("Фільм з таким кодом не знайдено.")

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
