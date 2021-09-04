def DNA_strand(dna):
    dna_dect = {"A": "T", "T": "A", "G": "C", "C": "G"}
    result = ''
    for s in dna:
        result += dna_dect[s]
    return result

    # 2.
    # result = ''
    # for s in dna:
    #     if s == "A":
    #         result += "T"
    #     if s == "T":
    #         result += "A"
    #     if s == "G":
    #         result += "C"
    #     if s == "C":
    #         result += "G"
    # return result


# Top Solution
# import string
# def DNA_strand(dna):
#     return dna.translate(string.maketrans("ATCG","TAGC"))
    # Python 3.4 solution || you don't need to import anything :)
    # return dna.translate(str.maketrans("ATCG","TAGC"))


print(DNA_strand("AAAA"), "TTTT", "String AAAA is")
print(DNA_strand("ATTGC"), "TAACG", "String ATTGC is")
print(DNA_strand("GTAT"), "CATA", "String GTAT is")

print('ab'.translate("cd"))
