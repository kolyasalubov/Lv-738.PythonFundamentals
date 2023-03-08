from loader import tb
from aiogram import types
from aiogram.dispatcher.filters import Command
from states import register
from aiogram.dispatcher import FSMContext



@tb.message_handler(text = "/regist")
async def register_1(message:types.Message):
    await message.answer("HI,you have started registration,\nEnter your name  ")
    await register.test1.set()

@tb.message_handler(state=register.test1)
async def state1(message:types.Message,state:FSMContext):
    answer = message.text

    await state.update_data(test1=answer)
    await message.answer(f"{answer} how old are you?")
    await register.test2.set()

@tb.message_handler(state=register.test2)
async def state1(message:types.Message,state:FSMContext):
    answer = message.text

    await state.update_data(test2=answer)
    data = await state.get_data()
    name = data.get("test1")
    years = data.get("test2")
    # await state.update_data(test2=answer)
    # years = data.get("test2")
    await message.answer(f"Register create\nYour name {name}\nYou {years} years old")
    await state.finish()