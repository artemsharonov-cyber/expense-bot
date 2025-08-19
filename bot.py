import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("BOT_TOKEN")  # токен возьмем из Render
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Команда /start
@dp.message_handler(commands=["start"])
async def start(msg: types.Message):
    await msg.answer("Привет! Я бот для учёта расходов. Напиши сумму и категорию, например: 500 еда")

# Приём сообщений с суммой и категорией
@dp.message_handler()
async def add_expense(msg: types.Message):
    try:
        parts = msg.text.split()
        amount = float(parts[0])
        category = " ".join(parts[1:]) if len(parts) > 1 else "без категории"
        await msg.answer(f"✅ Записано: {amount} руб. в категорию '{category}'")
        # Пока сохраняем только в памяти, позже подключим базу
    except Exception:
        await msg.answer("⚠️ Введи данные правильно: пример — '500 еда'")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
