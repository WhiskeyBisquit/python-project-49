#!/usr/bin/env python3
from brain_games.engine import play_game
from brain_games.games.prime import description, is_prime


def start_prime():
    play_game(description, is_prime)


def main():
    start_prime()


if __name__ == '__main__':
    main()
