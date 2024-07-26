from random import randint, choice

description = 'What is the result of the expression?'


def math_problem():
    num1 = randint(1, 50)
    num2 = randint(1, 50)
    operators = ['+', '-', '*']
    random_operator = choice(operators)
    question = f'{num1} {random_operator} {num2}'
    result = str(eval(question))
    return question, result
