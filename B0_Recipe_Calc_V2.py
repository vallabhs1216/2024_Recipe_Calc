# import libraries
import pandas


# Functions go here

# instructions go here
def show_instructions():
    print('')


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


# checks if input is valid
def string_checker(question, num_letters, valid_responses, error):
    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print(error)
        print()


# checks input is not blank
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
filename = recipe_name

servings = num_check("How many servings does this recipe make? ", "Please enter a number more than 0\n", int)
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
    unit_bought = string_checker("What is the amount bought measurement unit? (Kg, g, ml, L)", 1, units_list,
                                 "Please choose Kg, g, L, or ml")
    print(f"You chose {unit_bought}")
    amount = num_check(f"How much did you get of this ingredient ({unit_bought})? ",
                       "Please enter an amount more than 0\n", float)
    print(f"You bought {amount}{unit_bought}")
    cost = num_check("How much did it cost? $", "Please enter a number more than 0\n",
                     float)
    print(f"You spent ${cost}")
    unit_used = string_checker("What is the amount used measurement unit? (Kg, g, ml, L)", 1, units_list,
                               "Please choose Kg, g, L, or ml")
    print(f"You used {unit_used}")

    using = num_check(f"How much are you using in the recipe? ({unit_used})", "Please enter an amount more than 0\n",
                      float)

    if unit_bought or unit_used == "millilitres":
        units = "ml"
    elif unit_bought or unit_used == "kilograms":
        units = "kg"

    # Adds to lists
    ingredients_list.append(ingredients)
    amount_list.append(amount)
    unit_bought_list.append(unit_bought)
    amount_used_list.append(using)
    unit_used_list.append(unit_used)
    cost_list.append(cost)

    if unit_bought in ["kg", "litres"]:
        amount *= 1000

    elif unit_used in ["kg", "litres"]:
        using *= 1000

    # Cost of the amount of ingredients used
    cost_to_make = cost / amount
    cost_to_make *= using

    cost_to_make_list.append(cost_to_make)

# *** Printing and Extra Calculation Area ***
ingredient_frame = pandas.DataFrame(recipe_cost_dict)

# Calculate Total and Per Server Costs
total = ingredient_frame['cost to make'].sum()
per_serve = total / servings

# Create String for To Write and Printing
ingredient_string = pandas.DataFrame.to_string(ingredient_frame)

to_write = [ingredient_string]

# Print output
for item in to_write:
    print(item)

# write output to file
# Create file to hold data (add .txt extension)
write_to = f"{filename}.txt"
text_file = open(write_to, "w+")

for item in to_write:
    text_file.write(item)
    text_file.write("\n")

# Close file
text_file.close()

print()
