#!/usr/bin/env python3
from brain_games.cli import welcome_user
from random import randint
import prompt


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def set_secret_number():
    secret_number = randint(1, 50)
    return secret_number


def is_even():
    name = welcome_user()
    score = 0
    secret_number = set_secret_number()
    question = f'Question: {secret_number}'
    print(RULE)
    print(question)
    player_answer = prompt.string('Your answer: ')

    while score < 3:
        if secret_number % 2 == 0 and player_answer.lower() == 'yes':
            print('Correct!')
            score += 1
        elif secret_number % 2 != 0 and player_answer.lower() != 'yes':
            print('Correct!')
            score += 1
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'."
                  + "\n" + f"Let's try again, {name}!")
            score = 0
            break

        secret_number = set_secret_number()
        question = f'Question: {secret_number}'

        if score == 3:
            print(f'Congratulations, {name}!')
            break

        print(question)
        player_answer = prompt.string('Your answer: ')


def main():
    is_even()


if __name__ == '__main__':
    main()
