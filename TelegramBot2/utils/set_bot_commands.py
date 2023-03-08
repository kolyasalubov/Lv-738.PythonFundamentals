from aiogram import types

async def set_defolt_commands(tb):
    await tb.bot.set_my_commands([
        types.BotCommand("start","Start bot"),
        types.BotCommand("help","Help to you"),
        types.BotCommand("regist","Help to you register"),
        types.BotCommand("photo","Show photo"),
        types.BotCommand("profile","Get data from database"),
        types.BotCommand("ref","Get your referral id")
        
    ])