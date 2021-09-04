# Module regex
import re

# Soal untuk menghapus huruf vokal


def disemvowel(string):
# func sub adalah func untuk replace string
# "[]" kurung siku untuk menentukan huruf apa saja yang akan direplace
# Dalam kurung siku hanya akan dicocokan satu huruf saja
# contoh huruf o atau O
return re.sub("[oOeEiIaA]", "", string)

# Atau bisa mengunakan translate untuk mereplace
# string.translate(None,"auieoAUIEO")


print(disemvowel("This website is for losers LOL!"),
"Ths wbst s fr lsrs LL!")
