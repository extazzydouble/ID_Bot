import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from handlers.setup_routers import setup_routers
from config.config import logger, TOKEN



async def on_shutdown(dispatcher: Dispatcher, bot: Bot):
    logger.info("Stopping polling and closing bot session...")
    await bot.session.close()
    logger.info("Bot stopped.")
            
async def main():

    if not TOKEN:
        raise ValueError("TOKEN environment variable not set. Please create a .env file with TOKEN=YOUR_BOT_TOKEN")

    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.shutdown.register(on_shutdown)
    setup_routers(dp)
    
    await dp.start_polling(bot)

    

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot stopped by user.")
