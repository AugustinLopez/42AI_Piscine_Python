#!/usr/bin/env python
from book import Book
from recipe import Recipe


def recipe_test(a, b, c, d, e, f="", book=None) -> Recipe:
    ret = None
    try:
        ret = Recipe(a, b, c, d, e, f)
        print(ret)
    except ValueError as e:
        print("<Value Error>", e)
    except TypeError as e:
        print("<Type Error>", e)
    return ret


def book_test(name="") -> Book:
    ret = Book()
    try:
        ret = Book(name)
    except ValueError as e:
        print("<Value Error>", e)
    except TypeError as e:
        print("<Type Error>", e)
    return ret

def part1():
    print("\033[33m RECIPE ERROR:\033[0m")
    test = recipe_test(1, 0, -1, 4, 5)
    test = recipe_test("", 0, -1, 4, 5)
    test = recipe_test("a", 0, -1, 4, 5)
    test = recipe_test("a", -1, -1, 4, 5)
    test = recipe_test("a", 6, -1, 4, 5)
    test = recipe_test("a", 1.0, -1, 4, 5)
    test = recipe_test("a", 2, -1, 4, 5)
    test = recipe_test("a", 2, 1e07, 4, 5)
    test = recipe_test("a", 2, 3, [], 5)
    test = recipe_test("a", 2, 3, [2], 5)
    test = recipe_test("a", 2, 3, [""], 5)
    test = recipe_test("a", 2, 3, [""], "")
    test = recipe_test("a", 2, 3, [""], "blabla")
    test = recipe_test("cooki", 0, 10, ["dough", "sugar", "love"], "dessert", "deliciousness incarnate")
    test = recipe_test("cooki", 1.5, 10, ["dough", "sugar", "love"], "dessert", "deliciousness incarnate",)
    test = recipe_test("cooki", 1, 10, [], "deliciousness incarnate", "dessert")

    print()

def part2():
    print("\033[33m RECIPE VALID:\033[0m")
    test = recipe_test("tourte", 1, 60, ["milk", "egg", "flour", "salt"], "lunch")
    print()
    test = recipe_test("cooki", 1, 10, ["dough", "sugar", "love"], "dessert", "deliciousness incarnate")

def part3():
    print("\033[33m BOOK ERROR:\033[0m")
    book = book_test(1)

def part4() -> Book:
    print("\033[33m BOOK VALID:\033[0m")
    mybook = book_test("")
    mybook = book_test("My Book")
    print(mybook)
    crumble = Recipe("Crumble" , 1, 25, ["apples", "flour", "sugar"],
                     "dessert", "delicious")
    mybook.add_recipe(crumble)
    mybook.add_recipe(Recipe("cooki", 1, 10, ["dough", "sugar", "love"],
                             "dessert", "delicious"))
    mybook.add_recipe(Recipe("tourte", 1, 60, ["milk", "egg", "flour", "salt"],
                             "lunch"))
    mybook.add_recipe(Recipe("tourte", 1, 60, ["milk", "egg", "flour", "salt"],
                             "lunch"))
    print(mybook.last_update)
    return mybook


def part5(myBook: Book):
    print("\033[33m BOOK GET_RECIPE_BY_NAME:\033[0m")
    recipe = myBook.get_recipe_by_name("Crumble")
    print(recipe)
    recipe = myBook.get_recipe_by_name("Liver Icecream")
    print(recipe)


def part6(myBook: Book):
    print("\033[33m BOOK GET_RECIPES_BY_TYPES:\033[0m")
    print(myBook.get_recipes_by_types("dessert"))
    print(myBook.get_recipes_by_types("dessert")[0])
    print(myBook.get_recipes_by_types("asdasd"))


part1()
part2()
part3()
myBook = part4()
part5(myBook)
part6(myBook)
