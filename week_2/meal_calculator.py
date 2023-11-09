import math
#Extras: I added an option for adding a tip, and some if elif else statements sprinkled in.
adult_meal_price=float(input("What is the price of an adult meal? "))
kids_meal_price=float(input("What is the price of a kid's meal? "))

adults=int(input("How many adults in your party?"))
children=int(input("How many children in your party?"))

adult_total=adult_meal_price * adults
kids_total=kids_meal_price * children
subtotal=adult_total + kids_total

#determining total
print(f"The price for the adult's meals is ${adult_total:.2f}. ")
print(f"The  price for the children's meals is ${kids_total:.2f}.")
print(f"The price for all meals is ${subtotal:.2f}.")

tip_decision = input("Would you like to add a tip? Y or N: ")
if tip_decision == "Y":
    tip_amount = float(input("That's very appreciated! What percentage? "))
elif tip_decision == "N":
    tip_amount = 0
    print("That's ok, it's not required. Just our livlihood, no big deal.")
else: print("I'm sorry, I didn't understand.")

tip_total= (tip_amount / 100) * subtotal
print(f"Thank you for your tip of ${tip_total:.2f}!")
print(f"Your new total comes to ${subtotal + tip_total:.2f}.")

#determining tax and total
tax=float(input("What is the sales tax in your state? (Enter as whole number, ie: enter 6 percent as 6) "))
tax_charged=tax / 100 * subtotal
total=tax_charged + subtotal + tip_amount
print(f"Total tax charged was ${tax_charged:.2f}.")
print(f"Final total is ${total:.2f}.")

#determining change
payment=float(input("What was the total payment amount? "))
change= payment - total

#thank you message for using exact change
if change == 0.00:
    print("Thank you for using exact change!") 
else:
    print(f"Your change comes out to ${change:.2f}.")  
