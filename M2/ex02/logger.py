#!/usr/bin/env python


import time
from random import randint
import os


def log(function):
    def wrapper(self, *args, **kwargs):
        timer = time.time()
        logfile = open("machine.log", "a+")
        result = function(self, *args, **kwargs)
        user = os.environ.get('USER')
        action = function.__name__.replace("_", " ").title()
        timer = time.time() - timer
        if (timer < 0.001):
            logfile.write("({})Running: {:19s}[ exec-time = {:.3f} ms ]\n"
                          .format(user, action, timer * 1000))
        else:
            logfile.write("({})Running: {:19s}[ exec-time = {:.3f} s ]\n"
                          .format(user, action, timer))
        logfile.close
        return result
    return wrapper


class CoffeeMachine():

    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.01)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5)*0.01)
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
