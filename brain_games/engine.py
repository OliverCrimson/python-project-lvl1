import prompt


NUM_OF_ROUNDS = 3


def please_go_game(game):
    print('Welcome to the Brain Games!')
    player_name = prompt.string('May i have your name? ')
    print(f'Hello, {player_name}!')
    print(game.DESCRIPT)
    for i in range(NUM_OF_ROUNDS):
        question, correct_answer = game.form_task_and_answer()
        print(f'Question: {question}')
        player_answer = prompt.string('Your answer: ')
        if str(correct_answer) == player_answer:
            print('Correct!')
        else:
            print(f"{player_answer} is wrong answer ;(.\n"
                  f"Correct answer was {correct_answer}\n"
                  f"Let's try again, {player_name}!")
            return
    print(f'Congratulations, {player_name}!')
