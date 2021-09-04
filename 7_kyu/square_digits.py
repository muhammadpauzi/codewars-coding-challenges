def square_digits(num):
    result = ''
    # Looping array while convert to str
    for i in str(num):
        # Join and count
        result += str(pow(int(i), 2))
    return int(result)


print(square_digits(9119), 811181)
