import telebot

bot = telebot.TeleBot('5795742813:AAEIHh9vx-gkPXsfwcSXsi-D9LHufMzaXvQ')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет, что хочешь узнать?)')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'Извини, что вышло недопонимание, вот тебе ссылочка чтобы тебе легче было работать с нашим ботом https://www.youtube.com/watch?v=H3StRyjtM4A&ab_channel=videoknopka.ru ', parse_mode='html')

bot.polling(none_stop=True)