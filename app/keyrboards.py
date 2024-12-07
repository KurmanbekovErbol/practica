from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_button = [
     [InlineKeyboardButton(text="Камен, ножницы, бумага", callback_data="Rock_paper_scissors")],
     [InlineKeyboardButton(text="Рандомайзер", callback_data="Randomizer")]
]

inline_keyboard = InlineKeyboardMarkup(inline_keyboard=inline_button)

Rock_paper_scissors_button = [
    [InlineKeyboardButton(text="Камен", callback_data="rock")],
    [InlineKeyboardButton(text="ножницы", callback_data="paper")],
    [InlineKeyboardButton(text="бумага", callback_data="scissors")]
]

Rock_paper_scissors_keyboard = InlineKeyboardMarkup(inline_keyboard=Rock_paper_scissors_button)


Our_news_button = [
    [InlineKeyboardButton(text="О нас", callback_data="About_Us")],
    [InlineKeyboardButton(text="Адрес", callback_data="Address")],
    [InlineKeyboardButton(text="Наши курсы", callback_data="Our_courses")]
]

Our_news_keyboard = InlineKeyboardMarkup(inline_keyboard=Our_news_button)