#!/usr/bin/env python
from brain_games.cli import welcome_user


def greeting():
	print('Welcome to the Brain Games!')


def main():
	greeting()
	welcome_user()

if __name__ == '__main__':
	main()