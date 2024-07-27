from random import randint

description = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime():
    result = ''
    question = randint(1, 100)

    if question == 1:
        result = 'no'
        return question, result

    divider = 2

    while divider <= question / 2:
        if question % divider == 0:
            result = 'no'
            return question, result

        divider += 1

    result = 'yes'
    return question, result
