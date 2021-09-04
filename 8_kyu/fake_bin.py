# Ubah nilai diatas lima menjadi "1" dan dibawah lima meenjadi "0"
def fake_bin(x):
    binary = ''
    for digit in x:
        if int(digit) >= 5:
            binary += '1'
        else:
            binary += '0'
    return binary

# Best Solution
# def fake_bin(x):
#     return ''.join('0' if c < '5' else '1' for c in x)

tests = [
    ["01011110001100111", "45385593107843568"],
    ["101000111101101", "509321967506747"],
    ["011011110000101010000011011", "366058562030849490134388085"],
    ["01111100", "15889923"],
    ["100111001111", "800857237867"],
]
        
for exp, inp in tests:
    print(fake_bin(inp), exp)