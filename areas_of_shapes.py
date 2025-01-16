#This program accepts and compute the areas of three different shapes (Square,Rectangle and Circle).

square_length= float(input('\nEnter the length of the side of the square : '))
print(f'The area of the square is : {square_length**2}')

length_of_rectangle=float(input('\nEnter the length of the rectangle : '))
width_of_rectangle=float(input('Enter the width of the rectangle : '))
print(f'The area of the rectangle is : {length_of_rectangle * width_of_rectangle}')

radius_of_circle=float(input('\nEnter radius of the circle : '))

print(f'\nThe area of the circle is {3.14 * radius_of_circle**2}')


#Stretch Challenge

# Stretch 1: Using the math library
from math import pi
print("\n\n*****************************************")
radius=float(input('\nEnter radius of the circle : '))
print(f'\nThe area of the circle is {pi* radius**2}\n')

# Stretch 2: Many areas from one value
length=float(input('Enter the value for the length : '))
print(f'\nThe area of the square is : {length**2}')
print(f'The area of the circle is {pi * length**2}\n')
print(f'The volume of the cube is : {length**3}')
print(f"Volume of a sphere: {(4/3)*pi*(length**3)}n")


# Stretch 3: cm to m conversion

# Area of a square
side = float(input("\nWhat is the length of a side of the square (in cm)? "))
area = side ** 2

print(f"The area of the square is: {area} cm^2")
print(f"The area of the square is: {area / 10000} m^2")

# Area of a rectangle
length = float(input("\nWhat is the length of rectangle (in cm)? "))
width = float(input("What is the width of the rectangle (in cm)? "))
area = length * width
print(f"The area of the rectangle is: {area} cm^2")
print(f"The area of the rectangle is: {area / 10000} m^2")

# Area of a circle
radius = float(input("\nWhat is the radius of the circle (in cm)? "))
area = 3.14 * (radius ** 2)
print(f"The area of the circle is: {area} cm^2")
print(f"The area of the circle is: {area / 10000} m^2")