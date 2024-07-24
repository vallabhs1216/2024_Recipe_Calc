def separate_units(amount):
    # Convert amount to string to easily manipulate
    amount_str = str(amount)

    # Check if the amount contains a decimal point
    if '.' in amount_str:
        integer_part, decimal_part = amount_str.split('.')
        units = decimal_part
    else:
        integer_part = amount_str
        units = ''

    return integer_part, units


# Example usage:
amount = 123.45
integer_part, units = separate_units(amount)
print(f"Integer part: {integer_part}")
print(f"Units: {units}")
