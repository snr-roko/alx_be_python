import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp (self) :
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator ()

    def test_add (self) :
        """Test the addition method."""
        self.assertEqual (self.calc.add (2, 3), 5)
        self.assertEqual (self.calc.add (-1, 1), 0)
        self.assertEqual (self.calc.add (-50, 20), -30)
    
    def test_subtract (self) :
        """Test the subtract method."""
        self.assertEqual (self.calc.subtract (20, 10), 10)
        self.assertEqual (self.calc.subtract (10, 20), -10)
        self.assertEqual (self.calc.subtract (30, 30), 0)

    def test_multiply (self) :
        """Test the multiply method"""
        self.assertEqual (self.calc.multiply (20, 20), 400)
        self.assertEqual (self.calc.multiply (-20, 20), -400)
        self.assertEqual (self.calc.multiply (20, 0), 0)
        self.assertEqual (self.calc.multiply (-20, -20), 400)

    def test_divide (self) :
        """Test the divide method"""
        self.assertEqual (self.calc.divide (20, 2), 10)
        self.assertEqual (self.calc.divide (20, 0), None)
        self.assertEqual (self.calc.divide (0, 20), 0)
        self.assertEqual (self.calc.divide (20, -2), -10)


if __name__ == "__main__" :
    unittest.main()
  