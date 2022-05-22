#################Словари изменять только содержимое скобок####################
ukraine_lang = "абвгдеєжзиіїйклмнопрстуфхцчшщьюя"
english_lang = "abcdefghijklmnopqrstuvwxyz0123456789"
##############################################################################


uk_len = len(ukraine_lang)
en_len = len(english_lang)

def uk_shifr(yslovie):
    try:
        move = int(input("Шаг смещения : "))
    except ValueError:
        print("\n\n\n*******Выберите число а не символ*******\n\n\n")
        uk_shifr(yslovie)
    mess = input("Сообщение для шифра : ")
    finish_message = ''
    if yslovie == '+':
        for abc in mess.lower():
            number_in_kwargs = ukraine_lang.find(abc)
            shifr_mesto = number_in_kwargs + move
            uk_lent = uk_len-1
            if abc in ukraine_lang:
                if shifr_mesto >uk_lent:
                    shifr_mesto = shifr_mesto % uk_len
                    finish_message += ukraine_lang[shifr_mesto]
                else:
                    finish_message += ukraine_lang[shifr_mesto]
            else:
                finish_message += abc
        print('\n\nДлина словаря: {}\nВаше сообщение :{} \nКоличество шагов:{} \nВот шифровка вашего сообщения : {}'.format(uk_len,mess, move, finish_message))
    elif yslovie == '-':
        for abc in mess.lower():
            number_in_kwargs = ukraine_lang.find(abc)
            shifr_mesto = number_in_kwargs - move
            if abc in ukraine_lang:
                if shifr_mesto < 0:
                    shifr_mesto = shifr_mesto % uk_len
                    finish_message += ukraine_lang[shifr_mesto]
                else:
                    finish_message += ukraine_lang[shifr_mesto]
            else:
                finish_message += abc
        print('\n\nДлина словаря: {}\nВаше шифрованое сообщение :{} \nКоличество шагов:{} \nВот дешифровка вашего сообщения : {}'.format(uk_len,mess, move, finish_message))
    else:
        print("uncorrect")

def en_shifr(yslovie):
    try:
        move = int(input("Шаг смещения : "))
    except ValueError:
        print("\n\n\n*******Выберите число а не символ*******\n\n\n")
        en_shifr(yslovie)
    mess = input("Сообщение для шифра : ")
    finish_message = ''
    if yslovie == '+':
        for abc in mess.lower():
            number_in_kwargs = english_lang.find(abc)
            shifr_mesto = number_in_kwargs + move
            en_lent = en_len - 1
            if abc in english_lang:
                if shifr_mesto > en_lent:
                    shifr_mesto = shifr_mesto % en_len
                    finish_message += english_lang[shifr_mesto]
                else:
                    finish_message += english_lang[shifr_mesto]
            else:
                finish_message += abc
        print('\n\nДлина словаря: {}\nВаше сообщение :{} \nКоличество шагов:{} \nВот шифровка вашего сообщения : {}'.format(en_len,mess, move, finish_message))
    elif yslovie == '-':
        for abc in mess.lower():
            number_in_kwargs = english_lang.find(abc)
            shifr_mesto = number_in_kwargs - move
            if abc in english_lang:
                if shifr_mesto < 0:
                    shifr_mesto = shifr_mesto%en_len
                    finish_message += english_lang[shifr_mesto]
                else:
                    finish_message += english_lang[shifr_mesto]
            else:
                finish_message += abc
        print('\n\nДлина словаря: {}\nВаше шифрованое сообщение :{} \nКоличество шагов:{} \nВот дешифровка вашего сообщения : {}'.format(en_len,mess, move, finish_message))
    else:
        print("uncorrect")


while True:
    try:
        exit = int(input(f"ШИФР ЦЕЗАРЯ\n\n\n\n\n1.Шифр украинским словарём\n2.Шифр английским словарём\n3.Выход\nСловари : \n English: {english_lang}\nUkraining: {ukraine_lang}\n\nNUM = "))
    except ValueError:
        print("\n\n\n*******Выберите число а не символ*******\n\n\n")
    if exit == 1:
        num = input("code: +\ndecode: -\n\n+/- : ")
        if num == '+' or num == '-':
            uk_shifr(num)
    elif exit == 2:
        num = input("code: +\ndecode: -\n\n+/- : ")
        if num == '+' or num == '-':
            en_shifr(num)
    elif exit == 3: break
    else: print("uncorrect\n\n\n")

#################################### With love Shakal #####################################
