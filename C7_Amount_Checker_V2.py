def amount_and_unit(question, valid_units, num_letters):
    while True:
        user_input = input(question).strip().lower()

        # Find where the units start
        i = 0
        while i < len(user_input) and (user_input[i].isdigit() or user_input[i] == '.'):
            i += 1

        if i > 0:
            amount = user_input[:i]
            unit = user_input[i:].strip()

            # Check if amount is a valid number
            try:
                amount = float(amount)
            except ValueError:
                print("Invalid input. Amount should be a valid number.")
                continue

            # Check if unit is in the valid list (allowing both long and short forms)
            valid = False
            for valid_unit in valid_units:
                if unit == valid_unit.lower() or unit == valid_unit[:num_letters].lower():
                    unit = valid_unit
                    valid = True
                    break

            if valid:
                return amount, unit
            else:
                print(f"Invalid unit. Please use a valid unit from: {', '.join(valid_units)}")

        else:
            print("Invalid format. Please enter in the format {amount}{unit} e.g '100g' ")


# Example usage:
units_list = ["kg", "litres", "ml", "kilograms", "grams", "millilitres", "" ]  # Include both long and short forms
for case in range(1, 5):
    amount, unit = amount_and_unit("How much did you use? (kg, g, l, ml, leave blank if no unit): ", units_list, 1)
    print(f"Amount: {amount}")
    print(f"Unit: {unit}")
