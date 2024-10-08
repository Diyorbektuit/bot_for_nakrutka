from aiogram import types
from dp import dp
from crud.users import get_users_count


@dp.message(lambda message: message.text == "📊 Umumiy foydalanuvchilar")
async def stat(message: types.Message):
    data = await get_users_count()


    text = (f"Botning umumiy statistikasi: \n"
            f"Umumiy foydalanuvchilar soni: {data['all_users_count']}ta \n "
            f"Oxirgi oyda kirgan foydalanuvchilar soni: {data['last_week_count']}ta \n"
            f"Oxirgi haftada kirgan foydalanuvchilar soni:{data['last_month_count']}ta "
            )

    await message.answer(text)


