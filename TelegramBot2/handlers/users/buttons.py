
from aiogram import types
from loader import tb

@tb.message_handler(text = "10")
async def button_test(message:types.Message):
    await message.answer(f"Hello {message.from_user.full_name}!\nYou choose {message.text}")


@tb.message_handler(text = "Anime")
async def button_test(message:types.Message):
    await message.answer(f"Hello {message.from_user.full_name}!\nYou choose {message.text},if you want to watch amnime click to lint https://v2.vost.pw/tip/tv/116-bleach1.html")
