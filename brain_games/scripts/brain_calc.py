#!/usr/bin/env python3
from brain_games.engine import play_game
from brain_games.games.calc import description, math_problem


def main():
    play_game(description, math_problem)


if __name__ == '__main__':
    main()
