import requests

#from countries_info import countries_data

from collections import Counter
# Iterate 0 to 10 using for loop, do the same using while loop
for i in range(10):
    print(i)

number = 0
while number < 10:
    #print(number)
    number += 1

# Iterate 10 to 0 using for loop, do the same using while loop
for i in range(10, -1, -1):
    print(i)

numbers = 10
while numbers >= 0:
    print(numbers)
    numbers -= 1

# Write a loop that makes seven calls to print(), so we get on the output the following triangle:
for i in range(1, 8):
    print("#" * i)

# Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #

for i in range(8):
    for j in range(9):
        print("#", end=" ")
    print()


""" Print the following pattern:

0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100 """

for i in range(0,11):
    print(f"{i} x {i} = {i*i}")


def tabla_multiplicar(inicio, fin):
    # Encabezado
    print("    ", end="")
    for j in range(inicio, fin + 1):
        print(f"{j:>4}", end="")
    print()
    print("    " + "----" * (fin - inicio + 1))

    # Filas de la tabla
    for i in range(inicio, fin + 1):
        print(f"{i:>3} |", end="")  # Encabezado de fila
        for j in range(inicio, fin + 1):
            print(f"{i * j:>4}", end="")
        print()  # salto de línea después de cada fila

tabla_multiplicar(1,10)
""" Salida: 
       1   2   3   4   5   6   7   8   9  10
    ----------------------------------------
  1 |   1   2   3   4   5   6   7   8   9  10
  2 |   2   4   6   8  10  12  14  16  18  20
  3 |   3   6   9  12  15  18  21  24  27  30
  4 |   4   8  12  16  20  24  28  32  36  40
  5 |   5  10  15  20  25  30  35  40  45  50
  6 |   6  12  18  24  30  36  42  48  54  60
  7 |   7  14  21  28  35  42  49  56  63  70
  8 |   8  16  24  32  40  48  56  64  72  80
  9 |   9  18  27  36  45  54  63  72  81  90
 10 |  10  20  30  40  50  60  70  80  90 100 """

# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
technologies = ['Python', 'Numpy','Pandas','Django', 'Flask']
for technologi in technologies:
    print(f"{technologi}")

# Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(101):
    if i % 2 == 0:
        print(i)

for i in range(0, 101, 2):
    print(i)

# Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(101):
    if i % 2 != 0:
        print(i)

for i in range(1, 101, 2):
    print(i)

# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
suma = 0
for i in range(0,101):
    suma += i
print(f"The sum of all numbers is {suma}.") #5050

print(f"The sum of all numbers is {sum(range(101))}")

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
# The sum of all evens is 2550. And the sum of all odds is 2500.
suma_evens = 0
suma_odds = 0 

for i in range(101): 
    if i % 2 == 0:
       suma_evens += i
    else:
        suma_odds += i
print(f"The sum of all evens is {suma_evens}. And the sum of all odds is {suma_odds}.")

# Go to the data folder and use the countries.py file. 
# Loop through the countries and extract all the countries containing the word land.

url = "https://raw.githubusercontent.com/Asabeneh/30-Days-Of-Python/master/data/countries.py"
response = requests.get(url)
if response.status_code == 200:
    lines = response.text.splitlines()
    for line in lines:
        if "land" in line:
            print(line.strip())
else:
    print("No se puede acceder al archivo Código de estado:", response.status_code)

# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
frutas = ['banana', 'orange', 'mango', 'lemon']
n = len(frutas)
for i in range(n // 2):
    frutas[i], frutas[n - 1 - i] = frutas[n - 1 - i], frutas[i]
print(frutas)

# Go to the data folder and use the countries_data.py file.

    # What are the total number of languages in the data
    # Find the ten most spoken languages from the data
    # Find the 10 most populated countries in the world
url_2 = "https://raw.githubusercontent.com/Asabeneh/30-Days-Of-Python/master/data/countries_data.py"
response = requests.get(url_2)

if response.status_code == 200:
    global_vars = {}
    exec(response.text, global_vars)
    if "countries_data" in global_vars:
        countries_data = global_vars["countries_data"]
        print("Datos cargados correctamente. Total de países:", len(countries_data))
    else:
        print("No se encontró la variable 'countries_data' en el archivo.")
else: 
    print("No se puede acceder al archivo Código de estado:", response.status_code)

file_path = 'countries_info.py'

global_vars = {}
with open(file_path, 'r', encoding='utf-8') as f:
    code = f.read()
    exec(code, global_vars)

# Accedemos a la variable 'countries_data' del archivo ejecutado
if 'countries_data' in global_vars:
    countries_data = global_vars['countries_data']
    print(f"Total de países cargados: {len(countries_data)}")
else:
    print("No se encontró la variable 'countries_data' en el archivo.")


""" # 1. Total de países

print(f"Total de países cargados: {len(countries_data)}")

# 2. Total de idiomas únicos
unique_languages = set()

for country in countries_data:
    for language in country['languages']:
        unique_languages.add(language)

print(f"\nTotal de idiomas únicos: {len(unique_languages)}")

# 3. Las 10 lenguas más habladas (por cantidad de países que las hablan)
language_counter = Counter()

for country in countries_data:
    for language in country['languages']:
        language_counter[language] += 1

top_10_languages = language_counter.most_common(10)

print("\n🔝 Las 10 lenguas más habladas (por número de países):")
for lang, count in top_10_languages:
    print(f"{lang}: hablada en {count} países")

# 4. Los 10 países más poblados
most_populated = sorted(countries_data, key=lambda x: x['population'], reverse=True)[:10]

print("\n🌍 Los 10 países más poblados:")
for country in most_populated:
    print(f"{country['name']}: {country['population']:,} habitantes") """

from countries_info import countries_data
from collections import Counter

# Total de idiomas distintos
all_languages = [lang for country in countries_data for lang in country['languages']]
unique_languages = set(all_languages)
print(f"Total number of unique languages: {len(unique_languages)}")

# Diez idiomas más hablados
language_counter = Counter(all_languages)
most_spoken_languages = language_counter.most_common(10)
print("\nTop 10 most spoken languages:")
for lang, count in most_spoken_languages:
    print(f"{lang}: {count} countries")

# Diez países más poblados
most_populated = sorted(countries_data, key=lambda x: x['population'], reverse=True)[:10]
print("\nTop 10 most populated countries:")
for country in most_populated:
    print(f"{country['name']}: {country['population']}")

""" Total de países cargados: 250
Total number of unique languages: 112

Top 10 most spoken languages:
English: 91 countries
French: 45 countries
Arabic: 25 countries
Spanish: 24 countries
Portuguese: 9 countries
Russian: 9 countries
Dutch: 8 countries
German: 7 countries
Chinese: 5 countries
Serbian: 4 countries

Top 10 most populated countries:
China: 1377422166
India: 1295210000
United States of America: 323947000
Indonesia: 258705000
Brazil: 206135893
Pakistan: 194125062
Nigeria: 186988000
Bangladesh: 161006790
Russian Federation: 146599183
Japan: 126960000 """