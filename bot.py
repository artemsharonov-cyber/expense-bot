import os
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiohttp import web

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# --- Бот команды ---
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Привет! Я бот для учета расходов 💰")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(f"Ты написал: {message.text}")

# --- Web server для Render ---
async def handle(request):
    return web.Response(text="Бот работает ✅")

async def start_web_app():
    app = web.Application()
    app.router.add_get("/", handle)
    port = int(os.environ.get("PORT", 10000))  # Render выдаёт PORT
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

# --- Запуск и бота, и веб-сервера ---
async def main():
    await start_web_app()
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())
