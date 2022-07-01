import prompt


NUM_OF_ROUNDS = 3


def please_go_game(game):
    print('Welcome to the Brain Games!')
    player_name = prompt.string('May i have your name? ')
    print('Hello, ' + player_name + '!')
    print(game.DESCRIPT)
    for i in range(NUM_OF_ROUNDS):
        question, correct_answer = game.form_task_and_answer()
        print('Question: ' + question)
        player_answer = prompt.string('Your answer: ')
        if str(correct_answer) == player_answer:
            print('Correct!')
        else:
            print(player_answer, ' is wrong answer ;(.')
            print('Correct answer was ' + str(correct_answer))
            print("Let's try again, " + player_name + '!')
            return
    print('Congratulations, ' + player_name + '!')
