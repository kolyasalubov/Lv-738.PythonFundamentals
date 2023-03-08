
from aiogram import types
from loader import tb
from aiogram.dispatcher.filters import CommandStart
from utils.tb_api import quick_comands as commands
from utils.misc import rate_limit


@rate_limit(limit = 3)
@tb.message_handler(CommandStart())
async def command_start(message:types.Message):
    args = message.get_args()
    print(args)

    new_args = await commands.check_args(args,message.from_user.id )
    print(new_args)
    
    try :
        user = await commands.select_user(message.from_user.id)
        if user.status == "active":
            await message.answer(f"Hi {user.first_name}\nYou are already registered")
        elif user.status == "baned":
            await message.answer("You are banned.") 
    except Exception:
        await commands.add_user(user_id = message.from_user.id,
        first_name = message.from_user.first_name,
        last_name = message.from_user.last_name,
        username = message.from_user.username,
        referral_id = int(new_args),
         status = "active")
        await message.answer("You are registered")
        

    try :
        await tb.bot.send_message(chat_id = int(new_args),text = f"Thanks to you {message.from_user.first_name} registered")
    except Exception:
        pass
        

@rate_limit(limit = 3)
@tb.message_handler(text = "/ban")
async def get_ban(message:types.Message):
    await commands.update_status(user_id = message.from_user.id,status = "baned")
    await message.answer("They banned you")


@rate_limit(limit = 3)
@tb.message_handler(text = "/unban")
async def get_unban(message:types.Message):
    await commands.update_status(user_id = message.from_user.id,status ="active")
    await message.answer("They unbanned you")


@rate_limit(limit = 3)
@tb.message_handler(text = "/profile")
async def get_unban(message:types.Message):
    user = await commands.select_user(message.from_user.id)
    await commands.update_status(user_id = message.from_user.id,status="active")
    await message.answer(f"Id - {user.user_id}\n"
    f"first_name - {user.first_name}\n"
    f"last_name - {user.last_name}\n"
    f"username - {user.username}\n"
    f"status - {user.status}\n")