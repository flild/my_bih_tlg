from config_tlg import token_tlg, my_id, chanel_id
from telebot import types
from youtube.youtube import YouTube_downloader
from parser_for_alpaca.parser import hen_parser

import traceback
import telebot
import time
import os

bot = telebot.TeleBot(token_tlg, threaded=False)
inf_dict = {}
danger_tag ={'футанари','футанари имеет парня','shemale'}

# main kb with func
def keyboard_main():
    main_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    parse_btn = types.KeyboardButton('pars_alpaca')
    main_kb.add(parse_btn)
    return main_kb


# button click handler
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    pass


# listening server
@bot.message_handler(content_types=['text'])
# main cmds
def start(message):
    global inf_dict
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
    elif message.text.startswith('https://telegra.ph'):
        tags = ''
        result = list(set(inf_dict['tag']) & danger_tag)
        if result == []:
            result = inf_dict['tag']
        else:
            for el in result:
                tags = tags + f'<b>#{el.upper().replace(" ","_")}</b> '
            result = list(set(inf_dict['tag'])-set(result))
        for i in result:
            tags = tags + f"#{i.replace(' ','_')} "

        bot.send_message(chanel_id, f'<a href="{message.text}">{inf_dict["name"]}</a>\n'
                                    f'Теги: \n{tags}\n'
                                    f'Автор: #{inf_dict["author"].replace(" ","_")}\n'
                                    f'Переводчик: #{inf_dict["translator"].replace(" ","_")}\n'
                                    f'Страниц: {inf_dict["str_count"]}', parse_mode="HTML")
    elif message.text == 'pars_alpaca':
        inf_dict = hen_parser()
        print(inf_dict)
        with open('last_request.txt', 'w') as f:
            f.write(str(inf_dict))
        bot.send_message(my_id, str(inf_dict))
    elif message.text.startswith('https://hentai-chan.pro/manga/'):
        inf_dict = hen_parser(message.text)
        print(inf_dict)
        with open('last_request.txt', 'w') as f:
            f.write(str(inf_dict))
        bot.send_message(my_id, str(inf_dict))

        


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)

        except Exception as e:
            traceback.print_exc()
            time.sleep(5)
