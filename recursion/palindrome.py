def ispalindrome(input):
    if len(input) == 0 or len(input) == 1:
        return True
    
    if input[0] == input[len(input)-1]:
        return ispalindrome(input[1:len(input)-1])
    
    return False

print(ispalindrome("racecar"))
print(ispalindrome("kayak"))
print(ispalindrome("hello"))
print(ispalindrome(""))
