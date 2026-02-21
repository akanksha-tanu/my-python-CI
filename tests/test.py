import unittest
from calculator import add, subtract

class TestCalculator(unittest.TestCase):

    # Test Case 1: Test the add function
    def test_add(self):
        result = add(3, 5)
        self.assertEqual(result, 8)

    # Test Case 2: Test the subtract function
    def test_subtract(self):
        result = subtract(10, 4)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()
