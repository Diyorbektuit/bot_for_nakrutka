from aiogram import types
from dp import dp, bot
from states.balance import BalanceState
from aiogram.fsm.context import FSMContext
from crud.users import get_user_db
from crud.payment_application import (create_payment_application, all_payment_amount_application,
                                      count_payment_approved_applications)
from crud.referral import user_referrals_count
import os

RECEIPT_DOWNLOAD_PATH = './media/receipt/'

@dp.message(lambda message: message.text == "💰 Mening hisobim")
async def cmd_balance(message: types.Message):
    user_id = message.chat.id
    user = await get_user_db(user_id)
    wallet = user.wallet

    all_amount = await all_payment_amount_application(user)
    referral_count = await user_referrals_count(user)
    payment_applications_count = await count_payment_approved_applications(user)

    text = (f"👤 Sizning ID raqamingiz:{user_id} \n\n"
            f"💵 Balansingiz: {wallet} so'm \n"
            f"📊 Buyurtmalaringiz: {payment_applications_count}\n"
            f"🗣 Referallaringiz: {referral_count} \n"
            f"💰 Botga kiritgan pullaringiz: {all_amount} \n")

    await message.answer(text)

@dp.message(lambda message: message.text == "💵 Hisob to'ldirish")
async def add_point(message: types.Message, state=FSMContext):
    await state.set_state(BalanceState.first)
    await message.answer(
        text=f"Hisobni to'ldirish uchun quyidagi karta raqamga to'lov qilib\n"
             f"botga chekini yuborishingiz kerak shunda sizning \n"
             f"hisobingizga pul qo'shib beriladi:\n\n"
             f"5614680006684340"
    )


@dp.message(BalanceState.first)
async def add_point_second(message: types.Message, state: FSMContext):
    user_id = message.chat.id
    photo = message.photo[-1]

    if not photo:
        await message.reply(
            text="Iltimos faqat hisob to'ldirish uchun tashlagan pulingizni chekini yuboring"
        )
        return

    if not os.path.exists(RECEIPT_DOWNLOAD_PATH):
        os.makedirs(RECEIPT_DOWNLOAD_PATH)

    file_info = await bot.get_file(photo.file_id)

    file_path = f"{RECEIPT_DOWNLOAD_PATH}{message.from_user.id}_receipt.jpg"

    await bot.download_file(file_info.file_path, file_path)

    user = await get_user_db(user_id)

    app = await create_payment_application(user=user, receipt_path=file_path)

    await state.clear()
    await message.answer(
        text=f"Hisob to'ldirish buyurtmangiz qabul qilindi \n "
             f"Buyurtma raqami : {app.id}\n"
             f"Tez orada hisobingiz to'ldirilishi bilan sizga xabar beramiz"
    )
