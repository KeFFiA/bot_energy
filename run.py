import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from bot.logging_settings import setup, logger
from database import get_connection
from bot.config_data import api_token
from bot.handlers.user_handlers import router


async def main():
    await setup()
    logger.info('Start initialization...')
    bot = Bot(token=api_token, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    logger.info('Initialization complete.')


if __name__ == "__main__":
    username = input('Username: ')
    password = input('Password: ')
    if get_connection(username=username, password=password) is True:
        asyncio.run(main())
    else:
        logger.critical('Username/password is incorrect. ACCESS DENIED')
