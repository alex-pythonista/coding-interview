def findbinary(input):
    if input == 0:
        return "0"
    if input == 1:
        return "1"
    
    return findbinary(input // 2) + str(input % 2)

print(findbinary(11))
