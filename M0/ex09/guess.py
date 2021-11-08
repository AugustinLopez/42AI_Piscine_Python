#!/usr/bin/env python
from random import randint


num = randint(1, 99)
print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 "
      "to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!")
loop = 0
win = 0
stop = 0
while (stop == 0):
    loop = loop + 1
    print("What's your guess between 1 and 99?")
    text = input(">> ").lower()
    if (text == "exit"):
        print("Goodbye!")
        stop = 1
    else:
        try:
            answer = int(text)
        except ValueError:
            answer = -1
            print("That's not a number.")
            continue
        if (answer == num):
            win = 1
            stop = 1
        elif (answer < num):
            print("Too low!")
        else:
            print("Too high!")
if (win == 1):
    if (num == 42):
        print("The answer to the ultimate question of life, "
              "the universe and everything is 42.")
    if (loop != 1):
        print("Congratulations, you've got it!")
        print("You won in", loop, "attempts!")
    else:
        print("Congratulations! You got it on your first try!")
