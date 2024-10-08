from aiogram import types
from dp import dp
from crud.users import get_user_db
from crud.payment_application import create_application


@dp.message(lambda message: message.text == "💰 Mening hisobim")
async def cmd_balance(message: types.Message):
    user_id = message.chat.id
    user = await get_user_db(user_id)
    wallet = user.wallet

    text = (f"Mening Balansim: \n"
            f"Sizning balansingiz: {wallet} so'm \n")

    await message.answer(text)

@dp.message(lambda message: message.text == "💵 Hisob to'ldirish")
async def add_point(message: types.Message):
    user_id = message.chat.id
    user = await  get_user_db(user_id)
    await create_application(user, )
