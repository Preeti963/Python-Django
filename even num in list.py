#find even number and store in new list using both 
# (without list comprehension and list comprehension)
#  of [2,4,5, 6, 7,8,912, 13, 14, 22, 27, 28]
numbers = [2, 4, 5, 6, 7, 8, 912, 13, 14, 22, 27, 28]
even_list = []   

for num in numbers:
    if num % 2 == 0:      
        even_list.append(num)   

print("Even numbers:", even_list)
