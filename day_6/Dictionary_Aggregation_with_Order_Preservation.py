'''
Docstring for day_6.Dictionary_Aggregation_with_Order_Preservation

Definition :

Given n input entries consisting of a string key and an integer value, where the key may contain multiple words, aggregate the values of identical keys while preserving the order of first appearance.
Finally, print each unique key along with the sum of its associated values, in the order they were first encountered.

Core Concepts Used :

Hash Map / Dictionary
Input Parsing with rsplit
Aggregation (Frequency / Sum Map)
Order Preservation (Python dictionaries)
'''

n = int(input())
ordinary_dictionary = {}

for _ in range(n):
    key, value = input().rsplit(" ", 1)
    value = int(value)

    if key in ordinary_dictionary:
        ordinary_dictionary[key] += value
    else:
        ordinary_dictionary[key] = value

for key, value in ordinary_dictionary.items():
    print(key, value)
