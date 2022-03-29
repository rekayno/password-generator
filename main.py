import os
os.system('pip install -r requirements.txt')
import string
import random
from typing import Any
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from keep_alive import keep_alive

TOKEN = os.environ['TOKEN']
dp = Dispatcher()

characters = list(string.ascii_letters + string.digits + '!@#$%^&*()')

@dp.message(commands={"start"})
async def command_start_handler(message: Message) -> None:
    await message.answer(f'Hello, <b>{message.from_user.full_name}!</b>\nI can generate a password for you\nPlease send me the password length by message')


@dp.message()
async def echo_handler(message: types.Message) -> Any:
    if message.text.isnumeric():
        length = int(message.text)
        if length > 1000:
            await message.answer('Maximum password length - 1000 characters')
            return
        await message.answer(generate_password(int(message.text)))
        
def generate_password(length: int):
    password = []
    for i in range(int(length)):
        password.append(random.choice(characters))
    random.shuffle(password)
    return ''.join(password)

def main() -> None:
    bot = Bot(TOKEN, parse_mode='HTML')
    dp.run_polling(bot)


if __name__ == '__main__':
    keep_alive()
    main()
