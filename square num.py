#WAP to print Square of all number of list [21,54,76,2,1,34,56,67]
numbers = [21,54,76,2,1,34,56,67]
count = 0 
while count < len(numbers):
    square = numbers[count]* numbers[count]
    print(numbers[count],"square is", square)
    count +=1