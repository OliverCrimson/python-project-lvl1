from random import randint, choice
from operator import add, sub, mul


DESCRIPT = 'What is the result of the expression?'


def form_task_and_answer():
    first_num = randint(1, 99)
    second_num = randint(1, 99)
    sign = choice('+-*')
    question = f'{first_num} {sign} {second_num}'
    if sign == '+':
        result = add(first_num, second_num)
    elif sign == '-':
        result = sub(first_num, second_num)
    else:
        result = mul(first_num, second_num)
    return question, result
