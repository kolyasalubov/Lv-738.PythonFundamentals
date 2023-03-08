import logging

from aiogram import Dispatcher
from data.config import admins_id

async def on_startap_notify(tb:Dispatcher):
    for admin in admins_id:
        try:
            text = "Bot started"
            tb.bot.send_message(chat_id = admin,text = text)
        except Exception as err:
            logging.exception(err) 