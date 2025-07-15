from collections import Counter
from functools import reduce
from countries_list import countries2
from countries_info import countries_data

# Explain the difference between map, filter, and reduce
"""
    Map: Take a function and iterable as a parameter. It execute a specified function
    for each item in a iterable, the item is sent to the function as a parameter. 
    Using map() you can avoid traditional for loops, and returns a map object (which is an iterator).
    Filter: Returns an iterator are filtered trought a function to test if the item is accepted or not
    The filter() method filters a gvien sequence with the help of a function that tests each element
    to be true or not, the function need to filter true or false for each element. 
    Returns a new iterable
    Reduce: The reduce(fun,seq) function is used to apply a particular function passed in 
    its argument to all of the list elements mentioned in the sequence passed along.
    The function accumulates results for each number in a iterable, Return a single result, instead of a iterble
 """
# Explain the difference between higher order function, closure and decorator
"""
    Higher Order functions:
    A Higher-Order Function is a function that either:
    Takes another function as an argument
    Returns a function as a result
    Closure: Closures allow functions to remember and use variables from their parent scope 
    even after the parent function has finished running. This makes them essential for higher-order 
    functions, enabling tasks like combining multiple functions , storing previous results for 
    faster performance, breaking functions into smaller and efficiently handling arrays
    Decorator: Decorators extend or modify functions without changing their original code 
    by wrapping them inside another function. They enhance higher-order functions by 
    enabling tasks like caching results, controlling access (authentication), 
    transforming inputs/outputs and tracking function calls.

"""
""" def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {} . I love to teach.".format(
        first_name, last_name, country))

print_full_name("Asabeneh", "Yetayeh",'Finland') """

# Define a call function before map, filter or reduce, see examples.
# Definir fucniones auxiliares. 
# Significa que antes de usar map, filter o reduce,
#  definís una función que será llamada por estas 
# funciones para operar sobre los datos.
def cuadrado(x):
    return x ** 2

numeros = [1,2,3,4]
resultado = list(map(cuadrado, numeros))
print(resultado)

def restar(x):
    return x - 1

resultado2 = list(map(restar, numeros))
print(resultado2)

def espar(x):
    return x % 2 == 0

resultado3 = list(filter(espar, numeros))
print(resultado3)

def suma(a,b):
    return a + b

resultado4 = reduce(suma, numeros)
print(resultado4)

# Use for loop to print each country in the countries list.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland', "Italia"]
for i in countries:
    print(i)
# Use for to print each name in the names list.
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
for name in names:
    print(name)

# Use for to print each number in the numbers list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print(number)
# Use map to create a new list by changing each country to uppercase in the countries list
new_countrie_list = list(map(str.upper, countries))
print(new_countrie_list)
# Use map to create a new list by changing each number to its square in the numbers 
new_number_list = list(map(cuadrado, numbers))
print(new_number_list)
# Use map to change each name to uppercase in the names list
new_names_list = list(map(str.upper, names))
print(new_names_list)
# Use filter to filter out countries containing 'land'.
land_list = list(filter(lambda country: "land" in country , countries))
print(land_list)
# Use filter to filter out countries having exactly six characters.
six_characters = list(filter(lambda countrie : len(countrie) == 6     ,  countries))
print(six_characters)
# Use filter to filter out countries containing six letters and more in the country list.
six_characters = list(filter(lambda country : len(country) >= 6, countries ))
print(six_characters)
# Use filter to filter out countries starting with an 'E'
resultado = list(filter(lambda country: "E" in country[:1] , countries))
print(resultado)
resultado = list(filter(lambda country: country.startswith("E"), countries))
print(resultado)
# Chain two or more list iterators 
# (eg. arr.map(callback).filter(callback).reduce(callback))
resultado = reduce(
    lambda acc, x: acc + ", " + x, 
    filter(
        lambda country: country.endswith("land"), 
        map(lambda c : c.capitalize(), countries)
    )
)
print(resultado)
# Dado un conjunto de números:
# Multiplicá cada número por 3 → map()
# Sumá todos los valores y repetí esa suma en una lista 3 veces → reduce()
#Filtrá los valores que son mayores que un umbral (por ejemplo, 50) → filter()
print(list(
    map(
        lambda x: x * 3,
        [reduce(
            lambda x, y: x + y,
            filter(lambda x: x < 10, numeros),
            0
        )]
    )
))
# Declare a function called get_string_lists which takes a list as a parameter 
# and then returns a list containing only string items.
datos = [1, 'Hola', 3.14, True, 'Python', [1, 2], {'a': 1}]
def get_string_list(lista):
    return list(filter(lambda x: isinstance(x, str), lista))
print(get_string_list(datos))
# Use reduce to sum all the numbers in the numbers list.
print(reduce(lambda x, y: x + y, numbers))
# Use reduce to concatenate all the countries and to produce this sentence: 
# Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
resultado = reduce(lambda x, val: x + ", " + val, countries[:-1])
print(f"{resultado} and {countries[-1]} are North European countries")
# Declare a function called categorize_countries that returns a list of countries 
# with some common pattern (you can find the countries list in this repository as 
# countries.js(eg 'land', 'ia', 'island', 'stan')).
def categorize_countries(lista, pattern):
    return list(filter(lambda pais: pattern.lower() in pais.lower(), lista))
print(categorize_countries(countries, "de"))
# Create a function returning a dictionary, where keys stand for starting letters of countries
# and values are the number of country names starting with that letter
def funcion_returning_string(lista):
    return dict(Counter(map(lambda c: c[0], lista )))

print(funcion_returning_string(countries2))

def count_countries_by_first_letter(lista):
    return reduce(
        lambda acc, country: {
            **acc,
            country[0].upper(): acc.get(country[0].upper(), 0) + 1
        },
        lista,
        {}
    )
print(count_countries_by_first_letter(countries2))

# Declare a get_first_ten_countries function - it returns a 
# list of first ten countries from the countries.js list in the data folder.
def get_first_ten_countries(lista):
    return list(map(lambda x: x[1], filter(lambda x: x[0] < 10, enumerate(lista))))
print(get_first_ten_countries(countries2))

# Declare a get_last_ten_countries function that returns the 
# last ten countries in the countries list.
def getLast_ten_countries(lista):
    total = len(lista)
    start = total - 10
    return list(map(lambda x: x[1], filter(lambda x: x[0] >= start , enumerate(lista))))
print(getLast_ten_countries(countries2))

# Sort countries by name, by capital, by population
def sorted_countries(campo, lista, descending=False):
    return sorted(lista, key=lambda x:x[campo], reverse=descending)
#print(sorted_countries("name", countries_data))
#print(f"Sorted by capital {sorted_countries("capital", countries_data)}")
#print(sorted_countries("population", countries_data))

# Sort out the ten most spoken languages by location.
from collections import Counter

def get_top_languages(countries_data, top_n=10):
    all_languages = []
    for country in countries_data:
        all_languages.extend(country['languages'])  # agregamos todos los idiomas

    language_counter = Counter(all_languages)  # contamos cuántas veces aparece cada idioma
    return language_counter.most_common(top_n)  # devolvemos los top_n idiomas más comunes

# Ejecución
top_languages = get_top_languages(countries_data)
for lang, count in top_languages:
    print(f"{lang}: {count} países")

from functools import reduce
from collections import Counter

def get_top_languages(data, top_n=10):
    # 1. Extraer la lista completa de idiomas usando map y reduce
    all_languages = reduce(
        lambda acc, country: acc + country['languages'],  # acumulador
        data,
        []  # inicial
    )

    # 2. Contar frecuencias
    language_counts = Counter(all_languages)

    # 3. Ordenar por valor (cantidad de países), de mayor a menor
    sorted_languages = sorted(language_counts.items(), key=lambda x: x[1], reverse=True)

    # 4. Retornar los top_n
    return sorted_languages[:top_n]

# 🔍 Ejemplo de ejecución
top_languages = get_top_languages(countries_data)
for lang, count in top_languages:
    print(f"{lang}: {count} países")


# Sort out the ten most populated countries.
def get_most_populated_countries(data, top_n=10):
    return list(
        map(
            lambda c: {'name': c['name'], 'population': c['population']},
            sorted(data, key=lambda c: c['population'], reverse=True)[:top_n]
        )
    )
top_populated = get_most_populated_countries(countries_data)

for country in top_populated:
    print(f"{country['name']}: {country['population']} habitantes")