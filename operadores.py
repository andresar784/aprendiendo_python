
import math
# Declare your age as integer variable
age = 45
#Declare your height as a float variable
height = 83.5
#Declare a variable that store a complex number
complex_number = 3j
# Write a script that prompts the user to enter base and height of the triangle and calculate an 
# area of this triangle (area = 0.5 x b x h).
# Hay que convertir a float porque con input se ingresa como str o string
height_2 = float(input("Enter the height: ").strip())
base = float(input("Enter the base: ").strip())
area = 0.5 * height_2 * base
print("Area es ", area)

# Write a script that prompts the user to enter side a, side b, 
# and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
a = int(input("Enter the lado a: "))
b = int(input("Enter the lado b: "))
c = int(input("Enter the lado c: "))
print("Perimetro: ", a + b + c)

# Get length and width of a rectangle using prompt. 
# Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
height_rectangle = int(input("Enter the height: "))
lenght = int(input("Enter the length: "))
print("Area: ", height_rectangle * lenght)
print("Perimeter", 2 * (lenght * height_rectangle))

#Get radius of a circle using prompt. 
#Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radio = float(input("Radius: "))
print(f"Area, {math.pi * radio * radio:.3f}") #f-strings Los f-strings (formatted strings) son una forma rápida y eficiente de formatear cadenas en Python. 
# Se introdujeron en Python 3.6 y permiten incrustar expresiones dentro de una cadena, usando {}.
print(f"Circunference: {2 * math.pi * radio:.2f}")

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
# Definir los coeficientes de la ecuación y = mx + b
m = 2  # Pendiente
b = -2  # Intersección con el eje Y

# Intersección con el eje X (cuando y = 0)
x_intercept = -b / m  # Resolver 0 = 2x - 2

# Imprimir resultados
print(f"Pendiente (m): {m}")
print(f"Intersección con el eje Y: (0, {b})")
print(f"Intersección con el eje X: ({x_intercept}, 0)")

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1,y1 = 2, 2
x2, y2 = 6, 10
slope = (y2 - y1) / (x2 - x1) 
print(f"Distance " , math.sqrt((x2 - x1)**2+(y2 - y1)**2))
print(f"Pendiente 2: {slope}")

# Compare the slopes in tasks 8 and 9.
if m > slope:
    print("La pendiente de la ecuación y=2x-2 es mayor que la pendiente calculada entre los puntos.")
elif m < slope:
    print("La pendiente calculada entre los puntos es mayor que la pendiente de la ecuación y=2x-2.")
else:
    print("Ambas pendientes son iguales.")

#Calculate the value of y (y = x^2 + 6x + 9). 
#Try to use different x values and figure out at what x value y is going to be 0.
x = -3
y = x**2 + (6*x) + 9
print(f"Value of y: {y}")

#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len("dragon")!= len("python"))

#Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')

#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('jargon' in 'I hope this course is not full of jargon')

#There is no 'on' in both dragon and python
print('on' not in 'dragon' and 'on' not in 'python')

#Find the length of the text python and convert the value to float and convert it to string
length = float(len('python'))
str_length = str(length)
print(f"The length of python is {length} letters and converted in string is {str_length}")

# Even numbers are divisible by 2 and the remainder is zero. 
# How do you check if a number is even or not using python?
# Solicitar un número al usuario
num = int(input("Enter a number: "))

# Comprobar si es par
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
if 7 // 3 == int(2.7):
    print("True")

# Check if type of '10' is equal to 10
if type('10') ==  10:
    print("True")
else:
    print("False")  

# Check if int('9.8') is equal to 10
if int(9.8) == 10:
    print("True") 
else:
    print("False") 

    # Writ a script that prompt the user to enter hours and rate per hour.
# Calculate pay of the person?  
# Enter Hours: 40
# Enter Rate: 28        
# Pay: 1120.0

hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
pay = hours * rate  
print(f"Pay: {pay}")

# Write a script that prompts the user to enter number of years.
# Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input("Enter number of years: "))
seconds = years * 365 * 24 * 60 * 60    
print(f"Seconds: {seconds}")

# Write a Python code that displays the following table
# 1 1 1 1 1         
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64   
# 5 1 5 25 125

for i in range(1, 6):
    print(i, 1, i, i**2, i**3)
