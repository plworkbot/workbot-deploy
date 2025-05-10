from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN
from sheets import add_user

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

user_data = {}

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    await message.answer("Привіт! Як тебе звати?")
    user_data[message.from_user.id] = {}

@dp.message_handler(lambda message: message.from_user.id in user_data and 'name' not in user_data[message.from_user.id])
async def get_name(message: types.Message):
    user_data[message.from_user.id]['name'] = message.text
    await message.answer("Введи номер телефону:")

@dp.message_handler(lambda message: 'phone' not in user_data.get(message.from_user.id, {}))
async def get_phone(message: types.Message):
    user_data[message.from_user.id]['phone'] = message.text
    await message.answer("Яке у тебе громадянство?")

@dp.message_handler(lambda message: 'citizenship' not in user_data.get(message.from_user.id, {}))
async def get_citizenship(message: types.Message):
    user_data[message.from_user.id]['citizenship'] = message.text
    await message.answer("Який маєш досвід роботи?")

@dp.message_handler(lambda message: 'experience' not in user_data.get(message.from_user.id, {}))
async def get_experience(message: types.Message):
    user_data[message.from_user.id]['experience'] = message.text
    await message.answer("У якому місті хочеш працювати?")

@dp.message_handler(lambda message: 'city' not in user_data.get(message.from_user.id, {}))
async def get_city(message: types.Message):
    user_data[message.from_user.id]['city'] = message.text
    add_user(user_data[message.from_user.id])
    await message.answer("✅ Дякую, анкета заповнена!")
    user_data.pop(message.from_user.id)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
