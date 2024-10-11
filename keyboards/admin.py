from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


class AdminKeyboard:

    @staticmethod
    def admin_panel_keyboard():
        rows = [
            [KeyboardButton(text="💰 Umumiy hisob"), KeyboardButton(text="🗂 Xizmatlar")],
            [KeyboardButton(text="🗣 Referallar"), KeyboardButton(text="📊 Umumiy foydalanuvchilar")],
            [KeyboardButton(text="Hisob to'dirish so'rovlari")]
        ]

        keyboard = ReplyKeyboardMarkup(
            keyboard=rows,
            resize_keyboard=True
        )

        return keyboard


    @staticmethod
    def inline_payment_applications_update():
        rows = [
            [InlineKeyboardButton(text="tasdiqlash", callback_data="approved")],
            [InlineKeyboardButton(text="bekor qilish", callback_data="canceled")],
        ]

        keyboard = InlineKeyboardMarkup(
            inline_keyboard=rows,
        )

        return keyboard


ADMIN_KEYBOARD = AdminKeyboard()
