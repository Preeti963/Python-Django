#for minimum number
numbers = [5, 2, 3, 4, 2, 1, 6, 9, 3, 2]

count = 0
min_num = numbers[0]

while count < len(numbers):
    if numbers[count] < min_num:
        min_num = numbers[count]
    count += 1

print("Minimum number is:", min_num)
