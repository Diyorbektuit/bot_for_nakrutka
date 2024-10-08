from aiogram import types

from dp import dp
from keyboards.referral import REFERRAL_KEYBOARD


@dp.message(lambda message: message.text == "🗣 Referal")
async def referral(message: types.Message):
    user_id = message.chat.id
    photo_path = "/home/diyorbek/PycharmProjects/my_bot/referral.jpeg"
    referral_link = f"https://t.me/example_dbot?start={user_id}"

    response_text = (
        f"🌟 <b>Sizning referal havolangiz tayyor!</b> 🌟\n\n"
        "<b>Sizning referal havolangizni do'stlaringizga ulashing va botdan ko'proq foyda ko'ring:</b>\n\n"
        f"➡️ <a href='{referral_link}'>Sizning referal havolangiz</a>\n\n"
        "📈 <b>Har bir yangi foydalanuvchi uchun siz ball olasiz!</b> \n\n"
        "<b>Katta bonuslarga ega bo'lish uchun imkoniyatni qo'ldan boy bermang:</b>\n\n"
        "1️⃣ <b>Ko'proq ball yig'ing</b>\n\n"
        "2️⃣ <b>Eksklyuziv sovg'alarga ega bo'ling</b>\n\n"
        "3️⃣ <b>Maxsus chegirmalar va imkoniyatlardan foydalaning</b>\n\n"
        "🤝 <b>Do'stlaringizni taklif qiling va imkoniyatlaringizni kengaytiring!</b>"
    )

    await message.answer_photo(
        types.FSInputFile(path=photo_path),
        caption=response_text,
        parse_mode="html",
        reply_markup=REFERRAL_KEYBOARD.panel_keyboard()
    )

