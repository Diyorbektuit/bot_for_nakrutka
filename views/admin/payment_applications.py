from aiogram import types, F
from aiogram.fsm.context import FSMContext

from crud.payment_application import moderation_applications_for_admin, get_application, add_point_user_db
from dp import dp
from keyboards.admin import ADMIN_KEYBOARD
from states.payment_applications import PaymentApplicationState, PaymentUpdateState


@dp.message(lambda message: message.text == "Hisob to'dirish so'rovlari")
async def payment_applications_1(message: types.Message, state=FSMContext):
    all_applications = await moderation_applications_for_admin()

    text = (f"barcha moderatsiyadagi hisob\n "
            f"to'dirish so'rovlari soni: {all_applications.get('all_count')} ta\n \n")
    text2 = ""
    for app in all_applications.get('data'):
        text2 += (f"{app.get('number')}. ID: {app.get('id')}\n"
                  f"Arizachi:{app.get('user')}\n \n")
    text += text2

    await state.set_state(PaymentApplicationState.first)
    return message.answer(
        text=text,
    )


@dp.message(PaymentApplicationState.first)
async def payment_applications_2(message: types.Message, state=FSMContext):
    number = message.text
    try:
        number = int(number)
        app = await get_application(number)
    except:
        app = False

    if app == False:
        return message.answer(
            text=f"Bunday so'rov yo'q"
        )
    else:
        user_info = app['user']
        text = f"user: {user_info}"
        await state.update_data(user=user_info)
        return message.answer_photo(
            caption=text,
            photo=types.FSInputFile(path=str(app.get('receipt'))),
            reply_markup=ADMIN_KEYBOARD.inline_payment_applications_update()
        )


@dp.callback_query(F.data == "approved")
async def approved_payment(callback: types.CallbackQuery, state=FSMContext):
    data = await state.get_data()
    user = data.get('user', 'No user info')

    await state.set_state(PaymentUpdateState.approved)
    await callback.message.answer(
        text=f"{user} uchun \n"
             f"To'ldirish summasini kiriting"
    )


@dp.callback_query(F.data == "canceled")
async def approved_payment(callback: types.CallbackQuery, state=FSMContext):
    data = await state.get_data()
    user = data.get('user', 'No user info')

    await state.set_state(PaymentUpdateState.approved)
    await callback.message.answer(
        text=f"{user} uchun \n"
             f"To'ldirish summasini kiriting"
    )


@dp.callback_query(lambda message: message.text == "")
async def add_point_user(message:types.Message, state=FSMContext):
    point = int(message.text)
    data = await state.get_data()
    user = data.get('user', 'No user info')

    await add_point_user_db(amount=point, user=user)

