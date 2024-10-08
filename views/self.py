from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from dp import dp
from keyboards.inline import create_keyboard


@dp.message(Command("self"))
async def self(message: Message, state=FSMContext):
    await message.answer(
        "Bu ichki tugma",
        reply_markup=create_keyboard()
    )


