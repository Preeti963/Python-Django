#Assignment： 4212 4556 5456 2189 =**** ****
#**** 2189

numbers = [4212, 4556, 5456, 2189]

hiden_num =["****"] * (len(numbers)-1) + [str(numbers[-1])]
print("".join(hiden_num))

print("****",(numbers[-1]))