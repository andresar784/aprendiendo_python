# Filter only negative and zero in the list using list comprehension
import math


numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negativos = [i for i in numbers if i <= 0]
print(negativos)

# Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flatten_list = [num for sublist in list_of_lists for inner in sublist for num in inner]
print(flatten_list)

# Using list comprehension create the following list of tuples:
lista_de_tupla = [(i, i ** 1, i ** 2, i ** 3, i ** 4, i ** 5, i ** 6, ) for i in range(11)]
print(lista_de_tupla)

# Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flatten_list_countries = [[pais.upper(), pais[:3].upper(), capital.upper()]
                          for sublist in countries
                          for (pais, capital) in sublist]
print(flatten_list_countries)
# Change the following list to a list of dictionaries:
list_of_dict = { pais.upper():
                {
                    "code" : pais[:3].upper(),
                    "capital"  : capital.upper()
                }
                for sublist in countries
                for (pais, capital) in sublist
                }
print(list_of_dict)
# Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], 
         [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated_string = [f"{nombre} {apellido} " for sublist in names for (nombre, apellido) in sublist]
print(concatenated_string)

# Write a lambda function which can solve a slope or y-intercept of linear functions.
slope = lambda m,x,b : m * x + b
print(slope(2,3,1))
