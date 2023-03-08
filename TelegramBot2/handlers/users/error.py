from aiogram import types
from loader import tb

@tb.message_handler()
async def command_error(message:types.Message):
    await message.answer(f"Command - {message.text} no found")
