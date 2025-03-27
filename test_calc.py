import unittest
from calc import *

class TestCalc(unittest.TestCase):
    def test_class(self):
        self.assertEqual(add(10, 5), 15)

if __name__ == '__main__':
    unittest.main()