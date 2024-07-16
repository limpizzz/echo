import telebot
token = '6812961601:AAHFTqSQ88_bDw4rCTYknURlKQvSAI7Muaw'
bot = telebot.TeleBot(token)
@bot.message_handler(content_types=['text'])
def repeat(message):
    bot.send_message(message.chat.id, message.text)
bot.polling()