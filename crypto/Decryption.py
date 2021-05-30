from cryptography.fernet import Fernet
import os

from settings import key_filename, filenames
from crypto.KeyGenerator import KeyGenerator


class Decryption:
    def __init__(self, file_path):
        self.path = file_path
        self.file_path = file_path + "\\"

        self.key = self.get_key()

        self.encrypted_files = []

        for _, filename in filenames.items():
            pivot = filename.find(".txt")
            self.encrypted_files.append(self.file_path + filename[:pivot] + "_e" + filename[pivot:])

        self.decrypt()

    def decrypt(self):
        for count, decrypting_file in enumerate(self.encrypted_files):
            if os.path.isfile(self.encrypted_files[count]):
                with open(self.encrypted_files[count], 'rb') as f:
                    data = f.read()

                fernet = Fernet(self.key)
                decrypted = fernet.decrypt(data)

                pivot = decrypting_file.rfind("\\") + 1
                decryption_filename = "_".join(["decrypted", decrypting_file[pivot:], ".txt"])
                decryption_path = "\\".join([self.path, decryption_filename])
                with open(decryption_path, 'wb') as f:
                    f.write(decrypted)
                return decrypted

    def get_key(self):
        key_path = "\\".join([self.path, key_filename])
        if not os.path.isfile(key_path):
            KeyGenerator(self.file_path)
        with open(key_path, 'rb') as f:
            key = f.read()
        return key
