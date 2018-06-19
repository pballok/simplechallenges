min_secret = 1
max_secret = 100

def guess_one(turn, min_value, max_value):
    guess = (min_value + max_value) // 2
    
    answer = input("Turn {}. Is it {}? Enter 'h' for too high, 'l' for too low or 'c' for correct: ".format(turn, guess))

    if answer[0] == 'h' or answer[0] == 'H':
        guess_one(turn + 1, min_value, guess - 1)
    elif answer[0] == 'l' or answer[0] == 'L':
        guess_one(turn + 1, guess + 1, max_value)
    elif answer[0] == 'c' or answer[0] == 'C':
        print("Cool! Thanks for playing!")
    else:
        print("Please answer with either 'h', 'l' or 'c'")
        guess_one(turn, min_value, max_value)

input("Think of a number between {} and {}. Press ENTER when ready.".format(min_secret, max_secret))

guess_one(1, min_secret, max_secret)
