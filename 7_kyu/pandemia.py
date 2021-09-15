from math import floor

def infected(s):
    arrays = s.split('X')
    arrays = list(filter(lambda x: x != "", arrays))
    result = ""
    for i, array in enumerate(arrays):
        if array.count('1') > 0:
            arrays[i] = '1' * len(array)
            result += arrays[i]
            continue
        else:
            result += arrays[i]
    

    if not result:
        return 0
        
    percentage = 100 * result.count('1') / len(result)

    if percentage in [100.0, 0.0]:
        return floor(percentage)

    return percentage

    # BEST
    # lands = s.split('X')
    # total = sum(map(len, lands))
    # infected = sum(len(x) for x in lands if '1' in x)
    # return infected * 100 / (total or 1)


fixeds = [
    ("01000000X000X011X0X",73.33333333333333),
    ("01X000X010X011XX", 72.72727272727273),
    ("XXXXX", 0),
    ("00000000X00X0000", 0),
    ("0000000010", 100),
    ("000001XXXX0010X1X00010", 100),
    ("X00X000000X10X0100",42.857142857142854)
]

for inp,exp in fixeds:
    print(infected(inp),exp)