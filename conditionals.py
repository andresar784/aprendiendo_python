#import tkinter as tk
#from tkinter import messagebox
# Get user input using input(“Enter your age: ”). 
# If user is 18 or older, give feedback: 
# You are old enough to drive.
#  If below 18 give feedback to wait for the missing amount of years. Output:
age = int(input("Enter you age: "))
if age >= 18:
    print("You are old enough to drive.")
else:
    age_to_drive = 18 - age
    print(f"You need {age_to_drive} more years to learn to drive.")

# Compare the values of my_age and your_age using if … else. 
# Who is older (me or you)? Use input(“Enter your age: ”) 
# to get the age as input. 
# You can use a nested condition to print 'year' for 1 year 
# difference in age, 'years' for bigger differences, and a custom text if 
# my_age = your_age. utput:
my_age = 44
you_age = int(input("Enter you age: "))
diference = abs(my_age - you_age)
if my_age == you_age:
    print("We have the same age")
else:
    year_string = "year" if diference == 1 else "years"
    if my_age > you_age:
        print(f"I am older than you by {diference} {year_string}")
    else:
        print(f"You are older than my by {diference} {year_string}")
    
""" import tkinter as tk
from tkinter import messagebox

def comparar_edades():
    try:
        my_age = 44
        your_age = int(entry.get())
        difference = abs(my_age - your_age)

        if my_age == your_age:
            mensaje = "We have the same age."
        else:
            year_string = "year" if difference == 1 else "years"
            if my_age > your_age:
                mensaje = f"I am older than you by {difference} {year_string}."
            else:
                mensaje = f"You are older than me by {difference} {year_string}."

        messagebox.showinfo("Resultado", mensaje)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Comparar Edades")
ventana.geometry("300x150")

# Etiqueta y campo de entrada
label = tk.Label(ventana, text="Enter your age:")
label.pack(pady=10)

entry = tk.Entry(ventana)
entry.pack()

# Botón para comparar edades
boton = tk.Button(ventana, text="Compare", command=comparar_edades)
boton.pack(pady=10)

# Ejecutar la interfaz
ventana.mainloop() """

# Get two numbers from the user using input prompt. If a is greater than b 
# return a is greater than b, if a is less b return a is smaller than b, 
# else a is equal to b. Output:
a = int(input("Ingresa numero a: "))
b = int(input("Ingresa numero b: "))
if a > b:
    print("a es mayor que b")
elif b > a:
    print("b es mayor que a")
else: 
    print("Son iguales")


# Write a code which gives grade to students according to theirs scores:
score = int(input("Enter your score: "))

if 90 <= score <= 100:
    letter = "A"
elif 70 <= score < 90:
    letter = "B"
elif 60 <= score < 70:
    letter = "C"
elif 50 <= score < 60:
    letter = "D"
elif 0 <= score < 50:
    letter = "F"
else:
    letter = None  # Para controlar error

if letter:
    print(f"Your grade is {letter}")
else:
     print("Has ingresado un número incorrecto.")

# Check if the season is Autumn, Winter, Spring or Summer.
#  If the user input is: September, October or November, the season is Autumn. 
# December, January or February, the season is Winter.
#  March, April or May, the season is Spring 
# June, July or August, the season is Summer
month = input("Enter the month: ")
if  month == "September" or month == "October" or month == "November":
    season = "Autumn"
elif month == "December" or month == "January" or month == "February":
    season = "Winter"
elif month == "March" or month == "April" or month == "May":
    season = "Winter"
elif month == "June" or month == "July" or month == "August":
    season = "Summer"
else:
    month = None

if month:
    print(f"The season is {season}")
else:
    print("Has ingresado cualquier cosa")


# fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list.
# If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input("Enter a fruit: ").strip().lower() # entered pear
if new_fruit in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(new_fruit)
    print(fruits) # ['banana', 'orange', 'mango', 'lemon', 'pear']

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
 #* Check if the person dictionary has skills key, 
 # if so print out the middle skill in the skills list.
def buscar_medio(diccionario):
    habilidades = diccionario.get("skills", [])
    if habilidades:
        medio = len(habilidades) // 2
        return habilidades[medio]
    return None

if "skills" in person:
    elemento_del_medio = buscar_medio(person)
    print(f"Elemento del medio {elemento_del_medio}")
else: 
    print("No existe habilidades en persona")
 #* Check if the person dictionary has skills key, if so check if the person has 'Python' 
 # skill and print out the result.
if "skills" in person:
    if "Python" in person["skills"]:
        print(f"La habilidad Python existe en la persona")
    else:
        print("La habilidad no exsite en la persona")
else:
    print("No se encuentra skills en la persona")
 #* If a person skills has only JavaScript and React,
 #  print('He is a front end developer'),
 #  if the person skills has Node, Python, MongoDB, print('He is a backend developer'),
 #  if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
 # else print('unknown title') - for more accurate results more conditions can be nested!
if "React" in person["skills"] and "Node" in person["skills"] and "MongoDB" in person["skills"]:
    print("Fullstack developer")
elif "Node" in person["skills"] and "Python" in person["skills"] and "MongoDB" in person["skills"]:
    print("Backend developer")
elif "JavaScript" in person["skills"] and "React" in person["skills"]:
    print("Frontend developer")
else:
    print("Unknown title")
 #* If the person is married and if he lives in Finland, 
 # print the information in the following format:
 # Asabeneh Yetayeh lives in Finland. He is married.
is_married = person["is_married"]
if is_married and "Finland" in person["country"]:
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
else:
    print("Esta persona no vive en Finlandia")