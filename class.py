#WAP to find out a given number is odd or even. if odd print "given number is odd"
#num = int(input("Enter a number:"))

#if num % 2 == 0:
    print("Given number is even")
#else:
 #   print("given number is odd")

# WAP to check paliandrom or not
word = input("enter a word:")

reserved_word = word[::-1]

print("reserved word is:", reserved_word)

if word == reserved_word:
    print(f"{word}is palindrome")
else:
    print(f"{word}is not palindrome")