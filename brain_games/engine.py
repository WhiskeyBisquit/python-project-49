from brain_games.cli import welcome_user
import prompt  # type: ignore


def play_game(description, game):
    score = 0
    round_count = 3
    name = welcome_user()
    print(description)
    question, result = game()

    while score < round_count:
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ').lower()
        if result == user_answer:
            print('Correct!')
            score += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  + f"Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            return
        question, result = game()

    print(f'Congratulations, {name}!')
