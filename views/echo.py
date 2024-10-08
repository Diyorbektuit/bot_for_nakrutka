from dp import dp
from aiogram.types import Message


# Handle all other messages
@dp.message()
async def echo_message(message: Message):
    await message.answer(f"You said: {message.text}")
