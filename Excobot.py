import telebot

bot = telebot.TeleBot('6428179834:AAFfErHhTdJ39E1sg3vgKf7ZXDdPzJhJVHA')

@bot.message_handler(commands=['start'])
def handle_start(message):
  bot.reply_to(message, 'hello, i am echo bot')

@bot.message_handler(content_types=['text', 'photo', 'sticker'])
def handle_message(message):
  
  # Ответ на текстовое сообщение
  if message.text:
      bot.reply_to(message, 'your massage: ' + message.text)
  
  # Ответ на изображение
  if message.photo:
      bot.send_message(message.chat.id, 'you are send photo')
  
  # Ответ на стикер
  if message.sticker:
      bot.send_message(message.chat.id, 'you are send sticker')

bot.polling(non_stop = True)