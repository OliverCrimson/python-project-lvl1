from random import randint


DESCRIPT = 'Answer "yes" if the number is even, otherwise answer "no".'


def form_task_and_answer():

#    number = randint(1, 99)
    question = str(randint(1, 99))
    even_number = int(question) % 2 == 0
    if even_number:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return question, right_answer
