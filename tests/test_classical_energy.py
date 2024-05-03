# Quantum Simulation Project - test_classical_energy.py
# This module contains unit tests for the classical_energy module.

import unittest
import numpy as np
from classical_energy import calculate_classical_energy

class TestClassicalEnergy(unittest.TestCase):
    def test_calculate_classical_energy_valid_input(self):
        # Test with valid inputs
        phonon_states = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
        config = {'atomic_mass': 1.0, 'spring_constant': 10.0}
        expected_energy = 0.075
        self.assertAlmostEqual(calculate_classical_energy(phonon_states, config), expected_energy, places=3)

    def test_calculate_classical_energy_invalid_input(self):
        # Test with invalid inputs
        with self.assertRaises(TypeError):
            calculate_classical_energy([0.1, 0.2, 0.3, 0.4, 0.5], {'atomic_mass': 1.0, 'spring_constant': 10.0})
        with self.assertRaises(TypeError):
            calculate_classical_energy(np.array([0.1, 0.2, 0.3, 0.4, 0.5]), ['atomic_mass', 'spring_constant'])
        with self.assertRaises(ValueError):
            calculate_classical_energy(np.array([0.1, 0.2, 0.3, 0.4, 0.5]), {'atomic_mass': 1.0})

    def test_calculate_classical_energy_edge_cases(self):
        # Test with edge cases
        phonon_states = np.array([0.1])  # Single phonon state
        config = {'atomic_mass': 1.0, 'spring_constant': 10.0}
        self.assertEqual(calculate_classical_energy(phonon_states, config), 0.0)  # Expected energy is 0 for single state

    def test_calculate_classical_energy_error_handling(self):
        # Test error handling
        # Test with invalid phonon_states (non-array)
        with self.assertLogs(level='ERROR'):
            calculate_classical_energy(0.1, {'atomic_mass': 1.0, 'spring_constant': 10.0})
        
        # Test with missing config parameters
        with self.assertRaises(ValueError):
            calculate_classical_energy(np.array([0.1, 0.2, 0.3, 0.4, 0.5]), {})
        
        # Test with invalid config (not a dictionary)
        with self.assertLogs(level='ERROR'):
            calculate_classical_energy(np.array([0.1, 0.2, 0.3, 0.4, 0.5]), 123)

if __name__ == '__main__':
    unittest.main()
