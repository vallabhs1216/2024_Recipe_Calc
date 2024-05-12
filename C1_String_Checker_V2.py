# Checks that users enter a valid response (e.g.yes / no, kg / g / l / ml) based on a list of options

def string_checker(question, num_letters, valid_responses, error):
    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print(error)
        print()


# Main routine starts here
yes_no_list = ["yes", "no"]
units_list = ["kg", "grams", "litres", "ml", "kilograms", "millilitres"]

for case in range(0, 1):
    want_instructions = string_checker("Do you want to read the instructions (y/n): ", 1,
                                       yes_no_list, "Please choose Yes or No")

    print("You chose", want_instructions)

for case in range(0, 5):
    units = string_checker("Choose the units of the item: kilograms (kg), grams (g), litres (L),"
                           " millilitres (ml): ", 1, units_list, "Please choose Kg, g, L, or ml")
    if units == "millilitres":
        units = "ml"
    elif units == "kilograms":
        units = "kg"
    print("You chose", units)
