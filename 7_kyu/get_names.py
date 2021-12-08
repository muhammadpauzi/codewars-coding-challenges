# https://www.codewars.com/kata/514a677421607afc99000002/train/python

# Best Sulution
def itemgetter(item):
    return item['name']
    
def get_names(data):
    return list(map(itemgetter, data))

    
data = [
    {'name': 'Joe', 'age': 20},
    {'name': 'Bill', 'age': 30},
    {'name': 'Kate', 'age': 23}
]

print(get_names(data), ['Joe', 'Bill', 'Kate'])
