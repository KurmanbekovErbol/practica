import random
from aiogram import types, F
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup

from app.keyrboards import *
from aiogram import Router

router=Router()

@router.message(CommandStart())
async def command_start(message: types.Message):
    await message.answer(f'Привет {message.from_user.first_name}')

@router.message(F.text=="Игра")
async def game(callback: types.CallbackQuery):
        await callback.message.answer("Выберите кнопку", reply_markup=inline_keyboard)

@router.message(F.text=="Наши новости")
async def news(callback: types.CallbackQuery):
        await callback.message.answer("Выберите кнопку", reply_markup=Our_news_keyboard)

@router.callback_query(F.data=="Rock_paper_scissors")
async def Rock_paper_scissors(callback: types.CallbackQuery):
        await callback.message.answer("Выберите кнопку", reply_markup=Rock_paper_scissors_keyboard)

class RANDOM(StatesGroup):
    choice = State()

@router.callback_query(F.data=="rock")
async def rock(callback: types.CallbackQuery):
        await callback.message.answer("Вы выбрали камень")

@router.callback_query(F.data=="paper")
async def paper(callback: types.CallbackQuery):
        await callback.message.answer("Вы выбрали ножницы")

@router.callback_query(F.data=="scissors")
async def scissors(callback: types.CallbackQuery):
        await callback.message.answer("Вы выбрали бумага")

@router.callback_query(F.data=="Randomizer")
async def Randomizer(callback: types.CallbackQuery):
        Random = str(random.randint(1,3))


@router.callback_query(F.data=="About_Us")
async def About_Us(callback: types.CallbackQuery):
        await callback.message.answer("Очистка отменена.")

@router.callback_query(F.data=="Address")
async def Address(callback: types.CallbackQuery):
        await callback.message.answer("Очистка отменена.")

@router.callback_query(F.data=="Our_courses")
async def Our_courses(callback: types.CallbackQuery):
        await callback.message.answer("Очистка отменена.")