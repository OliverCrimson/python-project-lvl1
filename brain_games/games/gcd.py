from random import randint
from math import gcd


DESCRIPT = 'Find the greatest common divisor of given numbers.'


def form_task_and_answer():
    first_num = randint(1, 99)
    second_num = randint(1, 99)
    divisor = gcd(first_num, second_num)
    question = f'{first_num} {second_num}'
    return question, divisor
