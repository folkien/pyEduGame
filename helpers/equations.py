'''
    Helpers code for generating equations
    objects.
'''
from dataclasses import dataclass, field
import random


@dataclass
class Equation:
    ''' Equation object '''
    # Equation string
    equation: str = field(default=None, init=True)
    # Equation answer
    answer: float = field(default=0, init=True)
    # Equation prize
    stars : int = field(default=1, init=True)

    def __post_init__(self):
        ''' Evaluate equation and get answer '''

        if (self.stars == 0):
            raise ValueError("Stars prize min is 1!")



def generate_equation_add(range : int = 20) -> Equation:
    ''' Generate equation object '''
    number1 = random.randint(0, range)
    number2 = random.randint(0, range)
    return Equation(equation=f"{number1} + {number2} = ", 
                    answer=number1+number2, 
                    stars=1)


def generate_equation_sub(range : int = 20) -> Equation:
    ''' Generate equation object '''
    number1 = random.randint(0, range)
    number2 = random.randint(0, range)
    return Equation(equation=f"{number1} - {number2} = ", 
                    answer=number1-number2, 
                    stars=1)


def generate_equation_sub_positive(range : int = 20) -> Equation:
    ''' Generate equation object '''
    number1 = random.randint(0, range)
    number2 = random.randint(0, range)

    # First number must be greater than second
    if number1 < number2:
        number1, number2 = number2, number1

    return Equation(equation=f"{number1} - {number2} = ", 
                    answer=number1-number2, 
                    stars=1)

def generate_equation_multiply(range : int = 10) -> Equation:
    ''' Generate equation object '''
    number1 = random.randint(0, range)
    number2 = random.randint(0, range)
    return Equation(equation=f"{number1} * {number2} = ", 
                    answer=number1*number2, 
                    stars=2)

def generate_equation_divide_int(range : int = 10) -> Equation:
    ''' Generate equation object '''
    # Divider
    number2 = random.randint(0, range)
    # Dividend
    number1 = random.randint(1, range) * number2


    return Equation(equation=f"{number1} / {number2} = ", 
                    answer=number1/number2, 
                    stars=2)