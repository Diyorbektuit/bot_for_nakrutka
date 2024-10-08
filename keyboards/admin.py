from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class AdminKeyboard:

    @staticmethod
    def admin_panel_keyboard():
        rows = [
            [KeyboardButton(text="💰 Umumiy hisob"), KeyboardButton(text="🗂 Xizmatlar")],
            [KeyboardButton(text="🗣 Referallar"), KeyboardButton(text="📊 Umumiy foydalanuvchilar")],
        ]

        keyboard = ReplyKeyboardMarkup(
            keyboard=rows,
            resize_keyboard=True
        )

        return keyboard


ADMIN_KEYBOARD = AdminKeyboard()
