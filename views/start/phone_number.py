from aiogram.fsm.context import FSMContext
from asgiref.sync import sync_to_async

from dp import dp
from crud.users import get_user_db, update_user_db, add_point
from crud.referral import get_referral
from aiogram.types import Message

from keyboards.user import USER_KEYBOARD
from states.phone_number import UserPhoneState


@dp.message(UserPhoneState.waiting_for_phone_number, lambda message: message.contact)
async def receive_contact(message: Message, state: FSMContext):
    await state.clear()
    user_phone_number = message.contact.phone_number
    user_id = message.chat.id

    user = await get_user_db(user_id=user_id)

    user = await update_user_db(
        user=user,
        phone=user_phone_number,
        is_active=True,
        is_referred=True
    )

    referral = await get_referral(offered_user=user)
    parent_user = await sync_to_async(lambda: referral.user)()
    point = await sync_to_async(lambda: referral.amount)()
    await add_point(user=parent_user, point=point)


    await message.answer(
        f"Siz {user_phone_number} raqami bilan ro'yhatdan o'tdingiz ",
        reply_markup=USER_KEYBOARD.admin_panel_keyboard()
    )
