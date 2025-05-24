import cmath
import keyword
from statistics import variance
import matplotlib.pyplot as plt
import math
import time
# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(uno, dos):
    return uno + dos

print(add_two_numbers(2,2))

# Area of a circle is calculated as follows: area = π x r x r. 
# Write a function that calculates area_of_circle.
def calcular_area_circle(radio):
    area = math.pi * radio * radio
    return area
print(f"El radio de un circulo con un radio de 1.5 es: {round(calcular_area_circle(1.5))}") # 7

# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments.
# Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*args):
    suma = 0
    for nums in args:
        if not isinstance(nums, (int, float)):
            print("No han ingresados numeros validos")
            return None
        suma += nums
    return suma

print(add_all_nums(5,10)) #15

# Temperature in °C can be converted to °F using this formula:
# °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_to_farenheit(grades):
    farenheits = (grades * 9/5) + 32
    return farenheits
print(convert_to_farenheit(20)) # 68

# Write a function called check-season, 
# it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    if month == "Enero" or month == "Febrero" or month == "Marzo": 
        return "Verano" 
    if month == "Abril" or month == "Mayo" or month == "Junio": 
        return "Otoño" 
    if month == "Julio" or month == "Agosto" or month == "Setiembre": 
        return "Invierno" 
    if month == "Octubre" or month == "Noviembre" or month == "Diciembre": 
        return "Primavera" 
    else:
        return "No se que has ingresado..."
    
print(check_season("Abril"))

def check_in_season_2(month):
    
    month = month.capitalize()

    if month in ["Enero", "Febrero", "Marzo"]:
        print( "Verano")
    if month in ["Abril", "Mayo", "Junio"]:
        print("Otoño")
    if month in ["Julio", "Agosto", "Setiembre"]:
        print("Invierno")
    if month in ["Octubre", "Noviembre", "Diciembre"]:
        print("Primavera")
    else: 
        print("Mes no válido.")
        # Cuenta regresiva antes de salir
        for i in range(3, 0, -1):
            print(f"Saliendo en {i}...")
            time.sleep(1)
        return "Has ingresado algo mal, saliendo..."
        
        
check_in_season_2("enero")

# Write a function called calculate_slope which return the slope of a linear equation (y = mx + b)
def calculate_slopee(x1, y1,x2,y2):
    m = (y2 - y1) / (x2 - x1)
    return m

print(calculate_slopee(1,2,3,6))

""" def calculate_slope(x1, y1, x2, y2):
    m = (y2 - y1) / (x2 - x1)
    return m

# Puntos
x1, y1 = 1, 2
x2, y2 = 3, 6

# Cálculo de pendiente
m = calculate_slope(x1, y1, x2, y2)

# Ecuación de la recta: y = mx + b
b = y1 - m * x1

# Crear valores de x para la recta
x_vals = [0, 1, 2, 3, 4]
y_vals = [m * x + b for x in x_vals]

# Graficar
plt.plot(x_vals, y_vals, label=f"y = {m}x + {b}")
plt.scatter([x1, x2], [y1, y2], color='red', label='Puntos dados')
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.grid(True)
plt.title("Recta entre (1,2) y (3,6)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show() """

# Quadratic equation is calculated as follows: ax² + bx + c = 0.
# Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_qaudratic_eqn(a,b,c):
    discriminante = cmath.sqrt(b**2 - 4*a*c)
    x1 = (-b + discriminante) / (2 * a)
    x2 = (-b - discriminante) / (2 * a)
    
    return x1, x2
print(solve_qaudratic_eqn(1,-3,2))

# Declare a function named print_list. 
# It takes a list as a parameter and it prints out each element of the list.
def print_list(lista):
    for items in lista:
       print(items)
dias = ["Lunes", "Martes", "Miercoles", "Jueves"]
print_list(dias)

# Declare a function named reverse_list. 
# It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(array):
    reversed_list = []
    for items in range(len(array)-1, -1, -1):
        reversed_list.append((array[items]))
    return reversed_list

print(reverse_list([1, 2, 3, 4, 5])) # [5, 4, 3, 2, 1]

# Declare a function named capitalize_list_items. 
# It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list(lista):
    capitalized_list = []
    for i in range(len(lista)):
        capitalized_list.append(lista[i].capitalize())
    return capitalized_list
estaciones = ["enero", "febrero", "marzo"]
print(capitalize_list(estaciones))

#Declare a function named add_item. It takes a list and an item parameters.
#  It returns a list with the item added at the end
def add_item(lista, item):
    lista.append(item)
    return lista

print(add_item(estaciones, "Abril"))
print(add_item(dias, "Sabado"))

# Declare a function named remove_item. 
# It takes a list and an item parameters. 
# It returns a list with the item removed from it.
def removed_item(lista, item):
    lista.remove(item)
    return lista
print(f"Lista antes de ser borrada {estaciones}")
print(removed_item(estaciones, "enero"))

def remove_lista(lista, *items):
    return [elemento for elemento in lista if elemento is not items]

# Declare a function named sum_of_numbers. 
# It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(numero):
    numeros_sumados = 0
    for n in range(numero + 1):
        numeros_sumados += n 
    return numeros_sumados

print(sum_of_numbers(10))

# Declare a function named sum_of_odds.
# It takes a number parameter and it adds all the odd numbers in that range.
def summ_of_odd(numero):
    numeros_sumados = 0
    for n in range(numero + 1):
        if n % 2 != 0:
            numeros_sumados += n
    
    return numeros_sumados

print(summ_of_odd(10))

# Declare a function named sum_of_even. 
# It takes a number parameter and it adds all the even numbers in that - range
def summ_of_evens(numero):
    numeros_sumados = 0
    for n in range(numero + 1):
        if n % 2 == 0:
            numeros_sumados += n
    return numeros_sumados

print(summ_of_evens(10))

# Declare a function named evens_and_odds . 
# It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(numero):
    odds = 0
    evens = 0
    for n in range(numero + 1):
        if n % 2 == 0:
            evens += 1
        else: 
            odds += 1
    print(f"The number of odds are {odds}.")
    print(f"The number of even are {evens}.")

evens_and_odds(100)
# Call your function factorial, 
# it takes a whole number as a parameter and it return a factorial of the number
def factorial(numero):
    factorial = 1 # multiplicar por 1, porque un numero multiplicado por 0 siempre es cero
    for n in range(1, numero + 1):
        factorial *= n
    return factorial
print(factorial(5))

# Call your function is_empty,
# it takes a parameter and it checks if it is empty or not
def is_empty(p):
    if p:
        return False
    else: 
        return True
    
print(is_empty([1]))
# Write different functions which take lists. 
lista = [1,2,3,4,5,6,7,8,9]
lista_vacia = []
# They should 
# calculate_mean,
def calculate_mean(list): # promedio
    promedio = 0
    suma = 0
    if is_empty(list):
        print("Lista Vacia")
        return 0
    else:
        for i in range(len(list)):
            suma += list[i]
    promedio = suma / len(list)
    return promedio
# Mas Pythonica: 
def calcular_promedio(lista):
    if not lista: 
        print("Lista vacia")
        return 0
    else:
        return sum(lista) / len(lista)
    

print(calculate_mean(lista))
print(calcular_promedio(lista))
# calculate_median, 
def calculate_median(lista):
    if not lista:
        return "Lista vacia" 
    else:
        n = len(lista)
        mitad = n // 2 
        return lista[mitad]
    
print(calculate_median(lista))
# calculate_mode, 
def calculate_mode(lista):
    if not lista:
        return "Lista Vacia"

    frecuencia = {}
    for elemento in lista:
        if elemento in frecuencia:
            frecuencia[elemento] += 1
        else:
            frecuencia[elemento] = 1

    max_frecuencia = max(frecuencia.values())
    mode = [k for k, f in frecuencia.items() if f == max_frecuencia]
    if len(mode) == len(frecuencia):
        return "No hay Moda"
    elif len(mode) == 1:
        return mode[0]
    else:
        return mode
    
print(calculate_mode(lista))
# calculate_range, 
def calculate_range(lista):
    if not lista:
        return "No hay lista"
    return max(lista) - min(lista)

print(calculate_range(lista))
# calculate_variance, 
def calculate_variance(lista):
    print(variance(lista))

calculate_variance(lista)

def calculate_variance1(lista):
    if not lista:
        return "Lista vacía"
    
    n = len(lista)
    media = sum(lista) / n
    
    suma_diferencias_cuadrado = 0
    for x in lista:
        diferencia = x - media
        suma_diferencias_cuadrado += diferencia ** 2
    
    varianza = suma_diferencias_cuadrado / (n - 1)  # Muestral
    return varianza

print(calculate_variance1(lista))
# calculate_std (standard deviation).
def calculate_std(lista):
    if not lista:
        return "Lista vacia o inexistente"  

    variance = calculate_variance1(lista)
    if variance is None:
        return "No se pudo calcular la varianza"
    
    desviacion_estandard = math.sqrt(variance)
    return f"La desviacion estandar es {desviacion_estandard:.2f}"

print(calculate_std(lista))

# Write a function called is_prime, which checks if a number is prime.
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return f"{n} no es primo"
    else:
        return f"{n}  es primo"

print(is_prime(2))
print(is_prime(4))
print(is_prime(17))

# Write a functions which checks if all items are unique in the list.
def is_unique(lista):
    if len(lista) == len(set(lista)):
        print (f"La lista {lista} es unica")
    else: 
        print(f"La lista tiene no tiene valores unicos")
is_unique(lista)

# Write a function which checks if all the items of the list are of the same data type.
def same_type(lista):
    referencia = type(lista[0])
    for elemento in lista:
         if type(elemento) != referencia:
            return "Los elementos tienen tipos diferentes"
    
    return f"Todos los elementos son del tipo {referencia.__name__}"

print(same_type(lista))
lista_2 = [1, 2, 3, "staa"]
print(same_type(lista_2))
# Write a function which check if provided variable is a valid python variable
def is_valid_variable(nombre_variable):
    if not isinstance(nombre_variable, str):
        return "Debe ser una cadena de texto"

    if keyword.iskeyword(nombre_variable):
        return f"'{nombre_variable}' es una palabra reservada en Python y no puede usarse como variable."

    if nombre_variable.isidentifier():
        return f"'{nombre_variable}' es un nombre de variable válido."
    else:
        return f"'{nombre_variable}' NO es un nombre de variable válido."
