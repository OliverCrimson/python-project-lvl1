from random import randint, choice

DESCRIPT = 'What number is missing in the progression?'


def form_task_and_answer():
    first_digit = randint(1, 3)
    differ = randint(1, 3)
    ending_row = first_digit + (differ * 10)
    progression = list(range(first_digit, ending_row, differ))
    invisible_index = str(choice(progression))
    progression = ' '.join(map(str, progression))
    question = progression.replace(invisible_index, '..', 1)
    return question, invisible_index
