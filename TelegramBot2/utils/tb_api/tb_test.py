from data import config
import quick_comands
from tb_yura import tp
import asyncio


async def tp_test():
 

    users = await quick_comands.select_all_users()
    print(list(users))

    count = await quick_comands.count_users()
    print(count)

    user = await quick_comands.select_user(1)
    print(user)

    # await quick_comands.update_user_name(1,"new name")

    user = await quick_comands.select_user(1)
    print(user)


loop = asyncio.get_event_loop()
loop.run_until_complete(tp_test())