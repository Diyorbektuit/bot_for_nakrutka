from aiogram import types
from dp import dp
from crud.referral import user_referrals
from keyboards.referral import REFERRAL_KEYBOARD


@dp.message(lambda message: message.text == "📊 Referrallar")
async def referral(message: types.Message):
    user_id = message.chat.id
    data = await user_referrals(user_id)

    text1 = f"Umumiy referrallaringiz soni: {data['referrals_count']}ta \nOxirgi 10ta taklif qilgan odamlaringiz: \n\n"
    text2 = ""
    for count, user in enumerate(data['referral_users'], 1):
        text2 += f"{count}. {user}\n"

    text = text1 + text2

    await message.answer(text=text, reply_markup=REFERRAL_KEYBOARD.panel_keyboard())

