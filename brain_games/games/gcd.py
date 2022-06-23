import random
from math import gcd


DESCRIPT = 'Find the greatest common divisor of given numbers.'
MIN_NUM = 1
MAX_NUM = 99


def form_task_and_answer():
    first_num = random.randint(MIN_NUM, MAX_NUM)
    sec_num = random.randint(MIN_NUM, MAX_NUM)
    divisor = gcd(first_num, sec_num)
    game_task = ('{x} {y}'.format(x=first_num, y=sec_num))
    return game_task, divisor
