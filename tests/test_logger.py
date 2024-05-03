# Quantum Simulation Project - test_logger.py
# This module contains unit tests for the Logger class.

import unittest
import logging
from unittest.mock import patch
from logger import Logger

class TestLogger(unittest.TestCase):
    def setUp(self):
        self.logger = Logger()

    def test_logger_default_level(self):
        # Test default logging level is set to INFO
        self.assertEqual(self.logger.get_level(), logging.INFO)

    def test_logger_custom_level(self):
        # Test setting custom logging level
        self.logger.set_level(logging.DEBUG)
        self.assertEqual(self.logger.get_level(), logging.DEBUG)

    def test_logger_format(self):
        # Test logging message format
        with patch('logging.FileHandler'):
            self.logger.set_file_handler('test.log')
        log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        self.assertEqual(self.logger.get_formatter().format, log_format)

    def test_logger_log_file_creation(self):
        # Test log file creation
        log_file = 'test.log'
        with patch('logging.FileHandler') as mock_file_handler:
            self.logger.set_file_handler(log_file)
        mock_file_handler.assert_called_once_with(log_file)

    def test_logger_log_message(self):
        # Test logging a message
        with patch('logging.FileHandler'):
            self.logger.set_file_handler('test.log')
        with patch('logging.Logger.log') as mock_log:
            self.logger.log('Test message', level=logging.INFO)
        mock_log.assert_called_once_with(logging.INFO, 'Test message')

if __name__ == '__main__':
    unittest.main()
