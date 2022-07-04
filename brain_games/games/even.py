from random import randint


DESCRIPT = 'Answer "yes" if the number is even, otherwise answer "no".'


def form_task_and_answer():
    question = str(randint(1, 99))
    right_answer = 'no' if int(question) % 2 else 'yes'
    return question, right_answer
