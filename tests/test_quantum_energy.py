import unittest
from myproject.quantum_energy import calculate_quantum_energy

class TestQuantumEnergy(unittest.TestCase):
    def test_calculate_quantum_energy(self):
        """Test calculation of quantum energy"""
        # Define sample phonon states and quantum parameters
        phonon_states = [0.1, 0.2, 0.3, 0.4]
        config = {'planck_constant': 6.626e-34, 'frequency_cutoff': 1e12}

        # Calculate quantum energy
        quantum_energy = calculate_quantum_energy(phonon_states, config)

        # Assert expected quantum energy value
        expected_energy = 6.626e-34 * (0.1 + 0.2 + 0.3 + 0.4) / 2
        self.assertAlmostEqual(quantum_energy, expected_energy)

if __name__ == '__main__':
    unittest.main()
