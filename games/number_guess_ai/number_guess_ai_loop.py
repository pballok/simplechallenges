min_secret = 1
max_secret = 1000

turn = 1

input("Think of a number between {} and {}. Press ENTER when ready.".format(min_secret, max_secret))

while True:
    guess = (min_secret + max_secret) // 2
    answer = input("Turn {}. Is it {}? Enter 'h' for too high, 'l' for too low or 'c' for correct: ".format(turn, guess))
    if answer[0] == 'h' or answer[0] == 'H':
        turn = turn + 1
        max_secret = guess - 1
    elif answer[0] == 'l' or answer[0] == 'L':
        turn = turn + 1
        min_secret = guess + 1
    elif answer[0] == 'c' or answer[0] == 'C':
        break
    else:
        print("Please answer with either 'h', 'l' or 'c'")

print("Cool! Thanks for playing!")
