from random import randint

DESCRIPT = 'What number is missing in the progression?'
ELEMENT_NUMBER = 10


def form_task_and_answer():
    first_digit = randint(1, 3)
    differ = randint(1, 3)
    ending_row = (first_digit + differ * (ELEMENT_NUMBER - 1))
    progression = progression_shape(first_digit, ending_row, differ)
    invisible_index = randint(0, ELEMENT_NUMBER - 1)
    hidden_one = progression[invisible_index]
    question = list_to_string(progression, invisible_index)
    return question, hidden_one


def progression_shape(first_digit, ending_row, differ):
    progression = range(first_digit, ending_row + 1, differ)
    return progression


def list_to_string(progression, invisible_index):
    progression = list(progression)
    return " ".join(str(s) if i != invisible_index else ".." for i,
                    s in enumerate(progression))
