# 6 Kyu

def unique_in_order(iterable):
    if iterable == '':  # Jika Iterable string kosong
        return []

    is_int = False
    if isinstance(iterable[0], int):
        is_int = True

    # Inisialisasi
    result = []
    temp = ''

    for i in iterable:
        if temp != str(i):  # Jika i tidak sama dengan temp maka masukan nilai baru
            temp = str(i)
            result.append(int(temp) if is_int else temp)
            temp[1:len(temp)]
    return result


# Sulution Best Practice Another Users
# def unique_in_order(iterable):
#     result = []
#     prev = None
#     for char in iterable[0:]:
#         if char != prev:
#             result.append(char)
#             prev = char
#     return result


print(unique_in_order('AAAABBBCCDAABBB'), ['A', 'B', 'C', 'D', 'A', 'B'])
print(unique_in_order([1, 2, 2, 3, 4]), [1, 2, 3, 4])
