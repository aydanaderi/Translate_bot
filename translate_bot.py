from langdetect import detect
from mtranslate import translate
import telepot
import time

bot = telepot.Bot('TOKEN')
def handle(msg):
    content_type,chat_type,chat_id = telepot.glance(msg)
    if content_type == 'text':
        text = msg['text']
        if text == '/start':
            bot.sendMessage(chat_id,'hi! welcom to translate bot! you can send /help to understand how to use this bot')
        elif text == '/help':
            bot.sendMessage(chat_id,'send your string for translating :')
        else :
            if detect(text) == 'en' :
               translated = translate(text,'fa','en')
               bot.sendMessage(chat_id, translated)
            elif detect(text) == 'fa' :
               translated = translate(text, 'en', 'fa')
               bot.sendMessage(chat_id, translated)
            else :
                bot.sendMessage(chat_id,'that is wrong!')
    else:
         bot.sendMessage(chat_id, 'your content type is wrong!')
bot.message_loop(handle)
print ('Listening ...')
while 1:
    time.sleep(30)
