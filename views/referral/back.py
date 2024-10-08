from aiogram import types

from dp import dp
from keyboards.user import USER_KEYBOARD


@dp.message(lambda message: message.text == "⬅️ Ortga")
async def referral(message: types.Message):
    await message.answer(
        text="Boshqaruv paneli",
        reply_markup=USER_KEYBOARD.admin_panel_keyboard()
    )

