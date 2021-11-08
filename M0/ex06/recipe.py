#!/usr/bin/env python

cookbook = {
            "sandwich": {"ingredients": {"ham", "bread", "cheese", "tomatoes"},
                         "meal": "lunch",
                         "prep_time": 10},
            "cake": {"ingredients": {"flour", "sugar", "eggs"},
                     "meal": "dessert",
                     "prep_time": 60},
            "salad": {"ingredients": {"avocado", "arugula", "tomatoes",
                                      "spinach"},
                      "meal": "lunch",
                      "prep_time": 15},
}


def cookbook_content():
    num = 0
    for recipe in cookbook:
        num = num + 1
        print("Recipe", num, "is:", recipe)
    print("")


def print_recipe(recipe):
    try:
        length = len(cookbook[recipe]['ingredients'])
        print("Recipe for ", recipe, ":", sep='')
        print("Ingredients list: [", sep='', end='')
        for i in cookbook[recipe]['ingredients']:
            length = length - 1
            print("'", i, "'", sep='', end='')
            if (length):
                print(", ", end='')
            else:
                print(']')
        print("To be eaten for ", cookbook[recipe]["meal"], ".", sep='')
        print("Takes", cookbook[recipe]["prep_time"], "minutes of cooking.")
    except KeyError:
        print("This recipe does not exists")
    print("")


def delete_recipe(recipe):
    try:
        del(cookbook[recipe])
        print("The recipe has been deleted")
    except KeyError:
        print("This recipe does not exists")
    print("")


def add_recipe(name, ingredients, meal, prep_time):
    if name not in cookbook.keys():
        cookbook[name] = {"ingredients": ingredients,
                          "meal": meal,
                          "prep_time": prep_time}
        print("The recipe '", name, "' has been added.")
    else:
        print("This recipe already exists")
    print("")


def add_recipe_main():
    name = input("Input a recipe name: ")
    ingredients = []
    print("Input ingredients (nothing to continue):")
    ingredient = input(">> ")
    while (ingredient != ''):
        ingredients.append(ingredient)
        ingredient = input(">> ")
    meal = print("Input meal type: ")
    meal = input(">> ")
    print("Input prep time: ")
    prep_time = input(">> ")
    if (prep_time == ''):
        prep_time = 0
    add_recipe(name, ingredients, meal, prep_time)


def print_menu(option):
    if (option != 0):
        print("Please select an option by typing the corresponding number:")
        print("1: Add a recipe")
        print("2: Delete a recipe")
        print("3: Print a recipe")
        print("4: Print the cookbook")
        print("5: Quit")
    text = input(">> ")
    print("")
    try:
        number = int(text)
        if (number < 1 or number > 5):
            number = 0
    except ValueError:
        number = 0
    return (number)


option = -1
while (option != 5):
    option = print_menu(option)
    if (option == 1):
        add_recipe_main()
    elif (option == 2):
        print("Please enter the recipe's name to delete it:")
        delete_recipe(input(">> "))
    elif (option == 3):
        print("Please enter the recipe's name to get its details:")
        print_recipe(input(">> "))
    elif (option == 4):
        cookbook_content()
    elif (option != 5):
        print("This option does not exist,"
              "please type the corresponding number.")
        print("To exit, enter 5.")
print("Cookbook closed.")
