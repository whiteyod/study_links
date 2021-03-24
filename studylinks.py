#!venv/bin/python
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.exceptions import BotBlocked
from aiogram.dispatcher.filters import Text
import asyncio
import random as rand


# Объект бота
bot = Bot(token="1555033388:AAEbf1sTNZdp-JuhhiKFmOjE_4bLkKHLEks")
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)




@dp.errors_handler(exception=BotBlocked)
async def error_bot_blocked(update: types.Update, exception: BotBlocked):
    # Update: объект события от Telegram. Exception: объект исключения
    # Здесь можно как-то обработать блокировку, например, удалить пользователя из БД
    print(f"Меня заблокировал пользователь!\nСообщение: {update}\nОшибка: {exception}")

    # Такой хэндлер должен всегда возвращать True,
    # если дальнейшая обработка не требуется.
    return True




@dp.message_handler(commands="start")
async def cmd_inline_url(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="GameDev от ХАМК", url="https://cambridge-academy-of-gaming-and-innovation.teachable.com/"),
        types.InlineKeyboardButton(text="Гайд по ботам(groosha)", url="https://mastergroosha.github.io/telegram-tutorial-2/"),
        types.InlineKeyboardButton(text="Слайды от Девмана", url="https://slides.dvmn.org/"),
        types.InlineKeyboardButton(text="Уроки devpractice", url="https://devpractice.ru/python-lessons/")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Учение-хуение", reply_markup=keyboard)



@dp.message_handler(commands="random")
async def cmd_random(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Нажми меня", callback_data="random_value"))
    await message.answer("Нажмите на кнопку, чтобы бот отправил число от 1 до 10", reply_markup=keyboard)





if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)