from config_tlg import token_tlg
from telebot import types
from youtube.youtube import YouTube_downloader

import traceback
import telebot
import time
import os

bot = telebot.TeleBot(token_tlg, threaded=False)

# listening server
@bot.message_handler(content_types=['text'])
# main cmds
def start(message):

    if message.text == '/start':
        bot.send_message(message.chat.id,
                         """ 
                         пришли мне ссылку на видео, и я его скачаю
                         """, )
    if 'https://youtu.be/' in message.text:
        loader = YouTube_downloader(message.text)
        title = loader.download_video(message.text)
        bot.send_document(message.chat.id, data=open(f'{title}.mp4', 'rb'))
        os.remove(f'{title}.mp4')




if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)

        except Exception as e:
            traceback.print_exc()
            time.sleep(5)