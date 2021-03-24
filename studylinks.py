#!venv/bin/python
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.exceptions import BotBlocked
from aiogram.dispatcher.filters import Text
import asyncio
import random as rand



bot = Bot(token="1555033388:AAEbf1sTNZdp-JuhhiKFmOjE_4bLkKHLEks")

dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)




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







if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
