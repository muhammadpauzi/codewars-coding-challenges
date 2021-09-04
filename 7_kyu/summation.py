def summation(num):
    n = 0
    for i in range(1, num + 1):
        n += i
    return n


# def summation(num):
    # func sum akan menghitung iterables dari index 0 sampai akhir [1,2,3,4] hasilnya = 10
    # Atau bisa juga di buat dengan function range
    # return sum(range(num + 1))

print(summation(1), 1)
print(summation(8), 36)
print(summation(22), 253)
print(summation(100), 5050)
print(summation(213), 22791)
