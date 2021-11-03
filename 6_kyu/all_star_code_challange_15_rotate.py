def rotate(str_):
    # if str_.strip() == '' and len(str_) > 0:
    #     return [str_]
    # elif str_.strip() == '':
    #     return []
    # elif len(str_.strip()) <= 1:
    #     return [str_]


    # reduced = 1
    # result = []
    # while True:
    #     temp = ''
    #     for i, s in enumerate(str_):
    #         temp += str_[i - (len(str_) - reduced)]
    #     else:
    #         result.append(temp)
    #         reduced += 1

    #     if reduced == len(str_):
    #         result.append(str_)
    #         break
    # return result

    # refactor
    # validate
    if str_ == '':
        return []

    if len(str_) <= 1:
        return [str_]

    reduced = 1
    result = []
    while True:
        temp = ''
        for i in range(len(str_)):
            temp += str_[i - (len(str_) - reduced)]
            
        result.append(temp)
        reduced += 1

        if reduced == len(str_):
            result.append(str_)
            break

    return result

    # Best Practice
    # return [str_[i + 1:] + str_[:i + 1] for i in range(len(str_))]

print(rotate("Hello"), ["elloH", "lloHe", "loHel", "oHell", "Hello"])
print(rotate("y"), ["y"])
print(rotate(" "), [" "])
print(rotate(""),[])
print(rotate("123"), ["231", "312", "123"])
