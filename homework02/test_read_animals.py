#!/usr/bin/env python3
import unittest
from read_animals import get_num_animals

class TestReadAnimals(unittest.TestCase):

    def test_get_num_animals(self):
        self.assertEqual(get_num_animals(1, 5), 1)
        self.assertEqual(get_num_animals(5, 5), 5)
        self.assertRaises(AssertionError, get_num_animals, 6, 5)
        self.assertRaises(AssertionError, get_num_animals, -1, 5)
        self.assertRaises(ValueError, get_num_animals, 'astring', 5)
        self.assertRaises(TypeError, get_num_animals, None, 5)

if __name__ == '__main__':
    unittest.main()
