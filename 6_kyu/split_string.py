# def solution(s):
#     # Jika string kosong
#     if s == "":
#         return []
#     # Inisialisasi
#     result = []
#     it = 0
#     # Mengambil string dan dimasukan ke result
#     for i in range(2, len(s) + 2, 2):
#         result.append(s[it:i])
#         it += 2
#     # Jika elemen terkahir result panjangnya 1 maka tambahkan "_"
#     if len(result[len(result) - 1]) == 1:
#         result[len(result) - 1] += '_'

#     return result

# # # Top Sulution
# # def solution(s):
# #     result = []
# #     # Jika panjang string ganjil maka tambahkan "_" dibelakangnya
# #     if len(s) % 2:
# #         s += '_'

# #     # Mendapatkan string dan memasukannya kedalam result
# #     for i in range(0, len(s), 2):
# #         result.append(s[i:i+2])

# #     return result


import re


def solution(s):
    return re.findall(".{2}", s + "_")


# print(solution("asdfadsf"), ['as', 'df', 'ad', 'sf'])
# print(solution("asdfads"), ['as', 'df', 'ad', 's_'])
# print(solution(""), []),
# print(solution("x"), ["x_"])
