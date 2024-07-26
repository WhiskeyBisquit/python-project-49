#!/usr/bin/env python3
from brain_games.engine import play_game
from brain_games.games.calc import description, math_problem


def start_calc():
    play_game(description, math_problem)


def main():
    start_calc()


if __name__ == '__main__':
    main()
