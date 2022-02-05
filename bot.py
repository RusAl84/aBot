from webbrowser import get
import telebot;
from genAns import genAns 

bot = telebot.TeleBot('5111904045:AAG9BxwuCvNiHqvGSu1qx0bIp1rVlRRRQ');

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    splitted_text = str(message.text).lower().split()
    if str(message.text).lower() == "/help":
        bot.send_message(message.from_user.id, "Описание проекта ")
    else:
        bot.send_message(message.from_user.id, genAns(str(message.text).lower()))

bot.polling(none_stop=True, interval=0)