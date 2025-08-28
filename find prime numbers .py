# Program to find prime numbers from 5 to 20

for num in range(5, 21):
   
    is_prime = True
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
