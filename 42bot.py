from telebot import TeleBot, types
from random import choice
bot = TeleBot('5608279736:AAFV3Q3tnwOA4vLxrg-MPzwHvVm2RMXREDw')
answer = ['Да', 'Очень вероятно', 'Безусловно', 'Без сомнений', 'Мне кажется да', 'Абсолютно нет', 'Нет', 'Не надейся']
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, choice(answer))

bot.polling(none_stop=True, interval=0)