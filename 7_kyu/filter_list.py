# Di soal ini kita ditugas kan untuk membuat array baru yang isi nya hanya integer
def filter_list(l):
    result = list()
    for i in l:
        if isinstance(i, int):
            result.append(i)
    return result


print(filter_list([1, 2, 'a', 'b']), [1, 2])
# print(filter_list([1, 'a', 'b', 0, 15]), [1, 0, 15])
# print(filter_list([1, 2, 'aasf', '1', '123', 123]), [1, 2, 123])
