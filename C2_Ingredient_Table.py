# import libraries
import pandas


# functions go here

# instructions go here
def show_instructions():
    print('''\n
***** Instructions *****

This program will ask you for ...
- The name of the recipe you are using
- The names of the ingredients you are using
- How much of it you plan on using
- The costs for the amount of servings you plan to make
- How much it will cost per serving

It will then output an itemised list of the costs 
with subtotals for the variable and fixed costs.
Finally it will tell you how much you should use of 
each item for you to reach your serving goal.

**** Program Launched! ****''')


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


def string_checker(question, valid_responses):
    error = "Please choose one of the following options: {}".format(", ".join(valid_responses))

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:len(response)]:
                return item

        print(error)


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


# main routine goes here

# list
yes_no_list = ["yes", "no"]
units_list = ["kg", "grams", "litres", "ml", "kilograms", "millilitres"]

# lists to hold ingredient details
ingredients_list = []
amount_list = []
amount_used_list = []
cost_list = []
unit_list = []
amount_needed_list = []

# Dictionary used to create data frame ie: column_name:list
recipe_cost_dict = {
    "Ingredients": ingredients_list,
    "Amount": amount_list,
    "Amount using": amount_used_list,
    "Cost": cost_list,
    "Unit": unit_list,
    "Amount Needed": amount_needed_list
}

# set maximum number of ingredients below
MAX_INGREDIENTS = 99
ingredients_listed = 0

# get recipe name
recipe_name = not_blank("Recipe name: ", "The recipe name can't be blank.")

# loop to get component, quantity and price
# ingredient_name = ""
get_ingredient_price = 0
while ingredients_listed < MAX_INGREDIENTS:
    # get ingredient name
    ingredients = not_blank("\nIngredient: ", "The component can't be blank.")

    if ingredients == 'xxx' and len(ingredients_list) > 0:
        break
    elif ingredients == 'xxx':
        print("You must write down at least ONE ingredient before quitting")
        continue

    amount = num_check(f"How much did you get of this ingredient? ",
                       "Please enter an amount more than 0\n", float)
    cost = num_check("How much does it cost (for the amount you bought)? $", "Please enter a number more than 0\n",
                     float)
    using = num_check("How much are you using in the recipe?)" ,"Please enter an amount more than 0\n", float)

    # cost needed for AMOUNT of ingredients USED in recipe
    needed1 = cost / amount
    needed = needed1 * using

    ingredients_listed += 1

    # add to list in order to print out
    all_ingredients.append(ingredients)
    all_amount.append(amount)
    all_using.append(using)
    all_cost.append(cost)
    all_unit.append(unit)
    all_texture.append(texture)
    all_needed.append(needed)