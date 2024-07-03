# import libraries
import pandas


# Functions go here

# instructions go here
def show_instructions():
    print("🍕Welcome to the Recipe Calculator🍕")
    print()
    print("Please start by entering your recipe name and amount of servings it makes.")
    print("And the total amount of ingredients you are using.")
    print()
    print("You can then start entering information about each ingredient,")
    print("You will be asked:")
    print()
    print("Ingredients name,")
    print()
    print("The unit it was bought in (Kg, g, mL, L), ")
    print("and the amount of the ingredient bought,")
    print()
    print("The unit of how much you used (Kg, g, mL, L),")
    print("and the amount of the ingredient used.")
    print()
    print("How much it cost to buy the ingredient.")


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

# List
yes_no_list = ["yes", "no"]
units_list = ["kg", "grams", "litres", "ml", "kilograms", "millilitres"]

# Lists to hold ingredient details
ingredients_list = []
amount_list = []
unit_bought_list = []
amount_used_list = []
unit_used_list = []
cost_list = []
cost_to_make_list = []

# Dictionary used to create data frame
recipe_cost_dict = {
    "Ingredients": ingredients_list,
    "Amount": amount_list,
    "Unit Bought": unit_bought_list,
    "Amount Using": amount_used_list,
    "Unit Used": unit_used_list,
    "Cost": cost_list,
    "Cost To Make": cost_to_make_list
}

# Ask user if the want instructions
Instructions = string_checker("Do you want to see the instructions? ", 1, yes_no_list, "Please enter yes or no. ")

# Set maximum number of ingredients below
MAX_INGREDIENTS = num_check("How many ingredients are you using? ", "Please enter a number more than 0\n", int)
ingredients_listed = 0

# Get recipe name
recipe_name = not_blank("Recipe name: ", "The recipe name can't be blank.")

servings = num_check("How many servings does this recipe make? ", "Please enter a number more than 0\n", int)
# Loop to get information for list

while ingredients_listed < MAX_INGREDIENTS:
    # Get ingredient names
    ingredients = not_blank("\nIngredient: ", "The component can't be blank.")

    if ingredients == 'xxx' and len(ingredients_list) > 0:
        break
    elif ingredients == 'xxx':
        print("You must write down at least ONE ingredient before quitting")
        continue
    # Asks for units bought, amount, cost, unit used, amount using
    unit_bought = string_checker("What is the amount bought measurement unit? (Kg, g, ml, L)", 1, units_list,
                                 "Please choose Kg, g, L, or ml")

    amount = num_check(f"How much did you get of this ingredient ({unit_bought})? ",
                       "Please enter an amount more than 0\n", float)
    print(f"You bought {amount}{unit_bought}")
    unit_used = string_checker("What is the amount used measurement unit? (Kg, g, ml, L)? ", 1, units_list,
                               "Please choose Kg, g, L, or ml")

    using = num_check(f"How much are you using in the recipe? ({unit_used})", "Please enter an amount more than 0\n",
                      float)
    print(f"You used {using}{unit_used}")

    cost = num_check("How much did the amount bought cost? $", "Please enter a number more than 0\n",
                     float)
    print(f"You spent ${cost}")

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
total = ingredient_frame['Cost To Make'].sum()
per_serve = total / servings

ingredient_frame['Cost To Make'] = ingredient_frame['Cost To Make'].apply(currency)
ingredient_frame['Cost'] = ingredient_frame['Cost'].apply(currency)
# Create String for To Write and Printing
ingredient_string = ingredient_frame.to_string(index=False)

Heading = f"=== {recipe_name} ===\n"
Servings = f"*** Servings: {servings} ***\n"
total = f"\nTotal Cost: ${total:.2f}\n"
per_serve = f"Cost Per Serve: ${per_serve:.2f}"

# Ask user for file name
filename = input("Please enter a file name: ")
if filename == "":
    filename = recipe_name

to_write = [Heading, Servings, ingredient_string, total, per_serve]

# Print output
for item in to_write:
    print(item)

# Write output to file
# Create file to hold data (add .txt extension)
write_to = f"{filename}.txt"
text_file = open(write_to, "w+")

for item in to_write:
    text_file.write(item)
    text_file.write("\n")

# Close file
text_file.close()

print()
