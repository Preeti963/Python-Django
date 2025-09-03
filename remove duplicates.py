#WAP  to remove duplicacy from list [5,6,3,4,5,6,4,3,5,6,7,3]
# numbers = [5,6,3,4,5,6,4,3,5,6,7,3]

# unique_num = list(set(numbers))

# print("list:",numbers)
# print("removing duplicstes",unique_num)

#without the  type conversion

# numbers = [5,6,3,4,5,6,4,3,5,6,7,3]
# unique_num =[]

# for num in numbers:
#     if num not in unique_num:
#         unique_num.append(num)
      
#     print(unique_num)

#sort the given list [5,6,3,4,5,6,4,3,5,6,7,3] without using sort predefined function
 
numbers = [5, 6, 3, 4, 5, 6, 4, 3, 5, 6, 7, 3]
sort = []

while numbers:                  
    minimum = numbers[0]        
    for num in numbers:         
        if num < minimum:       
            minimum = num
    sort.append(minimum) 
    numbers.remove(minimum)     
print(sort)
