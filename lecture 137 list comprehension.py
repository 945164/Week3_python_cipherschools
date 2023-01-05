nums = [3,4,7,8,9,2,3,4,5,6,7,1]

new_list = []
for i in nums:
    if i%2 == 0:
        new_list.append(i*3)
    else:
        new_list.append(-i)
print(new_list) 

new_list2 = [i*3 if (i%2 == 0) else -i for i in nums]
print(new_list2)
