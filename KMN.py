import telebot
import random

a = """
Это бот который будет играть с тобой в камень ножницы бумага
Отправь или нажми на кнопку /ножницы чтобы покозать ножницы
Отправь или нажми на кнопку /камень чтобы покозать камень
Отправь или нажми на кнопку /бумага чтобы покозать бумагу
"""
b = """
Бумага побеждает камень («бумага обёртывает камень»)
Камень побеждает ножницы («камень затупляет ножницы»)
Ножницы побеждают бумагу («ножницы разрезают бумагу»)
Если игроки показали одинаковый знак, то засчитывается ничья и игра переигрывается
За каждую победу тебе начисляется один поинт
А за каждое порожение твоему врагу
Так же за ничью никто не получает поинтов
После игры на экран выводится число побед с лева ваши а с права компютера
"""  

i_d = []
user = []

ritm = 0

doesntwin = "Вы проиграли"
draw = "Ничья"
win = "Вы выиграли!!!"

ro = "бот поставил камень"
si = "бот поставил ножницы"
pa = "бот поставил бумагу"

token = "6429473773:AAEPlPr4Oy88dJertcJVGKoYSqZxGry5HUc"
bot = telebot.TeleBot(token)

c = ["ножницы", "камень", "бумага"]
d = random.choice(c)

@bot.message_handler(commands=['start'])
def start(message):
  global i_d, count, ritm
  ritm = 0
  for i in i_d:
    if i == message.chat.id:
        break
    if ritm == len(i_d):
        i_d.append(message.chat.id)
        user.append([0, 0])
        break
    ritm+=1
  

@bot.message_handler(commands=['help'])
def start(message):
    global a
    bot.send_message(message.from_user.id, a)

@bot.message_handler(commands=['rules'])
def start(message):
    global b
    bot.send_message(message.from_user.id, b)

@bot.message_handler(commands=['paper'])
def start(message):
    global d, c, ritm, user
    if d == "ножницы":
        bot.send_message(message.from_user.id, doesntwin, si)
        user[ritm][1] +=1
    elif d == "камень":
        bot.send_message(message.from_user.id, win, ro)
        user[ritm][0] +=1
    elif d == "бумага":
        bot.send_message(message.from_user.id, draw, pa)
    d = random.choice(c)
    bot.send_message(message.from_user.id, user[ritm][0], user[ritm][1])


@bot.message_handler(commands=['scissors'])
def start(message):
    global d, c, ritm, user
    if d == "ножницы":
        bot.send_message(message.from_user.id, draw, si)
    elif d == "камень":
        bot.send_message(message.from_user.id, doesntwin, ro)
        user[ritm][1] +=1
    elif d == "бумага":
        bot.send_message(message.from_user.id, win, pa)
        user[ritm][0] +=1
    d = random.choice(c)
    bot.send_message(message.from_user.id, user[ritm][0], user[ritm][1])

@bot.message_handler(commands=['rock'])
def start(message):
    global d, c, ritm, user
    if d == "":
        bot.send_message(message.from_user.id, win, si)
        user[ritm][0] +=1
    elif d == "камень":
        bot.send_message(message.from_user.id, draw, ro)
    elif d == "бумага":
        bot.send_message(message.from_user.id, doesntwin, pa)
        user[ritm][1] +=1
    d = random.choice(c)
    bot.send_message(message.from_user.id, user[ritm][0], user[ritm][1])




bot.polling(none_stop=True, interval=0, timeout=120)
