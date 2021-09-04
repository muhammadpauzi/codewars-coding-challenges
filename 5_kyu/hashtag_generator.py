def generate_hashtag(s):
    # jika kosong atau panjangnya melebihi 140 char kembalikan False
    if not s.replace(' ', '') or len(s) > 140: return False
    # Ubah huruf pertama besar lalu Ubah whitespace menjadi '' (kosong) dan tambahkan diaawal '#'
    return '#' + s.title().replace(' ', '')

# Best Sulution
# def generate_hashtag(s):
#     output = "#"  
#     for word in s.split():
#         output += word.capitalize()   
#     return False if (len(s) == 0 or len(output) > 140) else output


print(generate_hashtag(''), False)
print(generate_hashtag('Do We have A Hashtag')[0], '#')
print(generate_hashtag('Codewars      '), '#Codewars')
print(generate_hashtag('Codewars Is Nice'), '#CodewarsIsNice')
print(generate_hashtag('codewars is nice'), '#CodewarsIsNice')
print(generate_hashtag('CodeWars is nice'), '#CodewarsIsNice')
print(generate_hashtag('c i n'), '#CIN')
print(generate_hashtag('codewars  is  nice'), '#CodewarsIsNice')
print(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'), False)