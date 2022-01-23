from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client


#@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await message.answer('Приятного аппетита', reply_markup=kb_client)


#@dp.message_handler(commands=['Режим_работы'])
async def pizza_open_command(message: types.Message):
    await message.answer('Пн-Вс с 9:00 по 21:00', reply_markup=kb_client)


#@dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message: types.Message):
    await message.answer('ул. Медиков 15 ', reply_markup=kb_client)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['Режим_работы'])
    dp.register_message_handler(pizza_place_command, commands=['Расположение'])
