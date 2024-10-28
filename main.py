import asyncio
import logging
from distutils.command.config import config

from venv import logger

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers.other import other_router
from handlers.user import user_router
from middlewares.inner import (
    FirstInnerMiddleware,
    SecondInnerMiddleware,
    ThirdInnerMiddleware,
)
from middlewares.outer import (
    FirstOuterMiddleware,
    SecondOuterMiddleware,
    ThirdOuterMiddleware,
)

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] #%(levelname)-8s %(filename)s:'
           '%(lineno)d - %(name)s - %(message)s'
)

logger = logging.getLogger(__name__)


async def main() -> None:
    config: Config = load_config()
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    dp.include_router(user_router)
    dp.include_router(other_router)

    await dp.start_polling(bot)


asyncio.run(main())