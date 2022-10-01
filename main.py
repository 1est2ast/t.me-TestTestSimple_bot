import telebot

bot = telebot.TeleBot('5736926408:AAHjJbhf7ZkDIIp8oiAMvBVOBDEjqhrAilQ')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == message.text:
        bot.send_message(message.from_user.id, message.text)

bot.polling(none_stop=True, interval=0)