import unittest
from calculator_main import Calculator


class TestCalculator(unittest.TestCase):
    def test_addition(self):
        calculator = Calculator()
        calculator.addition(5)
        self.assertEqual(calculator.memory, 5)

    def test_subtraction(self):
        calculator = Calculator()
        calculator.subtraction(3)
        self.assertEqual(calculator.memory, -3)

    def test_multiplication1(self):
        calculator = Calculator()
        calculator.addition(5)
        calculator.multiplication(3)
        self.assertEqual(calculator.memory, 15)

    def test_multiplication2(self):
        calculator = Calculator()
        calculator.multiplication(3)
        self.assertEqual(calculator.memory, 0)

    def test_division1(self):
        calculator = Calculator()
        calculator.addition(15)
        calculator.division(5)
        self.assertEqual(calculator.memory, 3)

    def test_division2(self):
        calculator = Calculator()
        calculator.division(3)
        self.assertEqual(calculator.memory, 0)

    def test_root1(self):
        calculator = Calculator()
        calculator.addition(9)
        calculator.root(2)
        self.assertEqual(calculator.memory, 3)

    def test_reset_memory(self):
        calculator = Calculator()
        calculator.addition(5)
        calculator.reset_memory()
        self.assertEqual(calculator.memory, 0)

    def test_get_memory(self):
        calculator = Calculator()
        calculator.addition(5)
        memory = calculator.get_memory()
        self.assertEqual(memory, 5)


if __name__ == '__main__':
    unittest.main()
