from aiogram import Bot, Dispatcher, executor, types
import pyqrcode 
from aiogram.types import  ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
bot = Bot(token='5958506659:AAF69UwcQvrVIk-F9HW8IQTzeb7eZDvpg9M' )

dp = Dispatcher(bot)

button1 = KeyboardButton('გამარჯობა!💋💋')
button2 = KeyboardButton('იუთუბი💖')
button3 = KeyboardButton('ფეისბუქი😎')
button4 = KeyboardButton('ტვიტერი✌')
keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1).add(button2).row( button3,button4)


@dp.message_handler(commands=['start','help'])
async def logo(message: types.Message):
    await message.answer_photo('https://th.bing.com/th/id/R.a06040fb38c4b5d69fdcaef03e510484?rik=2YF%2baN5QNrgoOA&riu=http%3a%2f%2fwww.freewebs.com%2fganjaman65%2fganjamanby-giuseppi.jpg&ehk=2eSYiIWxgwvGgYz%2fKd0c0h667QmkLWYV6nZBP6fKzoc%3d&risl=&pid=ImgRaw&r=0');
    await message.reply("გამარჯობა მე ვარ ბოტი, სახელად - რუსთავსკი", reply_markup=keyboard1)

@dp.message_handler()
async def kb_answer(message: types.Message):
   if message.text == 'გამარჯობა!💋💋':
    await message.answer('ბარო, რავახარ?')
   elif message.text == 'იუთუბი💖':
      await message.answer('https://youtube.com/avtunika')
   elif message.text == 'ფეისბუქი😎':
      await message.answer('https://www.facebook.com/profile.php?id=100089902212603')
   elif message.text == 'ტვიტერი✌':
      await message.answer('ტვიტერი არმაქვს')  
   else:
      await message.answer(f'შენი მონაწერი არის  :{message.text}')        








#dp.message_handler()
#async def qr(message: types.Message):
    #text = pyqrcode.create(message.text)
    #text.png('Code.png', scale=5)
    #await  bot.send_photo(chat_id= message.chat.id, photo=open('code.png', 'rb'))


















executor.start_polling(dp)
