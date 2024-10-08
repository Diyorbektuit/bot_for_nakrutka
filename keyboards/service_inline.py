from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class ServiceKeyboard:

    @staticmethod
    def service_keyboard():

        rows = [
            [InlineKeyboardButton(text="kanalga odam qo'shish", callback_data="add_person")],
            [InlineKeyboardButton(text="postga ko'rishlar qo'shish", callback_data="add_view")],
            [InlineKeyboardButton(text="postga like qo'shish", callback_data="add_like")]
        ]

        keyboard = InlineKeyboardMarkup(
            inline_keyboard=rows,
        )

        return keyboard

    @staticmethod
    def add_person_keyboard():
        rows = [
            [InlineKeyboardButton(text="1k --> 15 000 so'm", callback_data="1k-person")],
            [InlineKeyboardButton(text="5k --> 65 000 so'm ", callback_data="5k-person")],
            [InlineKeyboardButton(text="10k --> 120 000 so'm", callback_data="10k-person")],
            [InlineKeyboardButton(text="20k --> 220 000 so'm", callback_data="20k-person")],
            [InlineKeyboardButton(text="50k --> 500 000 so'm", callback_data="50k-person")],
            [InlineKeyboardButton(text="ortga", callback_data="back-service")],
        ]

        keyboard = InlineKeyboardMarkup(
            inline_keyboard=rows,
        )

        return keyboard

    @staticmethod
    def add_view_keyboard():
        rows = [
            [InlineKeyboardButton(text="1k --> 15 000 so'm", callback_data="1k-view")],
            [InlineKeyboardButton(text="5k --> 65 000 so'm ", callback_data="5k-view")],
            [InlineKeyboardButton(text="10k --> 120 000 so'm", callback_data="10k-view")],
            [InlineKeyboardButton(text="20k --> 220 000 so'm", callback_data="20k-view")],
            [InlineKeyboardButton(text="50k --> 500 000 so'm", callback_data="50k-view")],
            [InlineKeyboardButton(text="ortga", callback_data="back-service")],
        ]

        keyboard = InlineKeyboardMarkup(
            inline_keyboard=rows,
        )

        return keyboard

    @staticmethod
    def add_like_keyboard():
        rows = [
            [InlineKeyboardButton(text="1k --> 15 000 so'm", callback_data="1k-like")],
            [InlineKeyboardButton(text="5k --> 65 000 so'm ", callback_data="5k-like")],
            [InlineKeyboardButton(text="10k --> 120 000 so'm", callback_data="10k-like")],
            [InlineKeyboardButton(text="20k --> 220 000 so'm", callback_data="20k-like")],
            [InlineKeyboardButton(text="50k --> 500 000 so'm", callback_data="50k-like")],
            [InlineKeyboardButton(text="ortga", callback_data="back-service")],
        ]

        keyboard = InlineKeyboardMarkup(
            inline_keyboard=rows,
        )

        return keyboard


SERVICE_INLINE_KEYBOARD = ServiceKeyboard()
