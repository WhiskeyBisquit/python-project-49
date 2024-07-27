from brain_games.cli import welcome_user
import prompt  # type: ignore


def play_game(description, game):
    score = 0
    name = welcome_user()
    print(description)
    question, result = game()
    print(f'Question: {question}')
    user_answer = prompt.string('Your answer: ').lower()

    while score < 3:
        if result == user_answer:
            print('Correct!')
            score += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  + f"Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            break

        question, result = game()

        if score == 3:
            print(f'Congratulations, {name}!')
            return

        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ').lower()
