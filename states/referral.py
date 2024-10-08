from aiogram.fsm.state import StatesGroup, State


class ReferralState(StatesGroup):
    first = State()
    second = State()