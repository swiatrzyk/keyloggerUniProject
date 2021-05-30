import os
from unittest import TestCase
from settings import file_path, filenames

from SystemInfoProvider import SystemInfoProvider


class TestSystemInfoProvider(TestCase):

    def test_fetch_and_save_computer_information(self):
        system_information = filenames["system_info"]
        extend = "\\"
        SystemInfoProvider().fetch_and_save_computer_information(file_path)
        file_name = file_path + extend + system_information
        self.assertNotEqual(os.stat(file_name).st_size, 0)
