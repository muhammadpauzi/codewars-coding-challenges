# Membuat Table Perkalian
def multiplication_table(size):
    result = []
    for i in range(1,size + 1):
        # temp untuk memisahkan list didalam list
        temp = []

        for j in range(1,size + 1):
            temp.append(i * j)

        result.append(temp)
    return result

# Best Solution
# def multiplicationTable(size):
    # return [[j*i for j in range(1, size+1)] for i in range(1, size+1)]

print(multiplication_table(3), [[1,2,3],[2,4,6],[3,6,9]])