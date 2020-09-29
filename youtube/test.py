from config_tlg import token_tlg, chanel_id

import traceback
import telebot
import time

bot = telebot.TeleBot(token_tlg, threaded=False)

bot.send_message(chanel_id, 'Привет!')

if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)

        except Exception as e:
            traceback.print_exc()
            time.sleep(5)