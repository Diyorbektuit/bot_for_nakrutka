from aiogram import types

from dp import dp
from keyboards.referral import REFERRAL_KEYBOARD


@dp.message(lambda message: message.text == "📃 Referral Link")
async def referral(message: types.Message):
    user_id = message.chat.id
    photo_path = "/home/diyorbek/PycharmProjects/my_bot/referral.jpeg"
    referral_link = f"https://t.me/example_dbot?start={user_id}"

    response_text = (
        f"➡️Sizning referal havolangiz\n\n"
        f"{referral_link}"
    )

    await message.answer_photo(
        types.FSInputFile(path=photo_path),
        caption=response_text,
        reply_markup=REFERRAL_KEYBOARD.panel_keyboard()
    )

