#Extras: list of 100 words of different lengths, and the word is randomly picked every time. Option to play again. An option to give up.
import random 




words = ["apple", "happy", "train", "cloud", "quick", "yellow", "orange", "python", "cookie", "sunset",
              "garden", "jacket", "purple", "forest", "silver", "rocket", "puzzle", "flame", "wisdom", "planet",
              "ocean", "river", "guitar", "camera", "rocket", "coffee", "museum", "hiking", "cloudy", "singer",
              "butter", "summer", "travel", "breeze", "flower", "candle", "mirror", "keyboard", "diamond", "safari",
              "monkey", "lemon", "sunset", "forest", "basket", "cheese", "cactus", "writer", "office", "soccer",
              "blanket", "amazing", "journey", "whisper", "freedom", "captain", "mountain", "chocolate", "library",
              "zebra", "dolphin", "rocket", "helmet", "sweater", "penguin", "fantasy", "swimmer", "sprinter",
              "bicycle", "passion", "zodiac", "marble", "window", "silence", "moonlight", "alphabet", "shadow",
              "courage", "umbrella", "laughter", "diamond", "compass", "treasure", "whisper", "thunder", "sunset",
              "firefly", "journey", "harmony", "captain", "balance", "infinity", "whistle", "mystery", "heartbeat"]


word = random.choice(words).lower()
guess = " "
correct = False

tries = 0

number_of_letters = len(word)

for index_1 in range(number_of_letters):
    letter = word[index_1]
    #print(f"{letter}, {index_1}")
    

#giving the hint
print("Your hint is: ",)

for letter in word:
    print("_", end=" ")
print("\n")

#the puzzle
while correct is False:
    guess = input("What is your guess: ").lower()
    number_of_letters_guess = len(guess)
    tries += 1
    if guess == word:
        correct = True
        
    else:
        if guess == "i give up.":
            print(f"That's ok, let's try a different word! The word was {word}.")
            correct = True
        elif number_of_letters == number_of_letters_guess:
        
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
            #guess = input("Try again ").upper()
        elif number_of_letters_guess > number_of_letters:
            print("Too many letters, try a smaller word!")
           
           
            
            
        elif number_of_letters_guess < number_of_letters:
            print("Not enough letters, try a longer word!")
        
        
            


    
if guess == "i give up":
    print(f"You gave it {tries}. Better luck next time!")
else: 
    if tries == 1:
        print("Great job, you got it right on the first guess!")
    else:
        print(f"You got it! You found the word in {tries} tries.")








