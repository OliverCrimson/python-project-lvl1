import random

DESCRIPT = 'What number is missing in the progression?'
MIN_START = 1
MAX_START = 3
MIN_STEP = 1
MAX_STEP = 3
ELEMENT_NUMBER = 10


def form_task_and_answer():
    first_digit = random.randint(MIN_START, MAX_START)
    differ = random.randint(MIN_STEP, MAX_STEP)
    ending_row = (first_digit + differ * (ELEMENT_NUMBER - 1))
    progression = progression_shape(first_digit, ending_row, differ)
    invisible_digit = random.randint(0, ELEMENT_NUMBER - 1)
    hidden_one = progression[invisible_digit]
    game_task = list_to_string(progression, invisible_digit)
    return game_task, hidden_one


def progression_shape(first_digit, ending_row, differ):
    progression = range(first_digit, ending_row + 1, differ)
    return progression


def list_to_string(progression, invisible_digit):
    progression = list(progression)
    return " ".join(str(s) if i != invisible_digit else ".." for i,
                    s in enumerate(progression))
