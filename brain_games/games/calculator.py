import random


DESCRIPT = 'What is the result of the expression?'


def form_task_and_answer():
    first_num = random.randint(1, 99)
    second_num = random.randint(1, 99)
    sign = random.choice('+-*')
    game_task = ('{x} {y} {z}'.format(x=first_num, y=sign, z=second_num))
    if sign == '+':
        result = first_num + second_num
    elif sign == '-':
        result = first_num - second_num
    else:
        result = first_num * second_num
    return game_task, result
