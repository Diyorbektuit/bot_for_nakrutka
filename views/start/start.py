from uuid import uuid4

from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from dp import dp
from crud.users import have_user_db, get_user_db, create_user_in_db
from crud.referral import create_referral
from states.phone_number import UserPhoneState
from keyboards.user import USER_KEYBOARD
from keyboards.admin import ADMIN_KEYBOARD


@dp.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    user_id = message.chat.id
    first_name = message.chat.first_name
    last_name = message.chat.last_name
    username = message.chat.username
    password = str(uuid4())
    text_parts = message.text.split()
    referrer_id = int(text_parts[1]) if len(text_parts) > 1 and text_parts[1].isdigit() else None
    fullname = f"{message.chat.first_name} {message.chat.last_name}"
    if username is None:
        username = str(user_id)
    if await have_user_db(user_id=user_id):
        user = await get_user_db(user_id=user_id)
        if user.role == "admin":
            await message.answer(
                f"Salom {fullname} botga xush kelibsiz admin!",
                reply_markup=ADMIN_KEYBOARD.admin_panel_keyboard()
            )
        else:
            await message.answer(
                f"Salom {fullname} botga xush kelibsiz!",
                reply_markup=USER_KEYBOARD.admin_panel_keyboard()
            )

    else:
        if referrer_id:
            referred_user = await get_user_db(user_id=referrer_id)
            if referred_user is not None:
                user = await create_user_in_db(
                    phone=None,
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    user_id=str(user_id),
                    is_referred=True
                )

                referral = await create_referral(
                    user=referred_user,
                    offered_user=user
                )

        keyboard = ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="Telefon raqamni yuborish", request_contact=True)]],
            resize_keyboard=True,
        )

        await state.set_state(UserPhoneState.waiting_for_phone_number)
        await message.answer(
            f"Salom {fullname} botga xush kelibsiz! \n"
            f"Botdan foydalanish uchun raqamingizni yuboring",
            reply_markup=keyboard
        )



