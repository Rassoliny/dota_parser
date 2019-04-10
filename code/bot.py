from constants import TELE_TOKEN
import telebot


bot = telebot.TeleBot(TELE_TOKEN)


@bot.message_handler(content_types=["text"])
def receive_message(message):
    """bot receive handler"""
    command = message.text[:3]
    skin_name = message.text[4:]

    if command == 'cls':
        # clean file
        with open('../data/withdrawal_list.txt', 'w'):
            pass
        answer = 'File was cleared'

    elif command == 'add':
        # new record to file
        with open('../data/withdrawal_list.txt', 'a') as f:
            f.write(skin_name + '\n')
        answer = '{} added to file'.format(skin_name)

    else:
        # no command received
        answer = 'Did you forget to send command?'

    # send answer to user
    bot.send_message(message.chat.id, answer)


if __name__ == '__main__':
    bot.polling(none_stop=True)
