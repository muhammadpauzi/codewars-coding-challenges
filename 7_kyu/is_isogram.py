def is_isogram(string):
    for s in string.lower():
        if string.lower().count(s) > 1:
            return False
    return True


print(is_isogram("Dermatoglyphics"), True)
print(is_isogram("isogram"), True)
print(is_isogram("aba"), False, "same chars may not be adjacent")
print(is_isogram("moOse"), False, "same chars may not be same case")
print(is_isogram("isIsogram"), False)
print(is_isogram(""), True, "an empty string is a valid isogram")
