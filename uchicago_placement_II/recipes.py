from abc import ABC, abstractmethod
from typing import Optional

# Helper function to check whether two floats are equal
def check_floats_equal(f1: float, f2: float) -> bool:
    return abs(f1 - f2) < 0.001

class Ingredient(ABC):
    """
    Abstract base class to represent an ingredient.

    Attributes:
        name (str)
        amount (float)

    Methods:
        can_scale_by (bool)
        adjust_amount (Ingredient)
    """

    def __init__(self, name: str, amount: float):
        self.name = name
        self.amount = amount

    @abstractmethod
    def can_scale_by(self, factor: float) -> bool:
        raise NotImplementedError

    @abstractmethod
    def adjust_amount(self, amount: float) -> "Ingredient":
        raise NotImplementedError


class Unit(Ingredient):
    """
    Class to represent a unit ingredient.
    """

    def can_scale_by(self, factor: float) -> bool:
        # TODO: Write your solution here
        transformed_val = self.amount * factor
        return True if check_floats_equal(transformed_val, round(transformed_val)) else False

    def adjust_amount(self, amount: float) -> "Unit":
        # TODO: Write your solution here
        if check_floats_equal(amount, round(amount)):
            return Unit(self.name, amount)
        else:
            raise ValueError(f"{amount} is invalid inc")


class Weight(Ingredient):
    """
    Class to represent a weight ingredient.
    """

    def can_scale_by(self, factor: float) -> bool:
        # TODO: Write your solution here
        transformed_val = self.amount * factor
        return True if check_floats_equal(transformed_val / 0.1, round(transformed_val / 0.1)) else False

    def adjust_amount(self, amount: float) -> "Weight":
        # TODO: Write your solution here
        if check_floats_equal(amount / 0.1, round(amount / 0.1)):
            return Weight(self.name, round(amount, 1))
        else:
            raise ValueError(f"{amount} is invalid inc")


class Volume(Ingredient):
    """
    Class to represent a volume ingredient.
    """

    def can_scale_by(self, factor: float) -> bool:
        # TODO: Write your solution here
        transformed_val = self.amount * factor
        return True if check_floats_equal(transformed_val / 0.02, round(transformed_val / 0.02)) else False

    def adjust_amount(self, amount: float) -> "Volume":
        # TODO: Write your solution here
        if check_floats_equal(amount / 0.02, round(amount / 0.02)):
            return Volume(self.name, round(amount, 2))
        else:
            raise ValueError(f"{amount} is invalid inc")


class Recipe:
    """
    Class to represent a recipe.

    Attributes:
        name (str)
        ingredients (Dict[str, Ingredient])
        num_servings (int)

    Methods:
        can_scale_by (bool)
        scale_by (Recipe)
    """

    def __init__(
        self, name: str, ingredients: dict[str, Ingredient], num_servings: int):
        self.name = name
        self.ingredients = ingredients
        self.num_servings = num_servings

    def can_scale_by(self, total_servings: int) -> bool:
        # TODO: Write your solution here
        scale_factor = total_servings / self.num_servings
        for ingredient in self.ingredients.values():
            if ingredient.can_scale_by(scale_factor):
                continue
            else:
                return False
        return True    
        
    def scale_by(self, total_servings: int) -> "Recipe":
        assert self.can_scale_by(total_servings)
        # TODO: Write your solution here
        scale_factor = total_servings / self.num_servings
        scaled_ingredients = {}
        
        for name, ingredient in self.ingredients.items():
            scaled_ingredients[name] = ingredient.adjust_amount(ingredient.amount * scale_factor)
        
        return Recipe(self.name, scaled_ingredients, total_servings)


def make_recipe(recipe: Recipe, pantry: dict[str, Ingredient]) -> dict[str, Ingredient]:
    """
    Given a recipe and a pantry of ingredients, determine whether or not the
    recipe can be made with the ingredients in the pantry. 

    Args:
        recipe: the recipe to make
        pantry: the ingredients available to make the recipe

    Returns: An updated pantry if the recipe can be made. Otherwise, return an empty dictionary.
    """
    # TODO: Write your solution here
    # check if can make
    for name, req_ingredient in recipe.ingredients.items():
        # base case
        if name not in pantry:
            return {} # no ingredient
        if pantry[name].amount < req_ingredient.amount:
            return {} # not enough ingredient

    # if can make, sub req-ed elts
    for name, req_ingredient in recipe.ingredients.items():
        pantry[name].amount -= req_ingredient.amount
        
    return pantry
