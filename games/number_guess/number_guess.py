import random
import math

MAX_SECRET = 100

secret = random.randint(1, MAX_SECRET)
current_turn = 1
latest_guess = 0
max_turns = int(math.ceil(math.log2(MAX_SECRET))) + 1

print("I thought of a number between 1 and {}, try to guess it!".format(MAX_SECRET))

while latest_guess != secret and current_turn <= max_turns:
    try:
        latest_guess = int(input("Turn {}/{}. Your guess: ".format(current_turn, max_turns)))
    except Exception:
        print("Please enter numbers only.")
        continue
        
    if latest_guess < secret:
        print("That is a too small number!")
    elif latest_guess > secret:
        print("That is a too large number!")
    current_turn = current_turn + 1

if latest_guess == secret:
    print("Congratualtions, it took you {} turns to guess the number {}".format(current_turn - 1, secret))
else:
    print("Sorry, you ran out of tries. Better luck next time!")
