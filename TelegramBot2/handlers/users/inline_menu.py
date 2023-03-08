from pydoc import text
from aiogram import types
from loader import tb
from keyboard.inline import ikb_menu



@tb.message_handler(text="14")
async def show_line_menu(message:types.Message):
    await message.answer("buttons below",reply_markup = ikb_menu)

# @tb.callback_query_handler(text = "Message")
# async def send_message()