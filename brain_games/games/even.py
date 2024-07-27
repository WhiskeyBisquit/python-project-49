from random import randint

description = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even():
    question = randint(1, 150)
    result = ''

    if question % 2 == 0:
        result = 'yes'
    else:
        result = 'no'

    return question, result
