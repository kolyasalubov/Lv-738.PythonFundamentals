from cgitb import text
from loader import tb
from aiogram.types import ContentType,Message,MediaGroup,InputFile,ChatActions






video_file_id = "BAACAgIAAxkBAAIEe2QAAWxI9qkEQCZ3BaZLbQb-SSLLqwACgCoAAiuB-Ete0v97oOVlVC4E"
photo_file_id = "AgACAgIAAxkBAAIEJ2P_RTRiBw_jRuuyopWJkcZhd20BAAKByTEbK4H4Syf2roqFzdxEAQADAgADeAADLgQ"
photo_url = ""
# photo_file_id1 = "AgACAgIAAxkBAAIEeWQAAVnyTVC0ucIHYSDg6vIjjeKJ9AAC58MxG2436EvGw_K8M-bXPwEAAwIAA3kAAy4E"
photo_bytes = InputFile(path_or_bytesio="media/1572512819_3.jpg")




@tb.message_handler(content_types=ContentType.VIDEO)
async def send_video_file_id(message:Message):
    await message.reply(message.video.file_id)

@tb.message_handler(content_types=ContentType.PHOTO)
async def send_photo_file_id(message:Message):
    await message.reply(message.photo[-1].file_id) 






@tb.message_handler(text = "/photo")
async def send_photo(message:Message):
    chat_id = message.from_user.id 
    await ChatActions.upload_photo()



    video_file_id = "BAACAgIAAxkBAAIEe2QAAWxI9qkEQCZ3BaZLbQb-SSLLqwACgCoAAiuB-Ete0v97oOVlVC4E"
    photo_file_id = "AgACAgIAAxkBAAIEJ2P_RTRiBw_jRuuyopWJkcZhd20BAAKByTEbK4H4Syf2roqFzdxEAQADAgADeAADLgQ"
    photo_url = ""
    # photo_file_id1 = "AgACAgIAAxkBAAIEeWQAAVnyTVC0ucIHYSDg6vIjjeKJ9AAC58MxG2436EvGw_K8M-bXPwEAAwIAA3kAAy4E"
    photo_bytes = InputFile(path_or_bytesio="media/1572512819_3.jpg")
    await tb.bot.send_photo(chat_id=chat_id,photo=photo_file_id)
    # await tb.bot.send_photo(chat_id=chat_id)


@tb.message_handler(text = "/album")
async def send_album(message:Message):
    album = MediaGroup()
    chat_id = message.from_user.id 
    await ChatActions.upload_photo()


    album.attach_photo(photo_bytes,caption="shoto tam")
    album.attach_photo(photo_file_id)
    album.attach_video(video_file_id)
    await message.answer_media_group(media = album)