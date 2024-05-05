import telebot
import random

a = """
Это бот который будет играть с тобой в камень, ножницы, бумага
Нажми /scissors чтобы показать ножницы
Нажми /rock чтобы показать камень
Нажми /paper чтобы показать бумагу
"""
b = """
Бумага побеждает камень («бумага обёртывает камень»)
Камень побеждает ножницы («камень затупляет ножницы»)
Ножницы побеждают бумагу («ножницы разрезают бумагу»)
Если игроки показали одинаковый знак, то засчитывается ничья и игра переигрывается
За каждую победу тебе начисляется один point
А за каждое поражение начисляется твоему врагу
Так же за ничью никто не получает point
После игры, на экран выводится число побед:
Слева ваши - справа компуктера
""" 
e = """
Добро пожаловать пользователеь это игра камень, ножницы, бумага
Для начала срочно нажми на это: /accaunt
Если ты не нажмёшь на него то у тебя ничего не будет работать!!!
""" 
u = "Если ты хочешь начать заново то нажми сюда: /clear_accaunt"
h = "Рады видеть вас снова"
m = "Щедрин Михаил Сергеевич ЛОХ ХААААААААААХАХАХАХАХАХХАХАХАХАХАХАХАХХА"

i_d = [0]
user = [[0, 0]]

ritm = 0

doesntwin = "Вы проиграли"
draw = "Ничья"
win = "!!!Вы выиграли!!!"

ro = " бот поставил камень"
si = " бот поставил ножницы"
pa = " бот поставил бумагу"

token = "6429473773:AAEPlPr4Oy88dJertcJVGKoYSqZxGry5HUc"
bot = telebot.TeleBot(token)


c = ["ножницы", "камень", "бумага"]
d = random.choice(c)

@bot.message_handler(commands=['start'])
def start(message):
    global ritm, i_d, user
    ritm = 0
    for i in i_d:
      if i == message.from_user.id :
          bot.send_message(message.from_user.id, u)
          bot.send_message(message.from_user.id, h)
          break
      if ritm == len(i_d):
          i_d.append(message.from_user.id )
          user.append([0, 0])
          bot.send_message(message.from_user.id, e)
          break
      ritm+=1
    

@bot.message_handler(commands=['clear_accaunt'])
def start(message):
    global a
    i_d.pop(len(i_d)-1)
    user.pop(len(user)-1)
    i_d.append(message.from_user.id )
    user.append([0, 0])
    bot.send_message(message.from_user.id, h)

@bot.message_handler(commands=['misha'])
def start(message):
    global a
    bot.send_message(message.from_user.id, m)


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
        bot.send_message(message.from_user.id, doesntwin+si)
        user[ritm][1] +=1
    elif d == "камень":
        bot.send_message(message.from_user.id, win+ro)
        user[ritm][0] +=1
    elif d == "бумага":
        bot.send_message(message.from_user.id, draw+pa)
    d = random.choice(c)
    bot.send_message(message.from_user.id, str(user[ritm][0])+" - "+str(user[ritm][1]))


@bot.message_handler(commands=['scissors'])
def start(message):
    global d, c, ritm, user
    if d == "ножницы":
        bot.send_message(message.from_user.id, draw+si)
    elif d == "камень":
        bot.send_message(message.from_user.id, doesntwin+ro)
        user[ritm][1] +=1
    elif d == "бумага":
        bot.send_message(message.from_user.id, win+pa)
        user[ritm][0] +=1
    d = random.choice(c)
    bot.send_message(message.from_user.id, str(user[ritm][0])+" - "+str(user[ritm][1]))

@bot.message_handler(commands=['rock'])
def start(message):
    global d, c, ritm, user
    if d == "ножницы":
        bot.send_message(message.from_user.id, win+si)
        user[ritm][0] +=1
    elif d == "камень":
        bot.send_message(message.from_user.id, draw+ro)
    elif d == "бумага":
        bot.send_message(message.from_user.id, doesntwin+pa)
        user[ritm][1] +=1
    d = random.choice(c)
    bot.send_message(message.from_user.id, str(user[ritm][0])+" - "+str(user[ritm][1]))




bot.polling(none_stop=True, interval=0, timeout=120)