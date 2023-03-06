import requests

from aiogram import Bot, Dispatcher, executor, types

import day_6_classwork, NikeClothes

TOKEN = "6260729558:AAEX2TKRMI2qEXVe0cJITo5XYZKBAIyqjSs"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"]) 
async def start_function(message: types.Message): 
    button = [[types.KeyboardButton("/Jordan"), types.KeyboardButton("/Nike_clothes")]] 
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard = True) 
    await message.reply("Choose thing", reply_markup = keyboard) 
 
@dp.message_handler(commands=["Jordan"]) 
async def shoes(message: types.Message): 
    for i in day_6_classwork.shoes: 
        # sleep(3) 
        await message.reply(i) 
 
    
@dp.message_handler(commands=["Nike_clothes"]) 
async def clothes(message: types.Message): 
    for i in NikeClothes.clothes: 
        # sleep(3) 
        await message.reply(i) 
 
if __name__ == "__main__": 
    executor.start_polling(dp)