from aiogram.fsm.state import StatesGroup, State

class PaymentApplicationState(StatesGroup):
    first = State()
    second = State()

class PaymentUpdateState(StatesGroup):
    approved = State()
    canceled = State()