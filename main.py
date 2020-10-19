import cows_bulls_functions as func
import time

greeting = 'Hi there!'
lets_start = 'Enter a number'
lets_end = 'That\'s '
time_info1 = 'It took you '
time_info2 = ' to finish the game'
digits = 4


if __name__ == '__main__':
    start_time = time.time()
    print(greeting)
    number = func.generate_digits(digits)
    # TODO: hide print(number)
    print(number)
    print(lets_start)

    # set initial variables
    round_number = 0
    game_continues = True

    # play game till the number is guessed
    while game_continues:
        round_number += 1
        guess = func.get_guess(digits)
        game_continues = func.guess_eval(number, guess, round_number)  # now returns false

    # final message
    game_evaluation = func.game_evaluation_create_dict()
    print(lets_end + game_evaluation.get(round_number, 'pretty bad'))

    # game time message
    game_time = func.calc_time(start_time)
    print(time_info1 + game_time + time_info2)

