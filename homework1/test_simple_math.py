import unittest
from simple_math import SimpleMath

class TestSimpleMath(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleMath()

    def test_square(self):
        self.assertEqual(self.calc.square(2), 4)
        self.assertEqual(self.calc.square(-3), 9)
        self.assertEqual(self.calc.square(0), 0)

    def test_cube(self):
        self.assertEqual(self.calc.cube(3), 27)
        self.assertEqual(self.calc.cube(-3), -27)
        self.assertEqual(self.calc.cube(0), 0)

if __name__ == '__main__':
    unittest.main()
