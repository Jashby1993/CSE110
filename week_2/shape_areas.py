#So I can use the real pi
import math

#area of a square
square_side = float(input("What is the length of one side of the square in centimeters? "))
print(f"The area of the square is {square_side ** 2 :.1f} cm squared, or {square_side ** 2 / 10000:.1f} m squared. ")

#area of a rectangle
rec_side_1 = float(input("What is the width of the rectangle in centimeters? "))
rec_side_2 = float(input("What is the height of the rectangle in centimeters? "))
print(f"The area of the rectangle is {rec_side_1 * rec_side_2:.1f} cm squared, or {rec_side_1 * rec_side_2 / 10000} m squared.")

#area of a circle
radius = float(input("What is the length of the radius of the circle in cm? "))
print(f"The area of the circle is {radius ** 2 * math.pi:.1f} cm squared or {radius ** 2 * math.pi / 10000} m squared.")

#triple calculation
length = float(input("What is the lenth in centimeters? "))
length_m = length / 100

#First the square
print(f"The area of a square with a length that size is {length ** 2:.1f} cm squared, or {length_m ** 2 :.1f} m squared.")

#then the cube
print(f"The volume of a cube with a side of that length is {length ** 3:.1f} square cm, or {length_m **3:.1f} m squared. ")

#then the circle
print(f"The area of a circle with a radius of that length is {length ** 2 * 2 *math.pi:.3f} cm squared, or {length_m ** 2 * 2 * math.pi:.3f} m sqared.")

#then a SPHERE
print(f"The volume of a sphere with a radius of that length is {length ** 2 * 4 *math.pi:.3f} cm squared, or {length_m ** 2 * 4 * math.pi:.3f} m sqared.")

#then an equilateral triangle pyramid
print(f"The volume of an equilateral triangle pyramid with a length that size is {(length ** 3) / (6 * math.sqrt(2)):.3f} cm cubed.")