from aiogram import Bot, types,Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data import config
from utils.tb_api.tb_yura import db


bot = Bot(token="5922482735:AAEYOC_ohtA5TG8kYQkp9nP6WJ3nfib4-a4",parse_mode=types.ParseMode.HTML)


storage = MemoryStorage()


tb = Dispatcher(bot,storage = storage)


__all__ = ['bot','storage','tb','db']