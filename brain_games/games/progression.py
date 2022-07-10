from random import randint, randrange

DESCRIPT = 'What number is missing in the progression?'


def form_task_and_answer():
    first_num = randint(1, 20)
    step = randint(5, 10)
    end_row = first_num + (step * 10)
    length = 10
    progression = list(range(first_num, end_row, step))
    invisible = randrange(0, length)
    correct_answer, progression[invisible] = progression[invisible], '..'
    progression = ' '.join(map(str, progression))
    return progression, str(correct_answer)
