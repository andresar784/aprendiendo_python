import statistics
import requests


empty_list = list()
print(len(empty_list))

# Declare a list with more than 5 item
frutas = ["bananas", "manzanas", "peras", 1, 4]

# Find the length of your list
print(len(frutas)) # 5

# Get the first item, the middle item and the last item of the list
primer_item = frutas[0]
segundo_item = frutas[2]
tercer_item = frutas[4]
print(f"First item, {primer_item}, the middle item {segundo_item} and the last item {tercer_item}")
# First item, bananas, the middle item peras and the last item 4
# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Andres", 44, 1.80, "Married", "Juan Manuel Blanes 2491"]

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
# Print the list using print()
print(it_companies)
# Print the number of companies in the list
print(len(it_companies)) #7
# Print the first, middle and last company
print(f"Print the first {it_companies[0]}, middle, {it_companies[len(it_companies)// 2]} and last company {it_companies[len(it_companies) - 1]}")
# Print the first Facebook, middle, Apple and last company Amazon

# Print the list after modifying one of the companies
indice = it_companies.index("Facebook")
it_companies[indice] = "Meta"
print(it_companies)
# voy en el numero 10
# Add an IT company to it_companies
it_companies.append("Ebay")
print(f"Companies", it_companies) # Companies ['Meta', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Ebay']
# Insert an IT company in the middle of the companies list
midle_index = len(it_companies)// 2 # para hallar la mitad de una lista
it_companies.insert(midle_index,"Mercado Libre")
print(f"Companies", it_companies) # Companies ['Meta', 'Google', 'Microsoft', 'Apple', ' Mercado Libre', 'IBM', 'Oracle', 'Amazon', 'Ebay']

# Change one of the it_companies names to uppercase (IBM excluded!)
for i in range(len(it_companies)):
    if it_companies[i] != "IBM": 
        it_companies[i] = it_companies[i].upper()
        break
print(it_companies) # ['META', 'Google', 'Microsoft', 'Apple', ' Mercado Libre', 'IBM', 'Oracle', 'Amazon', 'Ebay']

# Join the it_companies with a string '#;  '
it_companie = "#, ".join(it_companies)
print(it_companie)

# Check if a certain company exists in the it_companies list.
company_to_check = "Google"
company_exists = company_to_check in it_companies
if company_exists:
    print(f"La empresa '{company_to_check}' **sí existe** en la lista de compañías.")
else:
    print(f"La empresa '{company_to_check}' **no existe** en la lista de compañías.")
# print(f"Does {company_to_check} exist in the list? {company_exists}")

def verificar_empresa(nombre_empresa, lista_empresas):
    if nombre_empresa in lista_empresas:
        print(f"La empresa '{nombre_empresa}' **sí existe** en la lista de compañías.")
    else:
        print(f"La empresa '{nombre_empresa}' **no existe** en la lista de compañías.")

verificar_empresa("Amazon", it_companies)
verificar_empresa("Tesla", it_companies)

# Lista original de compañías
# it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 1️⃣ Sort the list using sort() method
sorted_companies = sorted(it_companies)
print("Lista ordenada:", sorted_companies)

# 2️⃣ Reverse the list in descending order using reverse() method
reversed_companies = sorted(it_companies, reverse=True)
print("Lista en orden descendente:", reversed_companies)

# 3️⃣ Slice out the first 3 companies from the list
primeras_tres = it_companies[:3]
restantes_despues_primeras = it_companies[3:]
print("Lista original", it_companies)
print("Primeras tres compañías:", primeras_tres)
print("Resto después de eliminar las tres primeras:", restantes_despues_primeras)

# 4️⃣ Slice out the last 3 companies from the list
ultimas_tres = it_companies[-3:]
restantes_sin_ultimas = it_companies[:-3]
print("Lista original", it_companies)
print("Últimas tres compañías:", ultimas_tres)
print("Resto después de eliminar las tres últimas:", restantes_sin_ultimas)

# 5️⃣ Slice out the middle IT company or companies from the list
middle_sliced = it_companies.copy()  # Copiamos para trabajar sobre esta
mid_index = len(middle_sliced) // 2

if len(middle_sliced) % 2 != 0:
    middle_company = middle_sliced[mid_index]
    del middle_sliced[mid_index]
    print("Compañía del medio:", middle_company)
else:
    middle_companies = middle_sliced[mid_index - 1: mid_index + 1]
    del middle_sliced[mid_index - 1: mid_index + 1]
    print("Compañías del medio:", middle_companies)

print("Lista después de eliminar la(s) del medio:", middle_sliced)

# 6️⃣ Remove the first IT company from the list
sin_primera = it_companies[1:]
print("Lista original", it_companies)
print("Lista sin la primera compañía:", sin_primera)

# Remove the last IT company from the list
sin_ultima = it_companies[:-1]
print("Lista original", it_companies)
print("Lista sin la ultima compañía:", sin_ultima)

# Remove all IT companies from the list
lista_vaciada = it_companies.clear()
print(lista_vaciada)

# Destroy the IT companies list
# del it_companies elimina toda la lista
# it_companies = None La variable it_companies ahora no referenciará una lista, 
# sino que tendrá el valor None. Si intentas acceder a la variable, verás que ya no es una lista.
# print(it_companies)

# Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
technologies = front_end + back_end
print("Technologies" , technologies)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, 
# then insert Python and SQL after Redux.

full_stack = technologies
full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")
print(full_stack)

# Manera mas eficiente

# Encontrar la posición de "Redux"
redux_index = full_stack.index("Redux")

# Insertar "Python" y "SQL" después de "Redux"
full_stack.insert(redux_index + 1, "Python")
full_stack.insert(redux_index + 2, "SQL")

# Imprimir el resultado final
print("Ultima opcion mas eficiente", full_stack)

def insert_after_technology(full_stack, tech_list, tech_to_find, new_technologies):
    """
    Inserta nuevas tecnologías después de una tecnología específica en la lista unida.

    Args:
        full_stack (list): La lista combinada de tecnologías.
        tech_list (list): La lista de tecnologías a unir con `full_stack`.
        tech_to_find (str): La tecnología en la cual queremos insertar después.
        new_technologies (list): Nuevas tecnologías a insertar después de `tech_to_find`.

    Returns:
        list: Lista con las nuevas tecnologías insertadas si todo es válido.
    """
    # Unir las listas
    full_stack = full_stack + tech_list
    
    # Verificar si la tecnología a buscar existe en la lista
    if tech_to_find not in full_stack:
        print(f"Error: {tech_to_find} no se encuentra en la lista.")
        return full_stack  # Devuelve la lista sin cambios
    
    # Encontrar el índice de la tecnología a buscar
    index_to_insert = full_stack.index(tech_to_find)

    # Insertar las nuevas tecnologías después de la tecnología encontrada
    for i, tech in enumerate(new_technologies):
        full_stack.insert(index_to_insert + 1 + i, tech)
    
    return full_stack

# Ejemplo de uso
technologies = ['JavaScript', 'React', 'Node.js', 'Redux']
otras_technologies = ['HTML', 'CSS', 'Angular']
new_technologies = ['Python', 'SQL']

# Llamada a la función
full_stack = insert_after_technology(technologies, otras_technologies, "Redux", new_technologies)

# Imprimir el resultado
print(full_stack)

# Part 2 

# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages_sorted = sorted(ages)
print("Original",ages)
print(ages_sorted)
# min
edad_minima = min(ages_sorted)
edad_maxima = max(ages_sorted)

print(edad_minima, edad_maxima)

# Find the median age (one middle item or two middle items divided by two)
def encontrar_mediana(lista):
    n = len(lista)
    median_age
    if n % 1 :
        return median_age[lista // 2]
    else:
        medio1 = lista[n // 2 - 1]
        medio2 = lista[n // 2]
        return(medio1 + medio2) // 2
    
median_age = statistics.median(ages_sorted)
print(f"Se encontro mediante la libreria", median_age)
mediana = encontrar_mediana(ages_sorted)
print(f"La mediana mediante la funcion es", mediana)
                    
# Find the average age (sum of all items divided by their number )
diviendo = len(ages_sorted)
divisor = sum(ages_sorted)
average = divisor // diviendo
print(f"El promedio es: {average}, la suma es {divisor} y el total de items es {diviendo}")

# Find the range of the ages (max minus min)
range = max(ages_sorted) - min(ages_sorted) 
print(range)
# Compare the value of (min - average) and (max - average), use abs() method
value_compared = abs(edad_minima - average)
print(value_compared)

# Find the middle country(ies) in the countries list
url = "https://raw.githubusercontent.com/Asabeneh/30-Days-Of-Python/master/data/countries.py"
response = requests.get(url)
contenido = response.text

globals_ = {}
exec(contenido, globals_)

# Ahora tenemos la lista 'countries' disponible
countries = globals_['countries']
cantidad = len(countries)
medio = cantidad // 2
pais_del_medio = countries[medio]
print(pais_del_medio)

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
if medio % 2 == 0:
    paises_1 = countries[:medio]
    paises_2 = countries[medio:]
else:
    paises_1 = countries[:medio + 1]
    paises_2 = countries[medio + 1:]


print(f"Primera mitad {len(paises_1)} {paises_1}")
print(f"Segunda mitad {len(paises_2)} {paises_2}")

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. 
# Unpack the first three countries and the rest as scandic countries.
countries_2 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
china, russia, usa, *scandic_countries = countries_2
print(china)
print(russia)
print(usa)
print(scandic_countries)