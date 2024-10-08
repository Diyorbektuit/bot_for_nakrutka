from aiogram import F
from aiogram.types import InlineKeyboardMarkup, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from dp import dp



def create_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text="Meni bos", callback_data="btn_click")

    return keyboard.as_markup()


@dp.callback_query(F.data == "btn_click")
async def button_click_handler(callback_query: CallbackQuery):
    await callback_query.answer("Siz bu tugmani bosdinging!")

    await callback_query.message.edit_text(
        "Siz bu tugmani bosdinging! 🎉",
        reply_markup=None
    )