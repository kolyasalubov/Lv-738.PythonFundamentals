
from aiogram import types
from loader import tb

@tb.message_handler(text = "/help")
async def command_help(message:types.Message):
    await message.answer(f"Hello {message.from_user.full_name}!\nYou need help?")
