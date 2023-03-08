
from aiogram import types
from loader import tb
from utils.misc.throttling import rate_limit




@rate_limit(limit = 3)
@tb.message_handler(text = "/start")
async def command_start(message:types.Message):
    await message.answer(f"Hello {message.from_user.full_name}!\nYour id: {message.from_user.id}")
