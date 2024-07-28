#!/usr/bin/env python3
from brain_games.engine import play_game
from brain_games.games.even import description, is_even


def main():
    play_game(description, is_even)


if __name__ == '__main__':
    main()
