import telebot
import random

bot = telebot.TeleBot("1930222233:AAFQhJyMxFDrS3z3xCXaH4fTHM5tR1dwLVc")
film = []

file = open("movies.txt")
for i in file:
    film.append(i.rstrip())


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "Привет, напиши мне что нибудь и я тебе cгенерирую фильм")

@bot.message_handler(content_types=["text"])
def request(message):
    request_message = "хорошего просмотра\n" + film[random.randint(0, len(film)-1)]
    bot.send_message(message.chat.id, request_message)


bot.polling(none_stop=True)