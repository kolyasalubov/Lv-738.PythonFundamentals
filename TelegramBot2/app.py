from aiogram.utils import executor
from aiogram import Bot, Dispatcher,types



async def on_startup(tb):

    import midlwears
    midlwears.setup(tb)

    from loader import db
    from utils.tb_api.tb_yura import on_startup
    print ("Connection to PostgreSQL")
    await on_startup(db)

    print("Delete database")
    await db.gino.drop_all()

    print("Creation of waistcoats")
    await db.gino.create_all()
    print("ok")

    from utils.notifly_admins import on_startap_notify
    await on_startap_notify(tb)

    from utils.set_bot_commands import set_defolt_commands
    await set_defolt_commands(tb)
    
    print("Bot started")

if __name__ == "__main__":
    from aiogram import executor
    from handlers import tb
     

    executor.start_polling(tb,on_startup=on_startup)