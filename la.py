word = input("enter a word:")

reserved_word = word[::-1]

print("reserved word is:", reserved_word)

if word == reserved_word:
    print(f"{word }is palindrome")
else:
    print(f"{word} is not palindrome")