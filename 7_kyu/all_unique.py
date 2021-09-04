def has_unique_chars(string):
    for s in string.lower():
        if string.count(s) > 1:
            return False
    return True

# Best Solution
# def has_unique_chars(s):
    # return len(s) == len(set(s))

# print(has_unique_chars("abcdef"),True)
# print(has_unique_chars("++-"),False)
# print(has_unique_chars("  nAa"),False)
