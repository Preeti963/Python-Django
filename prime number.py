
#WAP to print square of prime number upto 200, if prime number is 13 then skip , if prime number 59 then exit the program

for num in range(2,200):
      for i in range(2, int(num**0.5) + 1):
         if num % i == 0:
            break
      if num == 13:
         continue
      if num == 59:
          print("prime number 59 reached,exiting program.")
          break 
      print(f"prime is {num} ")
