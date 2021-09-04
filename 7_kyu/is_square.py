def is_square(n):
    for i in range(0, 10):
        # Jika ada salah satu hasilnya akan mengembalikan true
        if i**2 == n:
            return True
    # JIka tidak ada maka kembalikan false
    return False


print(is_square(-1), False, "-1: Negative numbers cannot be square numbers")
print(is_square(0), True, "0 is a square number (0 * 0)")
print(is_square(3), False, "3 is not a square number")
print(is_square(4), True, "4 is a square number (4 * 4)")
print(is_square(25), True, "25 is a square number (5 * 5)")
print(is_square(26), False, "26 is not a square number")
