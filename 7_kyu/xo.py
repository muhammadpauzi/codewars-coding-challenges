# Soal ini meminta jika x dan o jumlahnya sama maka return True jika tidak return False
# Jika distring tersbut tidak ada x dan o maka return True juga
def xo(s):
    s = s.lower()
    # if s.count('x') == s.count('o'):
    #     return True
    # return False
    # or
    return s.count('x') == s.count('o')


print(xo('xo'), 'True expected')
print(xo('xo0'), 'True expected')
print(xo('xxxoo'), 'False expected')
