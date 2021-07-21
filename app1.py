from telegram.ext import Updater, MessageHandler,Filters
from Adafruit_IO import Client
import  os
aio = Client('sivapriya20',os.getenv('siva'))
def turn_on_light(bot,update):
    aio.send('bedroom-light',1)
    data = aio.receive('bedroom-light')
    print(f'Received value:{data.value}')
    chat_id=bot.message.chat_id
    path='https://freedesignfile.com/upload/2018/04/Electric-light-bulb-vector-material.jpg'
    bot.message.reply_text('light is turned on')
    update.bot.sendPhoto(chat_id=chat_id,photo=path)
def turn_off_light(bot,update):
    aio.send('bedroom-light',0)
    data = aio.receive('bedroom-light')
    print(f'Received value:{data.value}')
    chat_id=bot.message.chat_id
    path='https://cdn5.vectorstock.com/i/1000x1000/70/44/3d-realistic-off-light-bulb-icon-closeup-vector-27407044.jpg'
    bot.message.reply_text('light is turned off')
    update.bot.sendPhoto(chat_id=chat_id,photo=path)
def turn_on_fan(bot,update):
    aio.send('fan',1)
    data = aio.receive('fan')
    print(f'Received value:{data.value}')
    chat_id=bot.message.chat_id
    path='https://pursolaraz.com/wp-content/uploads/2019/04/Depositphotos_1175497_l-2015-1080.jpg'
    bot.message.reply_text('fan is turned on')
    update.bot.sendPhoto(chat_id=chat_id,photo=path)
def turn_off_fan(bot,update):
    aio.send('fan',0)
    data = aio.receive('fan')
    print(f'Received value:{data.value}')
    chat_id=bot.message.chat_id
    path='https://5.imimg.com/data5/XS/MM/KF/SELLER-99661502/1200mm-electric-celling-fan-500x500.jpg'
    bot.message.reply_text('fan is turned off')
    update.bot.sendPhoto(chat_id=chat_id,photo=path)
def main(bot,update):
      a = bot.message.text
      print(a)

      if a=="turn on light":
        turn_on_light(bot,update)
      elif a=="turn off light" or a=="light off":
          turn_off_light(bot,update)
      elif a=="turn on fan":
          turn_on_fan(bot,update)
      elif a=="turn off fan" or a=="fan off":
          turn_off_fan(bot,update)
      else:
            bot.message.reply_text('invalid')

BOT_TOKEN = os.getenv('BOT_TOKEN')  
u = Updater(BOT_TOKEN,use_context = True) 
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main)) 
u.start_polling()
u.idle()


