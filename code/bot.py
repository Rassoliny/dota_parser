from constants import TELE_TOKEN
import telebot


bot = telebot.TeleBot(TELE_TOKEN)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
