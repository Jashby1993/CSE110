#setting the word
word = input("Pick a word: ")
#setting the letter:
choice = input("pick a letter in the word: ")



for letter in word:
    if letter == choice:
        print("_",end=" ")
    else:
        print(letter.lower(),end=" ")