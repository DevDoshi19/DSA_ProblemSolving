'''
Docstring for HackerRank.collections_counter

problem link: https://www.hackerrank.com/challenges/collections-counter/problem

problem logic :
You are given the size of shoes and the list of shoe sizes available in the shop.
Your task is to compute how much money you earned by selling shoes to customers.

what i have done :
1. Used the Counter class from the collections module to count the occurrences of each shoe size.
2. Iterated through the customer requests, checking if the requested shoe size is available.
3. If available, added the price to the total amount and decremented the count of that shoe size.
4. Finally, printed the total amount earned.

'''


from collections import Counter

n = int(input())
my_list = list(map(int,input().split()))

size_counter = Counter(my_list)

x = int(input())
amount = 0
for i in range(x):
    size,price = map(int,input().split())
    if size_counter[size] > 0 :
        amount += price 
        size_counter[size] -= 1

print(amount)
   
