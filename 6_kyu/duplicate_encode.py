# 6 Kyu
# he goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

def duplicate_encode(word):
    result = ''
    word = word.lower()
    for char in word:
        if word.count(char) > 1:  # Jika char tersebut dudah lebih dari 1 di word
            result += ')'
        else:  # Jika hanya satu
            result += '('
    return result

# return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])


# print(duplicate_encode("din"), "(((")
# print(duplicate_encode("recede"), "()()()")
print(duplicate_encode("Success"), ")())())", "should ignore case")
# print(duplicate_encode("(( @"), "))((")
print(duplicate_encode("Pynzmwcxdme!a)@@y)lbkJS)xI"), "()(()(()()((()))))((((())(")
print(duplicate_encode("HH@HwHblcaHxPckOPbdal"), "))()())))))())(())())")
