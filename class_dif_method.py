#make a math class where different method like is_prime,is_odd,is_even,get_square_root,get_cube_root,is_num,calculate_simple_intrest

import math

class Math:
    def is_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def is_odd(self, n):
        return n % 2 != 0
    
    def is_even(self, n):
        return n % 2 == 0
    
    def get_square_root(self, n):
        return math.sqrt(n)
    
    def get_cube_root(self, n):
        return round(n ** (1/3), 3)
    
    def is_num(self, value):
        return isinstance(value, (int, float))
    
    def calculate_simple_interest(self, p, r, t):
        return (p * r * t) / 100



m = Math()

while True:
    print("\n---- Math Operations list ----")
    print("1. Check Prime")
    print("2. Check Odd")
    print("3. Check Even")
    print("4. Get Square Root")
    print("5. Get Cube Root")
    print("6. Check if Number")
    print("7. Calculate Simple Interest")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == "1":
        n = int(input("Enter number: "))
        print("Prime?", m.is_prime(n))

    elif choice == "2":
        n = int(input("Enter number: "))
        print("Odd?", m.is_odd(n))

    elif choice == "3":
        n = int(input("Enter number: "))
        print("Even?", m.is_even(n))

    elif choice == "4":
        n = int(input("Enter number: "))
        print("Square Root:", m.get_square_root(n))

    elif choice == "5":
        n = int(input("Enter number: "))
        print("Cube Root:", m.get_cube_root(n))

    elif choice == "6":
        val = input("Enter value: ")
        # check if it's number or not
        try:
            num = float(val)
            print("Yes, it is a number:", m.is_num(num))
        except:
            print("No, it's not a number:", m.is_num(val))

    elif choice == "7":
        p = float(input("Enter Principal: "))
        r = float(input("Enter Rate: "))
        t = float(input("Enter Time (years): "))
        print("Simple Interest:", m.calculate_simple_interest(p, r, t))

    elif choice == "8":
        print("Exiting...!")
        break
    
    else:
        print("Invalid choice! Try again.")
