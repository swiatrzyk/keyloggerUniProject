from cryptography.fernet import Fernet
import os

from settings import key_filename
from cryptography.KeyGenerator import KeyGenerator


class Decryption:
    def __init__(self, file_path):
        self.file_path = file_path
        self.key = self.get_key()

        system_information_e = 'e_system.txt'
        clipboard_information_e = 'e_clipboard.txt'
        keys_information_e = 'e_keys_logged.txt'

        self.encrypted_files = [system_information_e,
                                clipboard_information_e,
                                keys_information_e]

    def decrypt(self):
        for count, decrypting_files in enumerate(self.encrypted_files):
            with open(self.encrypted_files[count], 'rb') as f:
                data = f.read()

            fernet = Fernet(self.key)
            decrypted = fernet.decrypt(data)

            with open("decryption.txt", 'ab') as f:
                f.write(decrypted)

    def get_key(self):
        key_path = "\\".join([self.file_path, key_filename])
        if not os.path.isfile(key_path):
            KeyGenerator(self.file_path)
        with open(key_path, 'rb') as f:
            key = f.read()
        return key
