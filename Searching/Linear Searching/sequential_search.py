
"""Problem : You need a picture frame, so you walk down to the local photo store to examine their collection. They have all of their frames lined up against the wall. Apply the linear search algorithm to this problem, and describe how you would find the frame you wanted.

Starting at the first frame, examine each frame along the wall (without skipping any) until you find the frame you want."""

fav_frame = "Red Hearts Valentine Frame"

frames_in_store = ["New Born Baby Frame","Party Fram","Dark Frame","Quotes Frame","Color changing frame","Red Hearts Valentine Frame","Pink Teddy Frame"]

isExist = False
index = 0
total_frames = len(frames_in_store)-1
while index < total_frames:
    if frames_in_store[index] == fav_frame:
        isExist = True
        break
    index +=1

print(True) if isExist else print(False)

"""
Advanced method to save time complexity
"""
"""
Logic: If item is ordered and you reach greater point than current item so just break the loop
"""

first_ten_prime_nums = []
for i in range(1,1000):
    
    if len(first_ten_prime_nums) == 10:
        break
    total_factors = 0
    for j in range(1,i+1):
        if i%j == 0:
            total_factors +=1 
    if total_factors == 2:
        first_ten_prime_nums.append(i)

my_number = 10

isExist = False
index = 0
total_length = len(first_ten_prime_nums)-1
while index < total_length:
    if first_ten_prime_nums[index] == my_number:
        isExist = True
        break
    if first_ten_prime_nums[index] > my_number:
        break
    index +=1
    

print(True) if isExist else print(False)
print("I do not run whole loop, and I just run",index+1,"times!")