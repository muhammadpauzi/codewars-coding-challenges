def to_underscore(string):
    # if str(string).isnumeric():
    #     return str(string)
    # temp = ''
    # # looping each chars
    # for i, char in enumerate(string):
    #     if i != 0:
    #         # if char is uppercase
    #         if char.isupper():
    #             temp += '_'
    #     temp += char
    # return temp.lower()

    # REFACTOR
    string = str(string)
    temp = string[0]
    # looping each chars
    for char in string[1:]:
        # if char is uppercase
        temp += ('_' + char) if char.isupper() else char
    return temp.lower()

    # BEST PRACTICE
    # import re
    # return re.sub(r'(.)([A-Z])', r'\1_\2', str(string)).lower()    


print(to_underscore('TestController'), 'test_controller')
print(to_underscore('1'), '1')
print(to_underscore(5), '5')
