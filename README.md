# Calculator project

This is package for simple python calculations:
  1. addition
  2. subtraction
  3. division
  4. multiplication
  5. taking root from a number

Package consist of two files:
  1. calculator_main - are file consisting of Class and all methods
  2. calculator_test - are file with unittests

# Usage

Add 15, divide 3 and reset memory:

```python
>>> from calculator_main import Calculator
>>> calc = Calculator()
>>> current_memory = calc.get_memory()
>>> calc.addition(15)
>>> print(current_memory)
15
>>> >>> calc.division(3)
>>> print(current_memory)
5
>>> calc.reset_memory()
>>> print(current_memory)
0
```

# Instalation

```python
pip install calculator
```

# License

MIT (https://choosealicense.com/licenses/mit/)
