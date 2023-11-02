#So I can use the real pi
import math

#area of a square
square_side = float(input("What is the length of one side of the square? "))
print(f"The area of the square is {square_side ** 2 :.1f} units squared. ")

#area of a rectangle
rec_side_1 = float(input("What is the width of the rectangle? "))
rec_side_2 = float(input("What is the height of the rectangle? "))
print(f"The area of the rectangle is {rec_side_1 * rec_side_2:.1f} units squared.")

#area of a circle
radius = float(input("What is the length of the radius of the circle? "))
print(f"The area of the circle is {radius * math.pi:.1f} square units.")