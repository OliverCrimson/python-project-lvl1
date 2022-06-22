import random


DESCRIPT = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUM = 1
MAX_NUM = 99


def form_task_and_answer():

    number = random.randint(MIN_NUM, MAX_NUM)
    game_task = (str(number))
    even_number = (number % 2 == 0)
    if even_number:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return game_task, right_answer

