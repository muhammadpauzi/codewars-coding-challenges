def points(games):
    points = 0
    for score in games:
        if int(score[0]) > int(score[-1]):
            points += 3
        elif int(score[0]) == int(score[-1]):
            points += 1
    return points

# Best Solution
# def points(games):
#     count = 0
#     for score in games:
#         res = score.split(':')
#         if res[0]>res[1]:
#             count += 3
#         elif res[0] == res[1]:
#             count += 1
#     return count

print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']), 30)
print(points(['1:1','2:2','3:3','4:4','2:2','3:3','4:4','3:3','4:4','4:4']), 10)
print(points(['0:1','0:2','0:3','0:4','1:2','1:3','1:4','2:3','2:4','3:4']), 0)
print(points(['1:0','2:0','3:0','4:0','2:1','1:3','1:4','2:3','2:4','3:4']), 15)
print(points(['1:0','2:0','3:0','4:4','2:2','3:3','1:4','2:3','2:4','3:4']), 12)