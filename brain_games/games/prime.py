from random import randint


DESCRIPT = "Answer 'yes' if given number is prime. Otherwise answer 'no'."


def form_task_and_answer():
    number = randint(1, 99)
    question = f'{number}'
    if is_prime(number):
        result = 'yes'
    else:
        result = 'no'
    return question, result


def is_prime(digit):
    div = 2
    while digit % div != 0:
        div += 1
    return div == digit
