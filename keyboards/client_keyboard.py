from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

button_1 = KeyboardButton('/Режим_работы')
button_2 = KeyboardButton('/Расположение')
button_3 = KeyboardButton('/Меню')
button_4 = KeyboardButton('Поедлиться_номером', request_contact=True)
button_5 = KeyboardButton('Отправить геолокацию', request_location=True)
kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)   # one_time_keyboard - скрывает
                                                                                # клавиатуру после нажатия кнопки

kb_client.add(button_1).row(button_2, button_3).row(button_4, button_5)
#kb_client.row(button_1, button_2)   # add - с новой сторки, insert - в одну строку если влезет
                                    # row - все в одну строку
