# def dont_give_me_five(start, end):
#     result = []
#     for n in range(start, end + 1):
#         # Jika ada lima di angka tersebut
#         if str(n).count("5") > 0:
#             continue
#         # Jika tidak ada
#         result.append(n)

#     return len(result)

# def dont_give_me_five(start, end):
#     return sum('5' not in str(i) for i in range(start, end + 1))


print(dont_give_me_five(1, 9), 8)
print(dont_give_me_five(4, 17), 12)
