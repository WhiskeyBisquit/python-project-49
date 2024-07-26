#!/usr/bin/env python3
from brain_games.engine import play_game
from brain_games.games.gcd import description, find_gcd


def start_gcd():
    play_game(description, find_gcd)


def main():
    start_gcd()


if __name__ == '__main__':
    main()
