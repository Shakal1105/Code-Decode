import tkinter as tk
import tkinter.ttk as tkk

class ShakPy():
    def __init__(self):
        self.text, self.key, self.shifr = None, None, None
        self.wind()

    def wind(self):
        window = tk.Tk()
        window.title("[ShakPy]XOR, SHIFR")
        window.geometry("600x500+400+200")
        window.config(bg="Gray")

        def crypt():
            self.text, self.key, self.shifr = str(text.get(1.0, tk.END)).strip(), str(key.get()), int(shifr.get())
            ciphertext, decrypted = self.encrypt_decrypt()
            crypt_text.delete(0, tk.END)
            decrypt_text.delete(0, tk.END)
            crypt_text.insert(0, f"{ciphertext}")
            decrypt_text.insert(0, f"{decrypted}"[2:-1])

        text = tk.Text(window, width=60)
        text.grid(row=0, rowspan=2, column=1, columnspan=2)
        key = tk.Entry(window, width=20)
        tk.Label(window, text="KEY").grid(row=2, column=1)
        key.insert(0, "secret")
        key.grid(row=3, column=1)
        tk.Label(window, text="VALUE").grid(row=2, column=2)
        shifr = tkk.Spinbox(window, from_=0, to=999, width=5)
        shifr.insert(0, "0")
        shifr.grid(row=3, column=2)
        tk.Label(window, text="Encode ==> ").grid(row=4, column=1)
        crypt_text = tk.Entry(window, relief="raised", width=50)
        crypt_text.insert(0, "NULL DATA")
        crypt_text.grid(row=4, column=2, columnspan=2)
        tk.Label(window, text="Decode ==> ").grid(row=5, column=1)
        decrypt_text = tk.Entry(window, relief="groove", width=50)
        decrypt_text.insert(0, "NULL DATA")
        decrypt_text.grid(row=5, column=2, columnspan=2)
        tk.Button(window, text="Encrypt/Decrypt", command=crypt).grid(column=3, row=0)
        window.mainloop()

    def xor_cipher_with_shift(self, data, key, shift):
        encrypted = bytearray()
        key_length = len(key)
        for i, byte in enumerate(data):
            shifted_key_byte = key[(i + shift) % key_length]
            encrypted_byte = byte ^ ord(shifted_key_byte)
            encrypted.append(encrypted_byte)
        return bytes(encrypted)

    def encrypt_decrypt(self):
        if self.text.startswith("b'") and self.text.strip().endswith("'"):
            text_bytes = bytes(self.text[2:-1].encode('utf-8').decode('unicode_escape').encode('latin1'))
            print(text_bytes)
            decrypted = self.xor_cipher_with_shift(text_bytes, self.key, self.shifr)
            ciphertext = text_bytes
        else:
            text_bytes = self.text.encode('utf-8')
            ciphertext = self.xor_cipher_with_shift(text_bytes, self.key, self.shifr)
            decrypted = self.xor_cipher_with_shift(ciphertext, self.key, self.shifr)
        return ciphertext, decrypted

if __name__ == "__main__":
    ShakPy()
