import random


DESCRIPT = 'What is the result of the expression?'
MIN_NUM = 1
MAX_NUM = 99


def form_task_and_answer():
    first_num = random.randint(MIN_NUM, MAX_NUM)
    sec_num = random.randint(MIN_NUM, MAX_NUM)
    sign = random.choice('+-*')
    game_task = ('{x} {y} {z}'.format(x=first_num, y=sign, z=sec_num))
    if sign == '+':
        result = first_num + sec_num
    elif sign == '-':
        result = first_num - sec_num
    else:
        result = first_num * sec_num
    return game_task, result
