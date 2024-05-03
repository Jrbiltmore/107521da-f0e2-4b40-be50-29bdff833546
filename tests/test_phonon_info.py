import unittest
from myproject.phonon_info import PhononInfo

class TestPhononInfo(unittest.TestCase):
    def test_phonon_info_creation(self):
        """Test creation of PhononInfo instance"""
        phonon_info = PhononInfo(frequency=10, mode='X', amplitude=0.5)
        self.assertEqual(phonon_info.frequency, 10)
        self.assertEqual(phonon_info.mode, 'X')
        self.assertEqual(phonon_info.amplitude, 0.5)

    def test_phonon_info_str(self):
        """Test string representation of PhononInfo instance"""
        phonon_info = PhononInfo(frequency=10, mode='X', amplitude=0.5)
        self.assertEqual(str(phonon_info), "PhononInfo(Frequency: 10, Mode: X, Amplitude: 0.5)")

    def test_phonon_info_eq(self):
        """Test equality of PhononInfo instances"""
        phonon_info_1 = PhononInfo(frequency=10, mode='X', amplitude=0.5)
        phonon_info_2 = PhononInfo(frequency=10, mode='X', amplitude=0.5)
        phonon_info_3 = PhononInfo(frequency=5, mode='Y', amplitude=0.3)

        self.assertEqual(phonon_info_1, phonon_info_2)
        self.assertNotEqual(phonon_info_1, phonon_info_3)

if __name__ == '__main__':
    unittest.main()
