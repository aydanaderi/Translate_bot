from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
from mtranslate import translate
import telepot
import time

bot = telepot.Bot('Token')

def handle(msg):
    content_type,chat_type,chat_id = telepot.glance(msg)
    if content_type == 'text':
        text = msg['text']
        if text == '/start' :
            bot.sendMessage(chat_id,'hi! welcom to translate bot! you can send /help to understand how to use this bot')
        if text == '/help':
           keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text = "English"), KeyboardButton(text = "Persion")]])
           bot.sendMessage(chat_id, 'select your string language :', reply_markup = keyboard)
    else :
        bot.sendMessage(chat_id,'your content type is wrong!')
def main(msg):
    chat_id = telepot.glance(msg)
    bot.sendMessage(chat_id, 'please send your string :')
    text = msg['text']
    if text == 'English':
        translated = translate(text, 'fa', 'en')
        bot.sendMessage(chat_id, translated)
    if text == 'Persion':
        translated = translate(text, 'en', 'fa')
        bot.sendMessage(chat_id, translated)

bot.message_loop(handle)
print ('Listening ...')
while 1:
    time.sleep(20)
