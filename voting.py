#VOting programming
votes = {"A": 0, "B": 0, "C": 0}

def vote(candidate):
    if candidate in votes:
        votes[candidate] += 1
        print(f"Vote counted for {candidate}!")
    else:
        print("Invalid option!")

while True:
    choice = input("Enter your vote (or type 'exit'): ").upper()
    if choice == "EXIT":
        break
    vote(choice) 