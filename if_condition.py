age = 20
citizen = True

if age >= 18:
    if citizen:
        print("You can apply for a voter ID.")
    else:
        print("You must be a citizen to vote.")
else:
    print("You are too young to vote.")

