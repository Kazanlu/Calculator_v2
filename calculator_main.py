class Calculator:
    """
       A simple calculator class for performing basic arithmetic operations.

       Attributes:
       - memory: Holds the current value in memory.

       Methods:
       - addition: Adds a value to the memory.
       - subtraction: Subtracts a value from the memory.
       - multiplication: Multiplies the memory by a value.
       - division: Divide the memory by a value.
       - root: Take (n) root of a memory.
       """

    def __init__(self):
        self.memory = 0  # Current calculator number is zero as none of the actions was done yet.

    # Method which will add number to the current memory
    def addition(self, number):
        self.memory += number

    # Method which will subtract number from current memory
    def subtraction(self, number):
        self.memory -= number

    # Method which will perform multiplication on current memory by number defined
    def multiplication(self, number):
        self.memory *= float(number)

    # Method which will divide current memory by number defined
    def division(self, number):
        if number == 0:
            raise ValueError("Division was not done as input is not valid")
        else:
            self.memory /= number

    # Method which will take (n) root of a number where n = number
    def root(self, number):
        if number == 0:
            raise ValueError("Root was not taken as input is not valid")
        else:
            self.memory **= 1 / number

    # Method which will check current calculator memory
    def get_memory(self):
        return self.memory

    # Method which will reset current memory to initial value (zero)
    def reset_memory(self):
        self.memory = 0
