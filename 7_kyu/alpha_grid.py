# https://www.codewars.com/kata/60a94f1443f8730025d1744b/train/python

def grid(N):
    if N < 0:
        return None
    if N == 0:
        return ''

    chars = 'abcdefghijklmnopqrstuvwxyz' * 3
    start = 0
    result = []

    for i in range(N):
        temp = ''
        for j in range(N):
            temp += chars[j + start] + ' '
        else:
            result.append(temp.strip())
        start += 1

    return '\n'.join(result)

    # Best Practice
    if n >= 0: 
        return '\n'.join( ' '.join( chr(97+(i+j)%26) 
                                   for i in range(n) ) 
                         for j in range(n) )
    

# print(grid(0), '')
# print(grid(1), 'a')
# print(grid(2), '\na b\nb c')
# print(grid(4), '\na b c d\nb c d e\nc d e f\nd e f g')
# print(grid(6), '\na b c d e f\nb c d e f g\nc d e f g h\nd e f g h i\ne f g h i j\nf g h i j k')
print(grid(15))
# print(grid(-1), None)
# print(grid(-5), None)