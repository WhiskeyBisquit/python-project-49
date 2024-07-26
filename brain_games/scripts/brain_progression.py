#!/usr/bin/env python3
from brain_games.engine import play_game
from brain_games.games.progression import description, solve_progression


def start_progression():
    play_game(description, solve_progression)


def main():
    start_progression()


if __name__ == '__main__':
    main()
