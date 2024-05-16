# import libraries
import pandas


# functions go here

# instructions go here
def show_instructions():
    print('')


# *** functions go here ***

# checks that input is either a float or an
# integer that is more than zero. takes in custom error messages
def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


def string_checker(question, num_letters, valid_responses, error):
    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print(error)
        print()


def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)

        if response.strip() == "":
            print(error)
        else:
            return response


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# Functions go here

# Main routine goes here

# list
yes_no_list = ["yes", "no"]
units_list = ["kg", "grams", "litres", "ml", "kilograms", "millilitres"]

# lists to hold ingredient details
ingredients_list = []
amount_list = []
unit_bought_list = []
amount_used_list = []
unit_used_list = []
cost_list = []
cost_to_make_list = []

# Dictionary used to create data frame ie: column_name:list
recipe_cost_dict = {
    "ingredients": ingredients_list,
    "amount": amount_list,
    "unit bought": unit_bought_list,
    "amount using": amount_used_list,
    "unit used": unit_used_list,
    "cost": cost_list,
    "cost to make": cost_to_make_list
}

# set maximum number of ingredients below
MAX_INGREDIENTS = 99
ingredients_listed = 0

# get recipe name
recipe_name = not_blank("Recipe name: ", "The recipe name can't be blank.")

# Loop to get information for table

while ingredients_listed < MAX_INGREDIENTS:
    # Get ingredient names
    ingredients = not_blank("\nIngredient: ", "The component can't be blank.")

    if ingredients == 'xxx' and len(ingredients_list) > 0:
        break
    elif ingredients == 'xxx':
        print("You must write down at least ONE ingredient before quitting")
        continue
    # Asks for
    unit_bought = string_checker("What is the ingredients measurement unit? (Kg, g, ml, L)", 1, units_list,
                                 "Please choose Kg, g, L, or ml")

    amount = num_check(f"How much did you get of this ingredient ({unit_bought})? ",
                       "Please enter an amount more than 0\n", float)

    cost = num_check("How much does it cost (for the amount you bought)? $", "Please enter a number more than 0\n",
                     float)

    unit_used = string_checker("What is the amount used measurement unit? (Kg, g, ml, L)", 1, units_list,
                               "Please choose Kg, g, L, or ml")

    if unit_bought or unit_used == "millilitres":
        units = "ml"
    elif unit_bought or unit_used == "kilograms":
        units = "kg"

    using = num_check(f"How much are you using in the recipe? ({unit_used})", "Please enter an amount more than 0\n",
                      float)

    if unit_bought or unit_used == "kg" or "kilograms":
        amount = amount * 1000
        using = using * 1000
    elif unit_bought or unit_used == "l" or "litres":
        amount = amount * 1000
        using = using * 1000

    # Cost of the amount of ingredients used
    cost_to_make = cost / amount
    cost_to_make = cost_to_make * using

    ingredients_listed += 1

    # Adds to lists
    ingredients_list.append(ingredients)
    amount_list.append(amount)
    unit_bought_list.append(unit_bought)
    amount_used_list.append(using)
    unit_used_list.append(unit_used)
    cost_list.append(cost)
    cost_to_make_list.append(cost_to_make)
