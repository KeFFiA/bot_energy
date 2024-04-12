import logging
from datetime import datetime

from loguru import logger


class InterceptHandler(logging.Handler):
    LEVELS_MAP = {
        logging.CRITICAL: "CRITICAL",
        logging.ERROR: "ERROR",
        logging.WARNING: "WARNING",
        logging.INFO: "INFO",
        logging.DEBUG: "DEBUG",
    }

    def _get_level(self, record):
        return self.LEVELS_MAP.get(record.levelno, record.levelno)

    def emit(self, record):
        logger_opt = logger.opt(depth=8, exception=record.exc_info)
        logger_opt.log(self._get_level(record), record.getMessage())


async def setup():
    date = datetime.now().strftime("%m-%d-%y")
    logging.basicConfig(handlers=[InterceptHandler()], level=logging.INFO)
    logger.add(f'logs/logs_{date}.log', level='INFO', rotation='00:00', compression='zip')
    logger.add(f'logs/logs.log', level='INFO', mode='w')
