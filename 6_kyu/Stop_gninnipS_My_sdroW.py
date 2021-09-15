def reverse(string):
    result = ""
    for i in string:
        result = i + result
    return result

def spin_words(sentence):
    result = []
    for s in sentence.split(' '):
        if len(s) >= 5:
            result.append(reverse(s))
            continue
        result.append(s)

    return " ".join(result)

    # BEST
    # Your code goes here
    # return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])

print(spin_words("Welcome"), "emocleW")
print(spin_words("This is a Welcome"), "emocleW")
