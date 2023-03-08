from aiogram.types import ReplyKeyboardMarkup,KeyboardButton



kb_menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Anime"),
            KeyboardButton(text="10"),
            
        ],
        [
            KeyboardButton(text="11"),
            KeyboardButton(text="12"),
        ],
        [
            KeyboardButton(text="13"),
            KeyboardButton(text="14"),
            KeyboardButton(text="15"),
        ]
    ],
    resize_keyboard=True
    
)