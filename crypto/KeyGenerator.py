from cryptography.fernet import Fernet

from settings import key_filename


class KeyGenerator:
    def __init__(self, file_path):
        self.filename = key_filename
        self. file_path = "\\".join([file_path, self.filename])

        self.run()

    def run(self):
        key = Fernet.generate_key()
        with open(self. file_path, 'wb') as f:
            f.write(key)
