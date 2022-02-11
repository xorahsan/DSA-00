normal_table = [55, 37, 83, 91, 48,63,1,47]

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
                print("Sucessfully cracked! ")
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
    c =1
    while True:
        next_id = (index + (c**2))%10
        if hash_table[next_id] == search_id:
            print(search_id, " found! (Plagirasim)")
            break
        else:
            print("Try no",c)
        c =c+1
        if c > 20:
            print("Not found!")
            break
    

print(hash_table)


"""
Cons:

Best Case O(1)
Worst and Average Case O(n)

Pros:

01) When the hash table is half full or more, the algorithm starts to take infinite time calculate index
Because at bigger number we only get 1,4,5,6,9 only so if there is 3 then it wont calculate

"""