from datetime import datetime
from recipe import Recipe
from typing import List, Optional


class Book:
    """The class Book contains 4 attributes:
    - name (str)
    - last_update (datetime)
    - creation_date (datetime)
    - recipe_list (dict)"""
    def __verify_name(self, name: str) -> str:
        """the name must be a string (None not supported: \
type is displayed in the subject)"""
        if not isinstance(name, str):
            raise TypeError("Expected str. Got " + str(type(name)))
        return (name)

    def __init__(self, name: str = ""):
        self.name: str = self.__verify_name(name)
        self.last_update: datetime = datetime.now()
        self.creation_date: datetime = self.last_update
        self.recipe_list: dict = {"starter": [], "lunch": [], "dessert": []}

    def add_recipe(self, recipe: Recipe):
        """Add a recipe to the book and update last_update"""
        if not isinstance(recipe, Recipe):
            raise TypeError("Expected Recipe. Got " + str(type(recipe)))
        if not Recipe.is_recipe_type(recipe.recipe_type):
            raise TypeError("Unsupported recipe type")
        self.recipe_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()

    def get_recipe_by_name(self, name: str) -> Optional[Recipe]:
        """Prints a recipe content from its name and returns the instance"""
        if not isinstance(name, str):
            raise TypeError("Expected str. Got " + str(type(name)))
        elem: Recipe
        value: List[Recipe]
        for value in self.recipe_list.values():
            for elem in value:
                if (elem.name == name):
                    print(elem)
                    return elem
        print("Recipe not found")
        return None

    def get_recipes_by_types(self, recipe_type: str) -> List[Recipe]:
        """Get all recipe names for a given recipe_type """
        if not isinstance(recipe_type, str):
            raise TypeError("Expected str. Got " + str(type(recipe_type)))
        for key, value in self.recipe_list.items():
            if key == recipe_type:
                return value
        return []

    def __str__(self) -> str:
        txt: str = "Cookbook '" + self.name + "':\n"
        txt = txt + "- Creation date: " + str(self.creation_date) + "\n"
        txt = txt + "- Last update: " + str(self.last_update) + "\n"
        return (txt)

    def __repr__(self) -> str:
        return str(self.__dict__)
