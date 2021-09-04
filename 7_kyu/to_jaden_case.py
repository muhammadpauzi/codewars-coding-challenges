#  Soal ini sangat sederhana
# Hanya mengubah huruf awal dari setiap kata
def to_jaden_case(string):
    result = ''
    string = string.split(' ')

    for i, s in enumerate(string, 1):
        if i != 1:
            result += ' '
        result += s.capitalize()
    return result


quote = "How can mirrors be real if our eyes aren't real"
print(to_jaden_case(
    quote), "How Can Mirrors Be Real If Our Eyes Aren't Real")
