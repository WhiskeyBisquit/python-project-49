from random import randint
from math import gcd

description = 'Find the greatest common divisor of given numbers.'


def find_gcd():
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    question = f'{num1} {num2}'
    result = str(gcd(num1, num2))
    return question, result
