from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



ikb_menu = InlineKeyboardMarkup(row_width=2,
inline_keyboard=[
    [
        InlineKeyboardButton(text="Message",callback_data = "Message"),
        InlineKeyboardButton(text="anime link",url = "https://v2.vost.pw/tip/tv/116-bleach1.html")
    ],
    [
        InlineKeyboardButton(text="alert",callback_data = "alert")
        
    ]
]) 