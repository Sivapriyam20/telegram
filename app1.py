from telegram.ext import Updater, MessageHandler,Filters
from Adafruit_IO import Client
import  os
aio = Client('sivapriya20',os.getenv('siva'))
def turn_on_light(bot,update):
    aio.send('bedroom-light',1)
    data = aio.receive('bedroom-light')
    print(f'Received value:{data.value}')
    chat_id=bot.message.chat_id
    path='https%3A%2F%2Fscience4fun.info%2Fwp-content%2Fuploads%2F2016%2F12%2FLight-Bulb-1.jpg'
    bot.message.reply_text('light is turned on')
    update.bot.sendPhoto(chat_id=chat_id,photo=path)
def turn_off_light(bot,update):
    aio.send('bedroom-light',0)
    data = aio.receive('bedroom-light')
    print(f'Received value:{data.value}')
    chat_id=bot.message.chat_id
    path='https%3A%2F%2Fcdn.pixabay.com%2Fphoto%2F2020%2F06%2F03%2F14%2F28%2Flight-5255121_960_720.jpg'
    bot.message.reply_text('light is turned off')
    update.bot.sendPhoto(chat_id=chat_id,photo=path)
def turn_on_fan(bot,update):
    aio.send('fan',1)
    data = aio.receive('fan')
    print(f'Received value:{data.value}')
    chat_id=bot.message.chat_id
    path='https%3A%2F%2Fcdn.frontdoorhome.com%2Fahs%2Fblog%2Fprod%2Fstatic%2Fcs%2Fahs%2Fimage%2Frunning-fan.jpg'
    bot.message.reply_text('fan is turned on')
    update.bot.sendPhoto(chat_id=chat_id,photo=path)
def turn_off_fan(bot,update):
    aio.send('fan',0)
    data = aio.receive('fan')
    print(f'Received value:{data.value}')
    chat_id=bot.message.chat_id
    path='https%3A%2F%2Fitg.wfu.edu%2Fwp-content%2Fuploads%2FCeilingFan-300x157.jpg'
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


