"""
SIMPLE HASHED LIST
"""

"""
Please note the following:
0) Hashed list based on keys
1) For each Index on Array/Linked List, the index is calculated by value itself
2) When two value denote same index, it is called COLLISION!
3) It is limited to positive integers I GUESS
4) We should know the length of Array first
"""

# Here is a simple Hashed List that may have collision if we provide same index values

normal_table = [55, 37, 83, 91, 48]

n = 10
hash_table = []
for i in range(n):
    hash_table.append(None)

for i in normal_table:

    index = i % 10
    hash_table[index] = i

search_id = int(input("Enter an item: "))
index = search_id % 10

if hash_table[index] == search_id:
    print("Found at index",index)
else:
    print("Not Found")