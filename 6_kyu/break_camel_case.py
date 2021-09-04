def solution(s):
    result = []
    a = 0

    for i, char in enumerate(s):

        # Jika char huruf besar
        if char == char.upper():  # isUpper()
            result.append(s[a:i])
            a = i
    else:
        result.append(s[a:len(s)])
    # Join
    return " ".join(result)


# def solution(s):
#     return ''.join(' ' + c if c.isupper() else c for c in s)


print(solution("helloWorld"), "hello World")
# print(solution("camelCase"), "camel Case")
print(solution("breakCamelCase"), "break Camel Case")
