from cgitb import text
from loader import tb
from aiogram.dispatcher.filters import Command
from aiogram import types
from keyboard.default import kb_menu

 

@tb.message_handler(text = "/menu")
async def menu(message:types.Message):
    await message.answer("Select a menu item",reply_markup=kb_menu)
