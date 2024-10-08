from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class UserKeyboard:

    @staticmethod
    def admin_panel_keyboard():
        rows = [
            [KeyboardButton(text="💰 Mening hisobim"), KeyboardButton(text="🗂 Xizmatlar")],
            [KeyboardButton(text="🗣 Referal"), KeyboardButton(text="💵 Hisob to'ldirish")],
            [KeyboardButton(text="⚙️ Sozlamalar"), KeyboardButton(text="📕 Qo'llanma")] ,
            [KeyboardButton(text="☎️ Murojaat"), KeyboardButton(text="🤝 Hamkorlik dasturi")],
        ]

        keyboard = ReplyKeyboardMarkup(
            keyboard=rows,
            resize_keyboard=True
        )

        return keyboard


USER_KEYBOARD = UserKeyboard()
