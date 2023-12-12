import math

#area of a rectangle
def area_rectangle(length,width):
    rectangle_area = length * width
    return rectangle_area

#area of square
def area_square(length):
    square_area = area_rectangle(length,length)
    return square_area

#area of a circle
def area_circle(length):
    circle_area = 2 * math.pi * length
    return circle_area

shape = input("What shape do you have: a Circle, a Square, or a Rectangle? If you're done, type 'Done'. ").capitalize()


while shape != "Done":
    if shape == "Rectangle":
        rec_length = float(input("What is the length of your rectangle? "))    
        rec_width = float(input("What is the width of your rectangle? "))
        print(f"the area of your rectangle is {area_rectangle(rec_width, rec_length)} units squared.")

    elif shape == "Circle":
        cir_radius = float(input("What is the radius of your circle? "))
        print(f"The area of your circle is {area_circle(cir_radius)} units squared.")

    elif shape == "Square":
        sq_length = float(input("What is the length of your square? "))
        print(f"The area of your square is {area_square(sq_length)} units squared")

    else:
        print("That isn't something I know how to do, please choose one of the stated options.")
    
    shape = input("What shape do you have: a Circle, a Square, or a Rectangle? If you're done, type 'Done'. ").capitalize()


print("Thanks and goodbye!")