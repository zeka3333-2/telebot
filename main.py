#!venv/bin/python

import traceback
import telebot
import time

bot = telebot.TeleBot'(8221610205:AAFyE9l7MXBNQMZbAOe3tkrjIFfSSnbnll0')
ADMIN_ID = @CashFlow_Dnepr_bot
def main():
    try:
        @bot.message_handler(commands=['start'])
        def start(message):
            bot.send_message(message.chat.id, "Bot rabotae!")t
        bot.polling(none_stop=True)
    except Exception as e:
        error_msg = f"Bot upal!\n\nOshibka:\n{traceback.format_exc()}"
        print(error_msg) 
        try:
            bot.send_message(ADMIN_ID, error_msg)
        except:
            pass 
        time.sleep(5) 
if __name__ == '__main__':
    main()



