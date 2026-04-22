import random

number = random.randint(1, 10)
guess = 0
for guess in range(1, 10):
    while guess != number:
        guess = int(input("Enter the number"))

        if guess == number:
            print("You won")
        elif guess < number:
            print("Number is greater")
        elif guess > number:
            print("NUmber is less")
