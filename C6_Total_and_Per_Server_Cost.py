import pandas


# currency formatting function
def currency(x):
    return f"${x:.2f}"


# lists to hold ingredient details
ingredients_list = ["a", "b", "c", "d", "e", "f"]
amount_list = [1, 2, 5, 10, 3, 2]
unit_bought_list = ["kg", "kg", "l", "kg", "l", "l"]
amount_used_list = [0.5, 1, 3, 2, 2, 1]
unit_used_list = ["kg", "kg", "l", "kg", "l", "l"]
cost_list = [10, 20, 10, 20, 30, 10]
cost_to_make_list = [5, 10, 6, 4, 20, 5]

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

servings = 2
recipe_name = "Pizza"
filename = "Pizza"

# Create data frame from dictionary to organise information
ingredient_frame = pandas.DataFrame(recipe_cost_dict)

# Calculate the total ticket cost (ticket + surcharge)

# Calculate ticket and profit totals
total = ingredient_frame['cost to make'].sum()
per_serve = total / servings

ingredient_string = pandas.DataFrame.to_string(ingredient_frame)

total = f"\nTotal cost: ${total}\n"
per_serve = f"\nCost Per Serving: ${per_serve}"

# List holding content to print / write file
to_write = [recipe_name, ingredient_string, total, per_serve]

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

