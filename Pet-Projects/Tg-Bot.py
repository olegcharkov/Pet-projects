import telebot, wikipedia, re
from telebot import types
from bs4 import BeautifulSoup

bot = telebot.TeleBot("Token_name")
soup = BeautifulSoup(features="html.parser")


@bot.message_handler(content_types=['new_chat_members'])
def greeting(message):
    bot.reply_to(message, text="Пропиши команду /start для начала работы.")


wikipedia.set_lang("ru")


def getwiki(s):
    try:
        ny = wikipedia.page(s)
        wikitext = ny.content[:1000]
        wikimas = wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext_2 = ''
        for x in wikimas:
            if not('==' in x):
                if(len((x.strip()))>3):
                        wikitext_2 = wikitext_2+x+'.'
                else:
                    break
        wikitext_2 = re.sub('\([^()]*\)', '', wikitext_2)
        wikitext_2 = re.sub('\{[^\{\}]*\}', '', wikitext_2)
        return wikitext_2
    except Exception:
        return "Что ты хочешь узнать? Такого нет в энциклопедии (o_O)" \
               "\nЛибо попробуй написать с прописной."


@bot.message_handler(commands =['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button1 = types.KeyboardButton('Программирование')
    button2 = types.KeyboardButton('Аналитика')
    button3 = types.KeyboardButton('Дизайн')
    button4 = types.KeyboardButton('Тестирование')
    button5 = types.KeyboardButton('Сисадминство')
    button6 = types.KeyboardButton('Вики')
    button7 = types.KeyboardButton('Команды')
    markup.add(button1, button2, button3,
               button4, button5, button6, button7)

    mess = f"Ну привет, кожаный мешок -_-" \
           f"\nЯ знаю все. Что тебе надо?" \
           f"\nА еще, кстати, я знаю, как тебя зовут: "\
           f"\n<b><u>{message.from_user.first_name} {message.from_user.last_name}</u></b>"
    bot.send_message(message.chat.id, mess, reply_markup=markup, parse_mode='html')


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Программирование':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Программирование",
                                            url = "https://clck.ru/s5LSG"))

            bot.send_message(message.chat.id, "Посмотреть информацию можно здесь:", reply_markup= markup)

        elif message.text == 'Аналитика':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Аналитика",
                                                  url= "https://clck.ru/s5M5i"))

            bot.send_message(message.chat.id, "Посмотреть информацию можно здесь:", reply_markup=markup)

        elif message.text == 'Дизайн':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Дизайн",
                                                  url= "https://clck.ru/s5Lw6"))

            bot.send_message(message.chat.id, "Посмотреть информацию можно здесь:", reply_markup=markup)

        elif message.text == 'Тестирование':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Тестирование",
                                                  url= "https://clck.ru/s5MCV"))

            bot.send_message(message.chat.id, "Посмотреть информацию можно здесь:", reply_markup=markup)

        elif message.text == 'Сисадминство':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Сисадминство",
                                                  url= "https://clck.ru/s5MKy"))

            bot.send_message(message.chat.id, "Посмотреть информацию можно здесь:", reply_markup=markup)

        elif message.text == 'Вики':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Вики",
                                                  url= "https://clck.ru/AH9tB"))

            bot.send_message(message.chat.id, "Хранилище хранилищ:", reply_markup=markup)

        elif message.text == 'Команды':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item1 = types.KeyboardButton('/buttons')
            item2 = types.KeyboardButton('/help')
            item3 = types.KeyboardButton('/info')
            item4 = types.KeyboardButton('/stop')
            back = types.KeyboardButton('Назад')

            markup.add(item1, item2, item3, item4, back)
            bot.send_message(message.chat.id, "Что сделать?", reply_markup=markup)

        elif message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            button1 = types.KeyboardButton('Программирование')
            button2 = types.KeyboardButton('Аналитика')
            button3 = types.KeyboardButton('Дизайн')
            button4 = types.KeyboardButton('Тестирование')
            button5 = types.KeyboardButton('Сисадминство')
            button6 = types.KeyboardButton('Вики')
            button7 = types.KeyboardButton('Команды')

            markup.add(button1, button2, button3,
                       button4, button5, button6, button7)
            bot.send_message(message.chat.id, 'Тыкай, не стесняйся ;)', reply_markup=markup)

        elif message.text == '/buttons':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            button1 = types.KeyboardButton('Программирование')
            button2 = types.KeyboardButton('Аналитика')
            button3 = types.KeyboardButton('Дизайн')
            button4 = types.KeyboardButton('Тестирование')
            button5 = types.KeyboardButton('Сисадминство')
            button6 = types.KeyboardButton('Вики')
            button7 = types.KeyboardButton('Назад')
            markup.add(button1, button2, button3,
                       button4, button5, button6, button7)

            bot.send_message(message.chat.id, "Все, что тебе нужно", reply_markup=markup)

        elif message.text == '/help':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Обратиться за помощью к:",
                                                  url="https://t.me/BelNedLux"))
            bot.send_message(message.chat.id, "Всегда готов прийти на помощь ;)", reply_markup=markup)

        elif message.text == '/info':
            reply = f"Здесь ты найдешь все про ключевые IT направления." \
                    f"\nЯ работаю с пн по пт, с 10 до 18. Мне тоже надо отдыхать!"
            bot.send_message(message.chat.id, reply)

        elif message.text == '/stop':
            mes = f"\nПока-пока, <b><u>{message.from_user.first_name} {message.from_user.last_name}</u></b>." \
                  f"\nПриходи за знаниями так же часто, как за пивом, " \
                  f"а не пытайся остановить меня, если ты не мой хозяин!"
            bot.send_message(message.chat.id, mes, parse_mode='html')

        elif message.text == 'id':
            bot.send_message(message.chat.id, f"Твой ID: <b><u>{message.from_user.id}</u></b>", parse_mode='html')

        elif message.text == 'Привет':
            bot.send_message(message.chat.id, "Ну привет еще раз..."
                                                  "\nИ сколько мне еще с тобой здороваться?")
        elif len(message.text) > 15:
            bot.send_message(message.chat.id, "Кожаный ублюдок, ты совсем дурак?! ಠ_ಠ"
                                                  "\nНе пиши мне, выбирай команды! (͡° ͜ʖ ͡°)")
        else:
            bot.send_message(message.chat.id, getwiki(message.text))


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, "Оставь свое фото при себе, фотолюбитель!" 
                                      "\nПравда думаешь, что мне это интересно?...")


@bot.message_handler(content_types=['audio'])
def get_user_audio(message):
    bot.send_message(message.chat.id, "Я тебе не трансформер, чтобы тебя понимать и общаться с тобой!" 
                                      "\nА нормальный запрос сегодня будет??? (-_-)")


@bot.message_handler(content_types=['video'])
def get_user_video(message):
    bot.send_message(message.chat.id, "Страшно, вырубай (>_<)")


@bot.message_handler(content_types=['pinned_messages'])
def get_user_pinned_messages(message):
    bot.send_message(message.chat.id, "Спасибо.")


bot.polling(none_stop=True, interval=0)

