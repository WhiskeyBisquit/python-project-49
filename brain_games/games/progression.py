from random import randint

description = 'What number is missing in the progression?'


def solve_progression():
    first_el = randint(1, 85)
    step = randint(2, 9)
    progression_arr = [first_el]

    for el in progression_arr:
        progression_arr.append(el + step)
        if len(progression_arr) == 10:
            break

    missing_element = randint(0, 9)
    result = str(progression_arr[missing_element])
    progression_arr[missing_element] = '..'
    question = ' '.join(str(el) for el in progression_arr)

    return question, result
