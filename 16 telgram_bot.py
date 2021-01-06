import telebot
from myToken import TOKEN
from random import randint, choice, shuffle

bot = telebot.TeleBot(TOKEN)  # Создаём подключение к боту

isGame = False #Идёт игра словомеска или нет

word = None

@bot.message_handler(commands=['start'])
def komanda_start(message):
    bot.send_message(message.chat.id, "Я умею много разного, например текстовые сообщения я разворачиваю задом наперёд")


@bot.message_handler(commands=['pass'])
def komanda_pass(message):
    bot.send_message(message.chat.id, "Я сгенерирую тебе пароль из 4х цифр")
    rand_number = randint(1000, 9999)
    bot.send_message(message.chat.id, str(rand_number))



@bot.message_handler(commands=['game'])
def komanda_game(message):
    words = ['антарктида', 'амплитуда', 'локомотив', 'индустриализация', 'процессор']
    global word
    word = choice(words).lower()

    shuffle_word = list(word)
    shuffle(shuffle_word)

    bot.send_message(message.chat.id,
                     "Я загадал слово и перемшал в нём буквы, попробуй угадать: " + ''.join(shuffle_word))
    global isGame
    isGame = True


@bot.message_handler(content_types=['text'])
def otvet_na_text(message):
    print(message)
    global isGame
    if isGame:
        if message.text == word:
            bot.send_message(message.chat.id, "угадал")
            isGame = False
        else:
            bot.send_message(message.chat.id, "не угадал")

    else:
        bot.send_message(message.chat.id, message.text[::-1])
    # bot.send_message(message.chat.id, "Hello")


bot.polling()  # Забираем сообщения у бота
