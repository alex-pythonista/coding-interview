def revstring(input: str):
    # what is the base case? or when can I no longer continue?
    if input == "":
        return ""

    return revstring(input[1:]) + input[0]

print(revstring("hello"))
