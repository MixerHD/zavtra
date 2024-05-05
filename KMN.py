import telebot
import random

a = """
Это бот, который будет играть с тобой в камень ножницы бумага
Нажми /scissors чтобы показать ножницы
Нажми /rock чтобы показать камень
Нажми /paper чтобы показать бумагу
"""
b = """
Бумага побеждает камень («бумага обёртывает камень»)
Камень побеждает ножницы («камень затупляет ножницы»)
Ножницы побеждают бумагу («ножницы разрезают бумагу»)
Если игроки показали одинаковый знак, то засчитывается ничья и игра переигрывается
За каждую победу тебе начисляется один очков
А за каждое поражение твоему врагу
Так же за ничью никто не получает очков
После игры, на экран выводится число побед:
слева ваши - справа компьютера
""" 
e = """
Добро пожаловать пользователь это игра камень ножницы бумага!!!
Для начала срочно нажми на это
Если ты не нажмёшь на него то у тебя ничего не будет работать
""" 
u = "Если ты хочешь начать заново то нажми сюда: /clear_accaunt"
h = "Рады видеть вас снова"


user = {0:[0, 0]}



doesntwin = "Вы проиграли"
draw = "Ничья"
win = "Вы выиграли!!!"

ro = " бот поставил камень"
si = " бот поставил ножницы"
pa = " бот поставил бумагу"

token = "6429473773:AAEPlPr4Oy88dJertcJVGKoYSqZxGry5HUc"
bot = telebot.TeleBot(token)


c = ["ножницы", "камень", "бумага"]
d = random.choice(c)

@bot.message_handler(commands=['start'])
def start(message):
    global ritm, i_d, user, u, h, e
    ritm = 0
    if message.from_user.id in user.keys():
        bot.send_message(message.from_user.id, u)
        bot.send_message(message.from_user.id, h)
    else:
        i_d.append(message.from_user.id)
        user.append([0, 0])
        bot.send_message(message.from_user.id, e)
    

@bot.message_handler(commands=['clear_accaunt'])
def start(message):
    global a
    user[message.from_user.id] = [0, 0]
    bot.send_message(message.from_user.id, h)

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
    global d, c, user
    if d == "ножницы":
        bot.send_message(message.from_user.id, doesntwin+si)
        user[message.from_user.id][1]+=1
    elif d == "камень":
        bot.send_message(message.from_user.id, win+ro)
        user[message.from_user.id][0] +=1
    elif d == "бумага":
        bot.send_message(message.from_user.id, draw+pa)
    d = random.choice(c)
    bot.send_message(message.from_user.id, str(user[message.from_user.id][0])+" - "+str(user[message.from_user.id][1]))


@bot.message_handler(commands=['scissors'])
def start(message):
    global d, c, user
    if d == "ножницы":
        bot.send_message(message.from_user.id, draw+si)
    elif d == "камень":
        bot.send_message(message.from_user.id, doesntwin+ro)
        user[message.from_user.id][1]+=1
    elif d == "бумага":
        bot.send_message(message.from_user.id, win+pa)
        user[message.from_user.id][0] +=1
    d = random.choice(c)
    bot.send_message(message.from_user.id, str(user[message.from_user.id][0])+" - "+str(user[message.from_user.id][1]))

@bot.message_handler(commands=['rock'])
def start(message):
    global d, c, user
    if d == "ножницы":
        bot.send_message(message.from_user.id, win+si)
        user[message.from_user.id][0] +=1
    elif d == "камень":
        bot.send_message(message.from_user.id, draw+ro)
    elif d == "бумага":
        bot.send_message(message.from_user.id, doesntwin+pa)
        user[message.from_user.id][1]+=1
    d = random.choice(c)
    bot.send_message(message.from_user.id, str(user[message.from_user.id][0])+" - "+str(user[message.from_user.id][1]))


bot.polling(none_stop=True, interval=0, timeout=120)