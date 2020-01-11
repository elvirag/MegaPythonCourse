user_input = ''
questions = ["why", "how", "where", "who", "which", "when", "what", "are", "is", "am"]

res = ''
while True:
    user_input = input("Say something: ")
    if user_input != "\\end":
        res += user_input.capitalize()
        # check if it's a question
        if user_input.split(" ")[0].lower() in questions:
            res += "? "
        else:
            res += ". "

    else:
        break

print(res)
