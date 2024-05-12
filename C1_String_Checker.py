# Checks that users enter a valid response (e.g.yes / no, kg / g / l / ml) based on a list of options

def string_checker(question, num_letters, valid_responses):
    error = f"Please choose {valid_responses[0]}, {valid_responses[1]}"

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print(error)


# Main routine starts here
yes_no_list = ["yes", "no"]
units_list = ["kilograms", "grams", "litres", "millilitres"]

for case in range(0, 4):
    want_instructions = string_checker("Do you want to read the instructions (y/n): ", 1, yes_no_list)

    print("You chose", want_instructions)

for case in range(0, 4):
    units = string_checker("Choose the units of the item (kg, g, l, ml): ", 1, units_list)

    print("You chose", units)
