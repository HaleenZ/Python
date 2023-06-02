import random

random_number = random.randint(1, 9)

guess = int(input("Guess the number (between 1 and 9): "))

if guess < random_number:
    print("Too low!")
elif guess > random_number:
    print("Too high!")
else:
    print("Exactly right! Congratulations!")
