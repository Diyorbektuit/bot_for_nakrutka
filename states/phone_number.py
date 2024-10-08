from aiogram.fsm.state import StatesGroup, State

class UserPhoneState(StatesGroup):
    waiting_for_phone_number = State()
    keyboards = State()
