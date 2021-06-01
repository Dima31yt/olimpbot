import csv
import io
import urllib.request
import telebot
from telebot import TeleBot
from telebot import types

print("Запуск...")
print("Запуск Функций")

try:

    def wrdict (num, dict):
        a_dict.update({str(num): dict})

    url = 'https://docs.google.com/spreadsheets/d/1vqsYnAkVX-d0uwTVngZoAopepuSsFMd7eiigh885ArQ/export?format=csv'

    response = urllib.request.urlopen(url)

    a_dict = {}

    a = 0 #0
    a1 = 0 #0

    with io.TextIOWrapper(response, encoding='utf-8') as f:
        reader = csv.reader(f)

        for row in reader:
            if a1 > 3:
                wrdict(a, row)
                a += 1
            
            a1 += 1

    def rdict (strict, clm):
        return a_dict[str(strict)][int(clm)]


    def senda (num_s):
        num = int(num_s) - 1
        a_return = "ФИО: " + rdict(num, 0) + "\nДолжность: " + rdict(num, 1) + "\nE-mail: " + rdict(num, 2) + "\nID: " + rdict(num, 3)
        return a_return

except Exception as e:
    print("ERROR|При запуске функций произошла ошибка. Текст ошибки:\n" + str(e))

else:
    print("Успешно")


print("Запуск Telegram Bot")
token = "1574949421:AAEbVeRrchsiV-SDhJZPjUKvrgz7iGTTPdA"
bot = telebot.TeleBot(token)

invise = {"a": 0}
invise_call = {"a": 0}

@bot.message_handler(commands=['start', 'help'])  
def help_command(message):
    #Группа A
    main_keyboard_A = telebot.types.InlineKeyboardMarkup()  
    main_keyboard11 = (telebot.types.InlineKeyboardButton("A01", callback_data='A01'))
    main_keyboard12 = (telebot.types.InlineKeyboardButton("A02", callback_data='A02'))
    main_keyboard13 = (telebot.types.InlineKeyboardButton("A03", callback_data='A03'))
    main_keyboard_A.add(main_keyboard11, main_keyboard12, main_keyboard13)
    main_keyboard21 = (telebot.types.InlineKeyboardButton("A04", callback_data='A04'))
    main_keyboard22 = (telebot.types.InlineKeyboardButton("A05", callback_data='A05'))
    main_keyboard23 = (telebot.types.InlineKeyboardButton("A06", callback_data='A06'))
    main_keyboard_A.add(main_keyboard21, main_keyboard22, main_keyboard23)
    main_keyboard31 = (telebot.types.InlineKeyboardButton("A07", callback_data='A07'))
    main_keyboard32 = (telebot.types.InlineKeyboardButton("A08", callback_data='A08'))
    main_keyboard33 = (telebot.types.InlineKeyboardButton("A09", callback_data='A09'))
    main_keyboard_A.add(main_keyboard31, main_keyboard32, main_keyboard33)
    main_keyboard_A.add(telebot.types.InlineKeyboardButton("A10", callback_data='A10'))
    invise["a"] += 1
    key_up = (telebot.types.InlineKeyboardButton("Вперед -->", callback_data='UP'))
    main_keyboard_A.add(key_up)
    if message.chat.id == 1024861899:
        main_keyboard_A.add(telebot.types.InlineKeyboardButton("Отчет о пользователях", callback_data='new'))

    user = message.from_user.first_name
    bot.send_message(  
        message.chat.id,  
        'Привет ' + user + '!\nЗдесь представлен список активистов, задействованых в 1 смене лагеря "Олимп"',
        reply_markup=main_keyboard_A
    )


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            invise_call["a"] += 1
            if call.data == "A01":
                bot.send_message(call.message.chat.id, senda(1))
            if call.data == "A02":
                bot.send_message(call.message.chat.id, senda(2))
            if call.data == "A03":
                bot.send_message(call.message.chat.id, senda(3))
            if call.data == "A04":
                bot.send_message(call.message.chat.id, senda(4))
            if call.data == "A05":
                bot.send_message(call.message.chat.id, senda(5))
            if call.data == "A06":
                bot.send_message(call.message.chat.id, senda(6))
            if call.data == "A07":
                bot.send_message(call.message.chat.id, senda(7))
            if call.data == "A08":
                bot.send_message(call.message.chat.id, senda(8))
            if call.data == "A09":
                bot.send_message(call.message.chat.id, senda(9))
            if call.data == "A10":
                bot.send_message(call.message.chat.id, senda(10))
            
            if call.data == "B11":
                bot.send_message(call.message.chat.id, senda(11))
            if call.data == "B12":
                bot.send_message(call.message.chat.id, senda(12))
            if call.data == "B13":
                bot.send_message(call.message.chat.id, senda(13))
            if call.data == "B14":
                bot.send_message(call.message.chat.id, senda(14))
            if call.data == "B15":
                bot.send_message(call.message.chat.id, senda(15))
            if call.data == "B16":
                bot.send_message(call.message.chat.id, senda(16))
            if call.data == "B17":
                bot.send_message(call.message.chat.id, senda(17))
            if call.data == "B18":
                bot.send_message(call.message.chat.id, senda(18))
            if call.data == "B19":
                bot.send_message(call.message.chat.id, senda(19))
            if call.data == "B20":
                bot.send_message(call.message.chat.id, senda(20))


            if call.data == "UP":
                #Группа B
                main_keyboard_B = telebot.types.InlineKeyboardMarkup()
                main_keyboard11 = (telebot.types.InlineKeyboardButton("B11", callback_data='B11'))
                main_keyboard12 = (telebot.types.InlineKeyboardButton("B12", callback_data='B12'))
                main_keyboard13 = (telebot.types.InlineKeyboardButton("B13", callback_data='B13'))
                main_keyboard_B.add(main_keyboard11, main_keyboard12, main_keyboard13)
                main_keyboard21 = (telebot.types.InlineKeyboardButton("B14", callback_data='B14'))
                main_keyboard22 = (telebot.types.InlineKeyboardButton("B15", callback_data='B15'))
                main_keyboard23 = (telebot.types.InlineKeyboardButton("B16", callback_data='B16'))
                main_keyboard_B.add(main_keyboard21, main_keyboard22, main_keyboard23)
                main_keyboard31 = (telebot.types.InlineKeyboardButton("B17", callback_data='B17'))
                #main_keyboard32 = (telebot.types.InlineKeyboardButton("B18", callback_data='B18'))
                #main_keyboard33 = (telebot.types.InlineKeyboardButton("B19", callback_data='B19'))
                main_keyboard_B.add(main_keyboard31) #, main_keyboard32, main_keyboard33
                #main_keyboard_B.add(telebot.types.InlineKeyboardButton("B20", callback_data='B20'))
                key_back = (telebot.types.InlineKeyboardButton("<-- Назад", callback_data='BACK'))
                code = (telebot.types.InlineKeyboardButton("🖥", callback_data='code_member'))
                main_keyboard_B.add(key_back, code)
                main_keyboard_B.add(telebot.types.InlineKeyboardButton("Сообщить об ошибке", callback_data='error'))

                bot.send_message(call.message.chat.id, "Открыт список Бета", reply_markup=main_keyboard_B)
            
            if call.data == "BACK":
                #Группа A
                main_keyboard_A = telebot.types.InlineKeyboardMarkup()  
                main_keyboard11 = (telebot.types.InlineKeyboardButton("A01", callback_data='A01'))
                main_keyboard12 = (telebot.types.InlineKeyboardButton("A02", callback_data='A02'))
                main_keyboard13 = (telebot.types.InlineKeyboardButton("A03", callback_data='A03'))
                main_keyboard_A.add(main_keyboard11, main_keyboard12, main_keyboard13)
                main_keyboard21 = (telebot.types.InlineKeyboardButton("A04", callback_data='A04'))
                main_keyboard22 = (telebot.types.InlineKeyboardButton("A05", callback_data='A05'))
                main_keyboard23 = (telebot.types.InlineKeyboardButton("A06", callback_data='A06'))
                main_keyboard_A.add(main_keyboard21, main_keyboard22, main_keyboard23)
                main_keyboard31 = (telebot.types.InlineKeyboardButton("A07", callback_data='A07'))
                main_keyboard32 = (telebot.types.InlineKeyboardButton("A08", callback_data='A08'))
                main_keyboard33 = (telebot.types.InlineKeyboardButton("A09", callback_data='A09'))
                main_keyboard_A.add(main_keyboard31, main_keyboard32, main_keyboard33)
                main_keyboard_A.add(telebot.types.InlineKeyboardButton("A10", callback_data='A10'))

                key_up = (telebot.types.InlineKeyboardButton("Вперед -->", callback_data='UP'))
                main_keyboard_A.add(key_up)

                bot.send_message(call.message.chat.id, "Открыт список Альфа", reply_markup=main_keyboard_A)

            if call.data == "code_member":
                key_back = (telebot.types.InlineKeyboardButton("<-- Назад", callback_data='BACK'))

                bot.send_message(call.message.chat.id, "Бота напиисал:\nДмитрий\nVk: vk.com/maaaasyyyniiik\nTg: @maaaasyyyniiiik", reply_markup=key_back)

            if call.data == "error":
                error_key = telebot.types.InlineKeyboardMarkup()  
                error_key.add(telebot.types.InlineKeyboardButton("Неверное отображение данных", callback_data='error1'))
                error_key.add(telebot.types.InlineKeyboardButton("Несоответствие данных с действительностью", callback_data='error2'))
                error_key.add(telebot.types.InlineKeyboardButton("Устаревшие данные", callback_data='error3'))
                error_key.add(telebot.types.InlineKeyboardButton("Другая причина", callback_data='error4'))
                error_key.add(telebot.types.InlineKeyboardButton("Назад", callback_data='UP'))

                bot.send_message(call.message.chat.id, "В чем именно заключается ошибка?", reply_markup=error_key)
            
            if call.data == "error1":
                key_back = (telebot.types.InlineKeyboardButton("Назад", callback_data='UP'))
                bot.send_message(call.message.chat.id, "Отчет об ошибке:\nПричина: Неверное отображение данных\nВаша заявка будет рассмотрена нашими администраторами", reply_markup=key_back)
                user_id = call.message.chat.id
                bot.send_message(1024861899, "Отчет об ошибке:\nПричина: Неверное отображение данных\nОтправитель: @" + str(user_id))
                bot.send_message(1356201546, "Отчет об ошибке:\nПричина: Неверное отображение данных\nОтправитель: @" + str(user_id))
            if call.data == "error2":
                key_back = (telebot.types.InlineKeyboardButton("Назад", callback_data='UP'))
                bot.send_message(call.message.chat.id, "Отчет об ошибке:\nПричина: Несоответствие данных с действительностью\nВаша заявка будет рассмотрена нашими администраторами", reply_markup=key_back)
                user_id = call.message.chat.id
                bot.send_message(1024861899, "Отчет об ошибке:\nПричина: Несоответствие данных с действительностью\nОтправитель: @" + str(user_id))
                bot.send_message(1356201546, "Отчет об ошибке:\nПричина: Неверное отображение данных\nОтправитель: @" + str(user_id))
            if call.data == "error3":
                key_back = (telebot.types.InlineKeyboardButton("Назад", callback_data='UP'))
                bot.send_message(call.message.chat.id, "Отчет об ошибке:\nПричина: Устаревшие данные\nВаша заявка будет рассмотрена нашими администраторами", reply_markup=key_back)
                user_id = call.message.chat.id
                bot.send_message(1024861899, "Отчет об ошибке:\nПричина: Устаревшие данные\nОтправитель: @" + str(user_id))
                bot.send_message(1356201546, "Отчет об ошибке:\nПричина: Неверное отображение данных\nОтправитель: @" + str(user_id))
            if call.data == "error4":
                key_back = (telebot.types.InlineKeyboardButton("Назад", callback_data='UP'))
                bot.send_message(call.message.chat.id, "Отчет об ошибке:\nПричина: Другая причина\nВаша заявка будет рассмотрена нашими администраторами", reply_markup=key_back)
                user_id = call.message.chat.username
                bot.send_message(1024861899, "Отчет об ошибке:\nПричина: Другая причина\nОтправитель: @" + str(user_id))
                bot.send_message(1356201546, "Отчет об ошибке:\nПричина: Неверное отображение данных\nОтправитель: @" + str(user_id))
            


            if call.data == "new":
                bot.send_message(call.message.chat.id, "Очтет за сегодня:\nНовых пользователей: " + str(invise["a"]) + "\nВоспользовались callback меню: " + str(invise_call["a"]))

    except Exception as e:
        print(e)
        print("\n \n \n \n \n")
        print(repr(e))
        bot.send_message(1024861899, str(e))
        bot.send_message(1356201546, str(e))

print("Успешно")
print("polling...")
bot.polling(none_stop=True)