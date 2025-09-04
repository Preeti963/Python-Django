#WAP to make a function called isPrime which check the given input number is prime or not.
#isPrime function return in boolean(True,False).
def prime_num(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True   


numbers = int(input("Enter a number: "))

print("return value", prime_num(numbers))

if prime_num(numbers):
    print(f"{numbers} is prime")
else:
    print(f"{numbers} is not prime")