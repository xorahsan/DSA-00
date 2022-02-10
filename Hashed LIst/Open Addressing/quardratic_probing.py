normal_table = [55, 37, 83, 91, 48,63,1,3,33]

n = 10
hash_table = []
for i in range(n):
    hash_table.append(None)

for i in normal_table:

    index = i % 10
    if hash_table[index] != None:
        
        j = 1
        tries = 1
        while True:
            next_index = (index+(j**2))%10
            
            print("Cracking!")
            print("Try no: ",tries)
            if hash_table[next_index] == None:
                hash_table[next_index] = i
                
                break
            
            tries = tries +1
            j = j+1
            

    else:
        hash_table[index] = i

search_id = int(input("Enter an item: "))
index = search_id % 10



if hash_table[index] == search_id:
    print(search_id, " found!")
else:
    
    j = (search_id%10) +1
    new_c = 0
    check_found = False
    while new_c < len(hash_table)-1:
        if hash_table[j] == search_id:
            check_found = True
            print(search_id, " found! (Plagirasm)")
            break
        
        if j == len(hash_table)-1:
            j = 0
        else:
            j = j+1
        new_c = new_c +1

    if check_found == False:
        print(search_id, "does not found!")

print(hash_table)


"""
Cons:

Best Case O(1)
Worst and Average Case O(n)

Pros:

01) When the hash table is half full or more, the algorithm starts to take infinite time calculate index


"""