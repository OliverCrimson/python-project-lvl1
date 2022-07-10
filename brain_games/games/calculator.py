from random import randint, choice
from operator import add, sub, mul


DESCRIPT = 'What is the result of the expression?'


def form_task_and_answer():
    first_num = randint(1, 99)
    second_num = randint(1, 99)
    operations = {
        '+': add,
        '-': sub,
        '*': mul,
    }
    operation = choice(list(operations.keys()))
    result = str(operations[operation](first_num, second_num))
    question = f'{first_num} {operation} {second_num}'

    return question, result
