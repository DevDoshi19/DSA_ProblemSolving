from collections import OrderedDict

n = int(input())

ordered_dictionary = OrderedDict()
for _ in range(n):
    key,value= input().rsplit(" ",1)
    value = int(value)
    if key in ordered_dictionary :
        ordered_dictionary[key] += value
    else:
        ordered_dictionary[key] = value

for key, value in ordered_dictionary.items():
    print(key, value)

