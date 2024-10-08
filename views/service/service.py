from aiogram import types, F
from keyboards.service_inline import SERVICE_INLINE_KEYBOARD
from dp import dp


@dp.message(lambda message: message.text == "🗂 Xizmatlar")
async def referral(message: types.Message):
    text = (
        f"✅ Bizning xizmatlarimizni tanlaganingizdan xursandmiz\n"
        f"👇 Quydagi xizmatlardan birini tanlang"
    )

    await message.answer(
        text=text,
        reply_markup=SERVICE_INLINE_KEYBOARD.service_keyboard()
    )


@dp.callback_query(F.data == "add_person")
async def handle_add_person(callback_query: types.CallbackQuery):
    text = (
        f"✅ Bizning xizmatlarimizni tanlaganingizdan xursandmiz\n"
        f"👇 Quyda Kanalga odam qo'shish narxlari"
    )

    await callback_query.message.edit_text(
        text=text,
        reply_markup=SERVICE_INLINE_KEYBOARD.add_person_keyboard()
    )


@dp.callback_query(F.data == "add_view")
async def handle_add_view(callback_query: types.CallbackQuery):
    text = (
        f"✅ Bizning xizmatlarimizni tanlaganingizdan xursandmiz\n"
        f"👇 Quyda postga ko'rishlar qo'shish narxlari"
    )

    await callback_query.message.edit_text(
        text=text,
        reply_markup=SERVICE_INLINE_KEYBOARD.add_view_keyboard()
    )


@dp.callback_query(F.data == "add_like")
async def handle_add_like(callback_query: types.CallbackQuery):
    text = (
        f"✅ Bizning xizmatlarimizni tanlaganingizdan xursandmiz\n"
        f"👇 Quyda postga like qo'shish narxlari"
    )

    await callback_query.message.edit_text(
        text=text,
        reply_markup=SERVICE_INLINE_KEYBOARD.add_like_keyboard()
    )

@dp.callback_query(F.data == "back-service")
async def handle_add_like(callback_query: types.CallbackQuery):
    text = (
        f"✅ Bizning xizmatlarimizni tanlaganingizdan xursandmiz\n"
        f"👇 Quydagi xizmatlardan birini tanlang"
    )

    await callback_query.message.edit_text(
        text=text,
        reply_markup=SERVICE_INLINE_KEYBOARD.service_keyboard()
    )