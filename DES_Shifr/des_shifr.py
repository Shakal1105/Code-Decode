from DesBase import des, CBC, PAD_PKCS5
import binascii

class Des_code_decode():
    def __init__(self):
        self.running()

    def des_encrypt(self, s):
        """
             Шифрование DES
             : param s: необработанная строка
             : return: зашифрованная строка, hex
        """
        secret_key = self.KEY
        iv = secret_key
        k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
        en = k.encrypt(s, padmode=PAD_PKCS5)
        print(binascii.b2a_hex(en))


    def des_descrypt(self,s):
        """
             Дешифрование DES
             : param s: зашифрованная строка, hex
             : return: расшифрованная строка
        """
        secret_key = self.KEY
        iv = secret_key
        k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
        de = k.decrypt(binascii.a2b_hex(s), padmode=PAD_PKCS5)
        print(de)

    def yslovie(self):
        if len(self.KEY) < 8:
            while True:
                self.KEY += "0"
                if len(self.KEY) == 8:
                    print('был згенерирован ключ так как ключ меньше 8 бит ({})'.format(self.KEY))
                    break
        if len(self.KEY) > 8:
            self.KEY = self.KEY[:8]
            print('Был выбран ключ: (' + self.KEY + ")так как он превышает размер 8 байт")

    def running(self):
        self.choose= input("1. code , 2. decode: ")
        if self.choose == '1':
            self.KEY = input('Key: ')
            if len(self.KEY) != 8:self.yslovie()
            self.slovo = input("text : ")
            self.des_encrypt(self.slovo)
        elif self.choose == '2':
            self.KEY = input('Key: ')
            if len(self.KEY) != 8: self.yslovie()
            try:
                self.slovo = input("text : ")
                self.des_descrypt(self.slovo)
            except binascii.Error:
                print("Введённый текст не являеться шифром")
                self.running()
        else: self.running()
        self.running()

if __name__ == "__main__":
    Des_code_decode()
