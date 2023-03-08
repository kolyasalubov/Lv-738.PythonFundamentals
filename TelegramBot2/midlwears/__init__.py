from aiogram import Dispatcher
from .throttling import ThrottlingMiddleware


def setup(tb:Dispatcher):
    tb.middleware.setup(ThrottlingMiddleware())