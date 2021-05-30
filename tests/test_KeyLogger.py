from unittest import TestCase, mock
from unittest.mock import mock_open, patch

import time
from pynput.keyboard import Key, Listener

from KeyLogger import KeyLogger
from settings import file_path, time_iteration


class TestKeyLogger(TestCase):
    def setUp(self):
        self.keyLogger = KeyLogger(file_path)


class TestInit(TestKeyLogger):
    def test_initial_filename(self):
        self.assertEqual(self.keyLogger.filename, "keys_info.txt")

    def test_initial_stoppingTime(self):
        stopping_time = self.keyLogger.currentTime + time_iteration
        self.assertEqual(self.keyLogger.stoppingTime, stopping_time)

    def test_initial_number_of_iterations(self):
        self.assertEqual(self.keyLogger.number_of_iterations, 0)


class TestLoggingKeys(TestKeyLogger):
    def test_on_press(self):
        current_time = time.time()
        self.keyLogger.on_press("A")

        self.assertGreaterEqual(self.keyLogger.currentTime, current_time)

    @patch('__main__.__builtins__.open', new_callable=mock_open)
    def test_write_file(self, mock_write_file):
        self.keyLogger.keys = ["A", "B"]
        
        self.keyLogger.write_file()
        mock_write_file.assert_called_with(self.keyLogger.file_path, 'a')

    def test_on_release(self):
        result = self.keyLogger.on_release("A")
        self.assertTrue(result)

        result = self.keyLogger.on_release(Key.esc)
        self.assertFalse(result)

        self.keyLogger.stoppingTime = time.time()
        self.keyLogger.currentTime = self.keyLogger.stoppingTime + 10

        result = self.keyLogger.on_release("A")
        self.assertFalse(result)

    def test_after_stop(self):
        current_time = time.time()
        stopping_time = current_time + time_iteration

        self.keyLogger.after_stop()

        self.assertGreaterEqual(self.keyLogger.currentTime, current_time)
        self.assertGreaterEqual(self.keyLogger.stoppingTime, stopping_time)
        self.assertEqual(self.keyLogger.number_of_iterations, 1)
