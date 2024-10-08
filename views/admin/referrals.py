from aiogram import types
from crud.referral import get_all_referrals
from dp import dp


@dp.message(lambda message: message.text == "🗣 Referallar")
async def referral(message: types.Message):
    all_referrals = await get_all_referrals()
    text = f"barcha referallar soni :{all_referrals.get('count')} ta"
    return message.answer(
        text=text,
    )


