print("My simple calculator ^_^")
while True:
   
   a = int(input("Enter the  first number:"))
   b = int(input("Enter the second number:"))
   print("enter the operation")
   op= input("Enter(+, -, *)")
   if op =="+":
      print("Result", a+b)
   elif op == "-":
        print("Result:",a-b)
   elif op == "*":
       print("Result:",a*b)
   elif op == "/":
       if b == 0:
           print("Cannot be divided by Zero")
       else:
           print("result:", a/b)
   count = input("\nDo you want to calculate again? (yes/no): ").lower()
   if count != "yes":
            print("Thanks for using my calculator ^_^")
            break