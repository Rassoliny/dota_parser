from constants import TELE_TOKEN, CHANNEL_ID
import telebot


bot = telebot.TeleBot(TELE_TOKEN)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(CHANNEL_ID, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
