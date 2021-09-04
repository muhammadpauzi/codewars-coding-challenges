def get_count(input_str):
    return int(input_str.count("a")) + int(input_str.count("i")) + int(input_str.count("o")) + int(input_str.count("e")) + int(input_str.count("u"))

# Best Solution
# def getCount(inputStr):
#     return sum(1 for let in inputStr if let in "aeiouAEIOU")

print(get_count("abracadabra"), 5)
print(get_count(""), 0)
print(get_count("pear tree"), 4)
print(get_count("o a kak ushakov lil vo kashu kakao"), 13)
print(get_count("tk r n m kspkvgiw qkeby lkrpbk uo thouonm fiqqb kxe ydvr n uy e oa"))