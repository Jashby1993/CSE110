
word = "SARCASM"

correct = False

tries = 0

number_of_letters = len(word)

for index_1 in range(number_of_letters):
    letter = word[index_1]
    print(f"{letter}, {index_1}")
    

#giving the hint
print("Your hint is: ",)

for letter in word:
    print("_", end=" ")
print("\n")
guess = input("What is your guess: ").upper()
number_of_letters_guess = len(guess)
tries += 1
if guess.upper() == word:
        
        correct = True
#the puzzle
while correct is False:
    
        #win or go again
    if guess != word:
        
        for i in range(len(word)):
            if i < len(guess):
                if guess[i] == word[i]:
                    # Same letter in the same position, print upper case
                    print(guess[i].upper(), end=" ")
                elif guess[i] in word:
                    # Letter in both words but not in the same position, print lower case
                    print(guess[i].lower(), end=" ")
                else:
                    # Letter not in the word, print underscore
                    print("_", end=" ")
        print("\n")
        guess = input("Not quite, try again ").upper()

        tries += 1

    elif guess.upper() == word:
        
        correct = True
if tries == 1:
    print("Great job, you got it right on the first guess!")
else:
    print(f"You got it! You found the word in {tries} tries.")
        




