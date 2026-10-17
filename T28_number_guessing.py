import random

lowest_num = 1
highest_num = 500
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("py num guessing game")
print(f"select a num between {lowest_num} and {highest_num}")

while is_running:

    guess = input("enter your guess: \n")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("out of range")
            print(f"please select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("too low")
        elif guess > answer:
            print("too high")
        else:
            print(f"correct, answer:{answer}")
            print(f"number of guesses: {guesses}")
            is_running = False
    else:
        print("invalid guess")
        print(f"please select a number between {lowest_num} and {highest_num}")