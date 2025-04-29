import math

#Write a python comment saying 'Day 2: 30 Days of python programming'
# Day 2: 30 days of Python
#Declare a first name variable and assign a value to it
first_name = "Andres"
#Declare a last name variable and assign a value to it
last_name = "Rodriguez"
#Declare a full name variable and assign a value to it\
full_name = "Andres Rodriguez"
#Declare a country variable and assign a value to it
country = "Uruguay"
#Declare a city variable and assign a value to it
city = "Rivera"
#Declare an age variable and assign a value to it
age = 40
#Declare a year variable and assign a value to it
year = 2024
#Declare a variable is_married and assign a value to it
is_married = True
#Declare a variable is_true and assign a value to it
is_true = True
#Declare a variable is_light_on and assign a value to it
is_light = False
#Declare multiple variable on one line
is_false, nombre, hijos = False, "Andres", 4

#Exercises: Level 2

#Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(is_false))
print(type(hijos))
print(type(age))
print(type(country))
print(type(nombre))
print(type(city))
#Using the len() built-in function, find the length of your first name
print(len(first_name))
#Compare the length of your first name and your last name
print(first_name >= last_name)
#Declare 5 as num_one and 4 as num_two
num_one, num_two = 5, 4
#Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
print(total)
#Subtract num_two from num_one and assign the value to a variable diff
dif = num_two - num_one
print(dif)
#Multiply num_two and num_one and assign the value to a variable product
product = num_two * num_one
print(product)
#Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
print(division)
#Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
print("Remainder", remainder)
#Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
print("Exp", exp)
#Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
print("Floor", floor_division)
"""
The radius of a circle is 30 meters.
        Calculate the area of a circle and assign the value to a variable name of area_of_circle
        Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
        Take radius as user input and calculate the area.
"""
# A = π * r²
radius = 30
area_of_circle = math.pi * (radius ** 2)
print("Area del circulo", area_of_circle)
circum_of_circle = (math.pi * 2) * radius
print("Circunferencia", circum_of_circle)
radio = input("Ingrese un radio para calcular: ").strip()
radio = int(radio)
area = math.pi * (radio ** 2)
print("Area del circulo con area por input ", area)

# Use the built-in input function to get first name, last name, country and age 
# from a user and store the value to their corresponding variable names
nombre = input("Nombre: ").strip()
apellido = input("Apellido: ").strip()
pais = input("Pais: ").strip()
edad = input("Edad: ").strip()
print(nombre, apellido, pais, edad)


#Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
