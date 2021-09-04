def count_positives_sum_negatives(arr):
    if arr == []: return arr
    leng = len(list(filter(lambda x: x > 0, arr)))
    total = sum(list(filter(lambda y: y < 0, arr)))
    return [leng,total]

# Best Solution
# def count_positives_sum_negatives(arr):
#     if not arr: return []
#     pos = 0
#     neg = 0
#     for x in arr:
#       if x > 0:
#           pos += 1
#       if x < 0:
#           neg += x
#     return [pos, neg]

print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]),[10,-65])
print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]),[8,-50])
print(count_positives_sum_negatives([1]),[1,0])
print(count_positives_sum_negatives([-1]),[0,-1])
print(count_positives_sum_negatives([0,0,0,0,0,0,0,0,0]),[0,0])
print(count_positives_sum_negatives([]),[])