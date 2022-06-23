import random


DESCRIPT = "Answer 'yes' if given number is prime. Otherwise answer 'no'."
MIN_NUM = 1
MAX_NUM = 99


def form_task_and_answer():
    numb = random.randint(MIN_NUM, MAX_NUM)
    game_task = ('{x}'.format(x=numb))
    if is_prime(numb):
        result = 'yes'
    else:
        result = 'no'
    return game_task, result


def is_prime(digit):
    div = 2
    while digit % div != 0:
        div += 1
    return div == digit
