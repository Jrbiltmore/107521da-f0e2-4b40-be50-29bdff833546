# Quantum Simulation Project - test_config_manager.py
# This module contains unit tests for the ConfigManager class.

import unittest
from unittest.mock import patch
from config_manager import ConfigManager

class TestConfigManager(unittest.TestCase):
    def setUp(self):
        self.config_manager = ConfigManager()

    def test_load_config_valid(self):
        # Test loading a valid configuration file
        with patch('builtins.open', unittest.mock.mock_open(read_data='{"param1": 1, "param2": 2}')):
            self.config_manager.load_config('test_config.json')
        self.assertEqual(self.config_manager.get_config(), {"param1": 1, "param2": 2})

    def test_load_config_invalid_json(self):
        # Test loading an invalid JSON configuration file
        with patch('builtins.open', unittest.mock.mock_open(read_data='invalid_json')):
            with self.assertRaises(ValueError):
                self.config_manager.load_config('test_config.json')

    def test_load_config_file_not_found(self):
        # Test loading a configuration file that does not exist
        with self.assertRaises(FileNotFoundError):
            self.config_manager.load_config('nonexistent_config.json')

    def test_get_param_valid(self):
        # Test retrieving a valid parameter from the configuration
        self.config_manager.config = {"param1": 1, "param2": 2}
        self.assertEqual(self.config_manager.get_param("param1"), 1)

    def test_get_param_invalid(self):
        # Test retrieving an invalid parameter from the configuration
        self.config_manager.config = {"param1": 1, "param2": 2}
        with self.assertRaises(KeyError):
            self.config_manager.get_param("param3")

    def test_get_param_default_value(self):
        # Test retrieving a parameter with a default value
        self.config_manager.config = {"param1": 1, "param2": 2}
        self.assertEqual(self.config_manager.get_param("param3", default=3), 3)

    def test_get_param_default_value_override(self):
        # Test retrieving a parameter with a default value, overridden by existing value in config
        self.config_manager.config = {"param1": 1, "param2": 2}
        self.assertEqual(self.config_manager.get_param("param2", default=3), 2)

if __name__ == '__main__':
    unittest.main()
