normal_table = [55, 37, 83, 91, 51,67,97,47,17]

n = 10
hash_table = []
for i in range(n):
    hash_table.append(None)

for i in normal_table:

    index = i % 10
    if hash_table[index] != None:
        
        hash2 = 9-(i%9)

        def final_hash_id(times):
            return (index + (times*hash2)) % 10


        j = 1
        tries = 1
        while True:
            next_index = final_hash_id(j)
            
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

    hash2 = 9-(i%9)

    def final_hash_id(times):
        return (index + (times*hash2)) % 10


    while True:
        next_id = final_hash_id(c)
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
Pros:

Best Case O(1)
Worst and Average Case O(n)

Cons:

01) System memory/CPU usage
02) difficult to implement


"""