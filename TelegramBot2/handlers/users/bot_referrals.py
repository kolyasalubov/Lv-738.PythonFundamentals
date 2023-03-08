from aiogram import types
from loader import tb
from aiogram.utils.deep_linking import get_start_link
from utils.tb_api import quick_comands as commands
from utils.tb_api.quick_comands import count_refs

@tb.message_handler(text = "/ref")
async def command_help(message:types.Message):
    ref_link = await get_start_link(payload=message.from_user.id)
    count_refs = await commands.count_refs(message.from_user.id)
    await message.answer(f"Hi {message.from_user.first_name}\n"
    f"Your ref link:\n"
    f"{ref_link}\n"
    f"Your count refs = {count_refs}\n")
    