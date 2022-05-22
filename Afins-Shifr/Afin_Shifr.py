# a = 111/2
# b = 111//2
# c = 111%122
class Afins():
    def __init__(self):
        #####################Словари можно изменять только содержимое в скобках#######################
        self.ukraine_lang = "абвгgдеєжзиіїйклмнопрстуфхцчшщьюя0123456789"
        self.english_lang = "abcdefgjklmnopqrstuvwxyz0123456789"
        self.arr_uk = self.ukraine_lang.split(' ')
        self.arr_en = self.english_lang.split(' ')
        ##############################################################################################
        self.uk_len = len(self.ukraine_lang)
        self.en_len = len(self.english_lang)

        while True:
            try:
                self.exit = int(input(f"\n*************AFINS CODE**************\n\nСловари:\nEnglish: {self.arr_en}\nUkraining: {self.arr_uk}\n\n1.Шифр украинским словарём\n2.Шифр английским словарём\n3.Выход\n\nNUM = "))
                if self.exit == 1:
                    self.num = input("code: +\ndecode: -\n\n+/- : ")
                    if self.num == '+' or self.num == '-':
                        self.uk_shifr(self.num)
                    else:
                        print("Введено не верное значение")
                elif self.exit == 2:
                    self.num = input("code: +\ndecode: -\n\n+/- : ")
                    if self.num == '+' or self.num == '-':
                        self.en_shifr(self.num)
                        Afins()
                    else:
                        print("Введено не верное значение")
                        Afins()
                elif self.exit == 3:
                    break
                else:
                    print("uncorrect")
            except Exception:
                print("\n\n\n*******Выберите число а не символ*******\n\n\n")
    def script(self):
        self.k_1 = 0
        if self.lucifer == 0:
            while True:
                self.k_1 += 1
                number = (self.k_1 * self.k1) % self.uk_len
                if number == 1:
                    break
        elif self.lucifer == 1:
            while True:
                self.k_1 += 1
                number = (self.k_1 * self.k1) % self.en_len
                if number == 1:
                    break

    def uk_shifr(self, yslovie):
        self.lucifer = 0
        try:
            self.k1 = int(input("K1 : "))
            self.k2 = int(input("K2 : "))
        except:
            print("\n\n\n*******Выберите число а не символ*******\n\n\n")
        self.script()
        self.mess = input("Сообщение для шифра : ")
        self.finish_message = ''
        if yslovie == '+':
            for abc in self.mess.lower():
                number_in_kwargs = self.ukraine_lang.find(abc)
                shifr_mesto = number_in_kwargs*self.k1 + self.k2
                shirf_mesto_2 = shifr_mesto%self.uk_len
                if abc in self.ukraine_lang:
                    self.finish_message += self.ukraine_lang[shirf_mesto_2]
                else:
                    self.finish_message += abc
            print("\n\n\nДлина словаря: {}\nСообщение: {}\nКоэфициент умножения К1: {}\nКоэфициэнт сумирования К2: {}\nЗашифрованое сообщение: {}".format(self.uk_len,self.mess, self.k1, self.k2,self.finish_message))
        elif yslovie == '-':
            for abc in self.mess.lower():
                number_in_kwargs = self.ukraine_lang.find(abc)
                shifr_mesto = (number_in_kwargs - self.k2)
                if shifr_mesto < 0:
                    shifr_mesto = (self.uk_len + shifr_mesto) * self.k_1
                else:
                    shifr_mesto = shifr_mesto * self.k_1
                shifr_mesto = shifr_mesto % self.uk_len

                if abc in self.ukraine_lang:
                    self.finish_message += self.ukraine_lang[shifr_mesto]
                else:
                    self.finish_message += abc
            print("\n\n\nДлина словаря: {}\nШифрованое сообщение: {}\nКоэфициент умножения К1: {}\nКоэфициэнт сумирования К2: {}\nОбернений коэфициэнт К^-1: {}\nCообщение: {}".format(self.uk_len,self.mess, self.k1, self.k2, self.k_1,self.finish_message))
        else:
            print("uncorrect")

    def en_shifr(self, yslovie):
        self.lucifer = 1
        try:
            self.k1 = int(input("K1 : "))
            self.k2 = int(input("K2 : "))
        except ValueError:
            print("\n\n\n*******Выберите число а не символ*******\n\n\n")


        self.script()

        self.mess = input("Сообщение для шифра : ")
        self.finish_message = ''
        if yslovie == '+':
            for abc in self.mess.lower():
                number_in_kwargs = self.english_lang.find(abc)
                shifr_mesto = number_in_kwargs*self.k1 + self.k2
                shirf_mesto_2 = shifr_mesto%self.en_len
                if abc in self.english_lang:
                    self.finish_message += self.english_lang[shirf_mesto_2]
                else:
                    self.finish_message += abc
            print("\n\n\nДлина словаря: {}\nСообщение: {}\nКоэфициент умножения К1: {}\nКоэфициэнт сумирования К2: {}\nЗашифрованое сообщение: {}".format(self.en_len,self.mess, self.k1, self.k2,self.finish_message))
        elif yslovie == '-':
            for abc in self.mess.lower():
                number_in_kwargs = self.english_lang.find(abc)
                shifr_mesto = (number_in_kwargs - self.k2)
                if shifr_mesto < 0:
                    shifr_mesto = (self.en_len + shifr_mesto) * self.k_1
                else:
                    shifr_mesto = shifr_mesto * self.k_1
                shifr_mesto = shifr_mesto%self.en_len

                if abc in self.english_lang:
                    self.finish_message += self.english_lang[shifr_mesto]
                else:
                    self.finish_message += abc
            print("\n\n\nДлина словаря: {}\nШифрованое сообщение: {}\nКоэфициент умножения К1: {}\nКоэфициэнт сумирования К2: {}\nОбернений коэфициэнт К^-1: {}\nCообщение: {}".format(self.en_len,self.mess, self.k1, self.k2, self.k_1,self.finish_message))
        else:
            print("uncorrect")

if __name__ == "__main__":
    Afins()

#################################### With love Shakal #####################################
