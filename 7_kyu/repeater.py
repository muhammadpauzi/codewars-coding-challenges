def repeater(string, n):
    # str = ''
    # for i in range(n):
    #     str += string
    # return str
    
    return string * n
        


print(repeater('a', 5), 'aaaaa')
print(repeater('Na', 16), 'NaNaNaNaNaNaNaNaNaNaNaNaNaNaNaNa')
print(repeater('Wub ', 6), 'Wub Wub Wub Wub Wub Wub ')