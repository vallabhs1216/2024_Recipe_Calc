def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)

        if response.strip() == "":
            print(error)
        else:
            return response


for case in range(1, 4):
    recipe_name = not_blank("Recipe name: ", "The recipe name can't be blank.")
