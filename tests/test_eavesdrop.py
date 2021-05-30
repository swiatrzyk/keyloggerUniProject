import os
import unittest
from unittest import TestCase
from key_logger.eavesdrop import EavesdropService
from settings import file_path, filenames


class TestEavesdrop(TestCase):

    def test_microphone(self):
        EavesdropService().microphone()
        file_name = file_path + "\\" + filenames["audio"]
        self.assertNotEqual(os.stat(file_name).st_size, 0)

    def test_screenshot(self):
        EavesdropService().screenshot()
        file_name = file_path + "\\" + filenames["screenshot"]
        self.assertNotEqual(os.stat(file_name).st_size, 0)

    def test_copy_clipboard(self):
        EavesdropService().copy_clipboard()
        file_name = file_path + "\\" + filenames["clipboard"]
        self.assertNotEqual(os.stat(file_name).st_size, 0)
