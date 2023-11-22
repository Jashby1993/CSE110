import random

play_again = True

while play_again == True:
    magic_number = random.randint(1,100)
    tries = 0
    guess = int( input("What is the magic number? "))
    tries += 1


    if guess != magic_number:
        correct = False

    tries = 0

    while correct == False:
        if guess > magic_number:
            print("Lower,", end=" ")
            guess = int( input("Guess again! "))
            tries += 1
            if guess == magic_number:
                correct = True
        elif guess < magic_number:
            print("Higher,", end=" ")
            tries += 1
            guess = int( input("Guess again! "))
            if guess == magic_number:
                correct = True

    if correct == True:

        print("Nailed it!!", end=" ")
        if tries == 1:
            print("You got it on the first try!")
        else:
            print(f"It took you {tries} to find the magic number!")
        
     
    start_over_answers = ["YES","NO"]
    acceptable_answer = False
    while acceptable_answer == False:
        start_over = input("Would you like to play again? YES or NO: ").upper()  
        if start_over in start_over_answers:
            acceptable_answer = True
        else:
            print("I didn't understand your answer.",end=" ")
    
    if start_over == "NO":
        play_again = False

    elif start_over == "YES":
        print("Great, let's play again!")

print("Thank you for playing!")


      
























