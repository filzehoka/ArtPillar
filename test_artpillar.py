# test_artpillar.py
"""
Tests for ArtPillar module.
"""

import unittest
from artpillar import ArtPillar

class TestArtPillar(unittest.TestCase):
    """Test cases for ArtPillar class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ArtPillar()
        self.assertIsInstance(instance, ArtPillar)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ArtPillar()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
