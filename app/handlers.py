from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
import app.keyboards as kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет!', reply_markup=kb.main)


@router.message(F.text == 'Каталог')
async def catalog(message: Message):
    await message.answer('Сделайте свой выбор из каталога', reply_markup=await kb.categories())


@router.callback_query(F.text.startswith('category_'))
async def category_selected(message: Message):
    category_id = message.data.split('_')[1]
    await message.answer(f'Вы выбрали категорию {category_id}')