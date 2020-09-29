from config_tlg import token_tlg
from telebot import types
from youtube.youtube import YouTube_downloader

import traceback
import telebot
import time
import os

bot = telebot.TeleBot(token_tlg, threaded=False)


# main kb with func
def keyboard_main():
    main_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    post_btn = types.KeyboardButton('post_alpaca')
    main_kb.add(post_btn)
    return main_kb


# button click handler
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    pass


# listening server
@bot.message_handler(content_types=['text'])
# main cmds
def start(message):
    if message.text == '/start':
        bot.send_message(message.chat.id,
                         """ 
                         пришли мне ссылку на видео, и я его скачаю, ну или кнопочки потыкай
                         """, reply_markup=keyboard_main())
    elif 'https://youtu.be/' in message.text:
        loader = YouTube_downloader(message.text)
        title = loader.download_video(message.text)
        bot.send_document(message.chat.id, data=open(f'{title}.mp4', 'rb'))
        os.remove(f'{title}.mp4')
    elif message.text == 'post_alpaca':
        


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)

        except Exception as e:
            traceback.print_exc()
            time.sleep(5)
