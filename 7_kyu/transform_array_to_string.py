def transform(s):
    return ''.join(list(map(lambda a: str(a),s)))

# Best Solution
# def transform(s):
#     return ''.join(map(str,s))

print(transform([5, 7, 8, 9, 0, 5]),"578905")
print(transform([False, True, " d g--"]),"FalseTrue d g--")
print(transform([78, 0, None, []]),"780None[]")
print(transform([(), (), ()]),"()()()")
print(transform([(1,2), (3,4), (5,6)]),"(1, 2)(3, 4)(5, 6)")
print(transform([(0.707), (3.1416), (2.718)]),"0.7073.14162.718")
print(transform(["abc", "xyz", "jmw"]),"abcxyzjmw")