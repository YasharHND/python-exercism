""" this is blah blah blah """

from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    return tuple((dish_name, set(dish_ingredients)))


def check_drinks(drink_name, drink_ingredients):
    alcoholic = {
        "liqueur",
        "gin",
        "whiskey",
        "scotch",
        "vodka",
        "rum",
        "vermouth",
        "tequila",
        "bourbon"
    }
    return drink_name + (" Cocktail" if any(any(drink in ingredient.lower().split(" ") for drink in alcoholic) for ingredient in drink_ingredients) else " Mocktail")


def categorize_dish(dish_name, dish_ingredients):
    categories = {
        "VEGAN": VEGAN,
        "VEGETARIAN": VEGETARIAN,
        "KETO": KETO,
        "PALEO": PALEO,
        "OMNIVORE": OMNIVORE,
        "ALCOHOLS": ALCOHOLS,
        "SPECIAL_INGREDIENTS": SPECIAL_INGREDIENTS
    }
    for category, category_ingredients in categories.items():
        if all(dish_ingredient in category_ingredients for dish_ingredient in dish_ingredients):
            return dish_name + ": " + category
    return None


def tag_special_ingredients(dish):
    return dish[0], {item for item in set(dish[1]) if item in SPECIAL_INGREDIENTS}


def compile_ingredients(dishes):
    master_list = set({})
    for dish in dishes:
        master_list.update(dish)
    return master_list


def separate_appetizers(dishes, appetizers):
    return set(dishes).symmetric_difference(set(appetizers))


def singleton_ingredients(dishes, intersection):
    unique = set({})
    for dish in dishes:
        unique.update(dish)
    return unique.symmetric_difference(intersection)
