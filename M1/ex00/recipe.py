from typing import List


class Recipe:
    """The class Recipe contains 6 attributes:
    - name (str)
    - cooking_level (int): from 1 to 5
    - cooking_time (int): positive minute
    - ingredients (list[str])
    - recipe_type ("starter", "lunch", "dessert")
    - description (str): can be empty"""
    __RECIPE_TYPE = ("starter", "lunch", "dessert")

    def __verify_name(self, name: str) -> str:
        """the name must be a string and cannot be empty"""
        if not isinstance(name, str):
            raise TypeError("Expected str. Got " + str(type(name)))
        elif name == '':
            raise ValueError("Cannot be empty")
        return name

    def __verify_cooking_level(self, cooking_level: int) -> int:
        """the level must be an int between 1 and 5"""
        if not isinstance(cooking_level, int):
            raise TypeError("Expected int. Got " + str(type(cooking_level)))
        elif cooking_level < 1 or cooking_level > 5:
            raise ValueError("Must be between 1 and 5")
        return cooking_level

    def __verify_time(self, cooking_time: int) -> int:
        """the time must be a positive int"""
        if not isinstance(cooking_time, int):
            raise TypeError("Expected int. Got " + str(type(cooking_time)))
        elif cooking_time < 0:
            raise ValueError("Must be positive")
        return cooking_time

    def __verify_ingredient(self, ingredients: List[str]) -> List[str]:
        """the ingredients must be provided in a non-empty string list"""
        if not isinstance(ingredients, list):
            raise TypeError("Expected list. Got " + str(type(ingredients)))
        elif len(ingredients) == 0:
            raise ValueError("Cannot be empty")
        for elem in ingredients:
            if not isinstance(elem, str):
                raise TypeError("Expected str. Got " + str(type(elem)))
        return ingredients

    def __verify_recipe_type(self, recipe_type: str) -> str:
        """recipe type is either a starter, lunch, or dessert"""
        if not isinstance(recipe_type, str):
            raise TypeError("Expected str. Got " + str(type(recipe_type)))
        if recipe_type not in Recipe.__RECIPE_TYPE:
            raise ValueError("Unexpected type")
        return recipe_type

    def is_recipe_type(recipe_type: str) -> bool:
        if not isinstance(recipe_type, str):
            return False
        if recipe_type not in Recipe.__RECIPE_TYPE:
            return False
        return True

    def __init__(self, name: str, cooking_level: int,
                 cooking_time: int, ingredients: List[str],
                 recipe_type: str, description: str = ""):
        self.name: str = self.__verify_name(name)
        self.cooking_level: int = self.__verify_cooking_level(cooking_level)
        self.cooking_time: int = self.__verify_time(cooking_time)
        self.ingredients: List[str] = self.__verify_ingredient(ingredients)
        self.recipe_type: str = self.__verify_recipe_type(recipe_type)
        self.description: str = description if \
            isinstance(description, str) else "<TypeError>"

    def __str__(self) -> str:
        txt: str = "Recipe for '" + self.name + "':\n"
        txt = txt + "- Best served for " + self.recipe_type + "\n"
        txt = txt + "- Difficulty level: " + str(self.cooking_level) + "/5\n"
        txt = txt + "- Preparation time: " + str(self.cooking_time) + "m\n"
        txt = txt + "- Description:\n\t" + self.description + "\n"
        txt = txt + "- Ingredients:\n"
        for elem in self.ingredients:
            txt = txt + "\t" + elem + "\n"
        return txt

    def __repr__(self):
        return str(self.__dict__)
