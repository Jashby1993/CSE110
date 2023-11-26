friends = []
friend=input("What is your friend's name? ").capitalize()

while friend  != "End":
    
    
    friends.append(friend)
    friend = input("What is your friend's name? ").capitalize()
    

print("Thank you.")

count = len(friends)

print(f"You have {count} friends. Their names are:")
for friend in friends:
    print(friend)