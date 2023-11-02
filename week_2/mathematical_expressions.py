#Asking what unit the user wants converted, and how many degrees
base_unit = (input("What temperature unit are we converting FROM? Type 'F' for farenheit or type 'C' for celsius. "))
degrees = float(input("What is the temperature? "))

#Both equations, to have the input ready either way
celsius = (degrees - 32) * (5 / 9)
farenheit = (degrees * 9 / 5) + 32

#Since both conversions are ready, this if/elif/else statement just determines what is displayed.
if base_unit == "F":
    print(f"That comes out to {celsius:.1f} degrees Celsius.")
elif base_unit == "C":
    print(f"That comes out to {farenheit:.1f} degrees Farenheit.")

#In case the user doesn't submit a vaild answer
else : print("I didn't understand what you want me to convert, please only type 'F' or 'C'.")
