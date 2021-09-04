def move_zeros(array):
    result = []
    zeros = array.count(0)
    for i in array:
        if i != 0:
            result.append(i)

    # Pakai for
    for i in range(zeros):
        result.append(0)

    # Atau pakai extend
    # result.extend([0 for i in range(zeros)])

    return result

# Best Solution
# def move_zeros(arr):
#     l = [i for i in arr if isinstance(i, bool) or i!=0]
#     return l+[0]*(len(arr)-len(l))

print(move_zeros(
        [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]),
        [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
print(move_zeros(
        [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
        [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
print(move_zeros([0, 0]), [0, 0])
print(move_zeros([0]), [0])
print(move_zeros([]), [])