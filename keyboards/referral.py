from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class ReferralKeyboard:

    @staticmethod
    def panel_keyboard():
        rows = [
            [KeyboardButton(text="📃 Referral Link")] ,
            [KeyboardButton(text="📊 Referrallar")],
            [KeyboardButton(text="⬅️ Ortga")],
        ]

        keyboard = ReplyKeyboardMarkup(
            keyboard=rows,
            resize_keyboard=True
        )

        return keyboard


REFERRAL_KEYBOARD = ReferralKeyboard()
