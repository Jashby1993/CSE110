
word = "SARCASM"

correct = False

tries = 0

#giving the hint
print("Your hint is: ",)

for letter in word:
    print("_", end=" ")
print("\n")
guess = input("What is your guess: ").upper()
tries += 1
#the puzzle
while correct is False:
    
        #win or go again
    if guess.upper() == word:
        correct = True

    else:
        guess = input("Not quite, try again: ")
        tries += 1

if tries == 1:
    print("Great job, you got it right on the first guess!")
else:
    print(f"You got it! You found the word in {tries} tries.")
        




